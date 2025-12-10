import asyncio
import logging
from typing import Callable, Any, TypeVar, Coroutine, Optional
from functools import wraps

logger = logging.getLogger(__name__)

# Type variable for the decorated function's return type
R = TypeVar("R")

class CircuitBreaker:
    def __init__(self, failure_threshold: int, recovery_timeout: int, name: str = "circuit_breaker"):
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time: Optional[datetime] = None
        self.is_open = False

    def _open(self):
        self.is_open = True
        self.last_failure_time = datetime.now()
        logger.warning(f"Circuit breaker '{self.name}' opened due to {self.failure_threshold} failures.")

    def _close(self):
        self.is_open = False
        self.failures = 0
        self.last_failure_time = None
        logger.info(f"Circuit breaker '{self.name}' closed.")

    def _half_open(self):
        logger.info(f"Circuit breaker '{self.name}' is half-open, allowing a trial request.")

    def __call__(self, func: Callable[..., Coroutine[Any, Any, R]]) -> Callable[..., Coroutine[Any, Any, R]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> R:
            if self.is_open:
                if (datetime.now() - self.last_failure_time).total_seconds() > self.recovery_timeout:
                    # Attempt to half-open
                    self._half_open()
                    try:
                        result = await func(*args, **kwargs)
                        self._close() # Success, close the circuit
                        return result
                    except Exception as e:
                        logger.error(f"Circuit breaker '{self.name}' trial request failed. Keeping circuit open. Error: {e}")
                        raise # Re-raise original exception
                else:
                    logger.warning(f"Circuit breaker '{self.name}' is open. Request blocked.")
                    raise CircuitBreakerOpenException(f"Circuit breaker '{self.name}' is open.")

            try:
                result = await func(*args, **kwargs)
                if self.failures > 0: # Reset failures on success if not already zero
                    self._close()
                return result
            except Exception as e:
                self.failures += 1
                logger.error(f"Service call failed. Current failures: {self.failures}/{self.failure_threshold}. Error: {e}")
                if self.failures >= self.failure_threshold:
                    self._open()
                raise # Re-raise original exception

        return wrapper

class CircuitBreakerOpenException(Exception):
    """Exception raised when a circuit breaker is open."""
    pass


def retry(
    max_attempts: int = 3,
    initial_delay: float = 0.5,
    exponential_backoff: bool = True,
    catch_exceptions: tuple = (Exception,),
    logger_obj: Optional[logging.Logger] = None,
):
    """
    Decorator for retrying asynchronous functions with exponential backoff.
    """
    _logger = logger_obj or logger

    def decorator(func: Callable[..., Coroutine[Any, Any, R]]) -> Callable[..., Coroutine[Any, Any, R]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> R:
            delay = initial_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)
                except catch_exceptions as e:
                    _logger.warning(
                        f"Attempt {attempt}/{max_attempts} for {func.__name__} failed: {e}"
                    )
                    if attempt < max_attempts:
                        await asyncio.sleep(delay)
                        if exponential_backoff:
                            delay *= 2
                    else:
                        _logger.error(
                            f"Max retry attempts ({max_attempts}) reached for {func.__name__}."
                        )
                        raise # Re-raise the last exception

        return wrapper

    return decorator
