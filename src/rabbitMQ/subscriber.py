import json
import os
import logging

import pika

from ..web.services import auth, test_connection, put_data_to_web_1c

logger = logging.getLogger('web')


def subscribe():
    """Init RabbitMQ queues subscriber.
    """
    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare(queue='new_completed_orders')
        channel.basic_consume('new_completed_orders', auto_ack=True, on_message_callback=get_orders)

        channel.start_consuming()
        connection.close()
    except Exception as err:
        logger.error(f'QueueSubscribeError: {err}')


def get_orders(ch, method, properties, body):
    """Handle orders: parse and save
    """
    try:
        data = json.loads(body)

        client_1c = auth()
        test_connection(client_1c)
        result = put_data_to_web_1c(client_1c, data)
        if not result:
            logger.info('Data doesn\'t send')
    except Exception as err:
        logger.error(f'{err}')
