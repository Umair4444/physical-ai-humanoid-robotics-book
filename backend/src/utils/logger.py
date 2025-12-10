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
