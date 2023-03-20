import logging
import os
import time
from logging import StreamHandler

from src.services.client import Client1С
from src.rabbitMQ import *
from tests.data import *

logger = logging.getLogger('web')
logger.setLevel(int(os.getenv('LOG_LEVEL')))
handler = StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler.setFormatter(formatter)

publish_new_data(create_order_data())
publish_new_data(create_withdraw_data())

server_url = os.getenv('1C_WEB_URL')
user = os.getenv('1C_USER_NAME')
password = os.getenv('1C_WEB_PASSWD')

client = Client1С(server_url, user, password)

subscribe(client)
