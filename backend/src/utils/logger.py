import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logger():
    logger = logging.getLogger("backend")
    logger.setLevel(logging.INFO)

    logHandler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        '%(levelname)s %(asctime)s %(name)s %(process)d %(threadName)s %(message)s'
    )
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    return logger

logger = setup_logger()

# Placeholder for metrics
def metric_counter(name: str, value: int = 1, tags: dict = None):
    tags_str = " ".join([f"{k}={v}" for k, v in tags.items()]) if tags else ""
    logger.info(f"metric_counter: {name}={value} {tags_str}")

def metric_gauge(name: str, value: float, tags: dict = None):
    tags_str = " ".join([f"{k}={v}" for k, v in tags.items()]) if tags else ""
    logger.info(f"metric_gauge: {name}={value} {tags_str}")
