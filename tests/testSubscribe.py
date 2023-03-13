import logging
import os
from logging import StreamHandler

from src.rabbitMQ import *

logger = logging.getLogger('web')
logger.setLevel(int(os.getenv('LOG_LEVEL')))
handler = StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler.setFormatter(formatter)

publish_new_completed_order()
subscribe()
