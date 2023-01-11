# Create rotating logs (file) with custom timezoned timestamp

import time
import logging
import logging.handlers
from pytz import timezone
from datetime import datetime

def log_setup():
    log_handler = logging.handlers.RotatingFileHandler('my.log', mode='a', maxBytes=1000, backupCount=2, encoding=None, delay=False, errors=None)
    formatter = logging.Formatter(
        '%(asctime)s Elasticsearch-Logs [%(process)d]: %(message)s',
        '%b %d %Y %H:%M:%S')
    formatter.converter = lambda *args: datetime.now(tz=timezone('America/Chicago')).timetuple()  #time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)

log_setup();
