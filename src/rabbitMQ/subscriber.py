import json
import functools

import pika

from src.services.factory import XMLFactory
from src.services.archive import *

logger = logging.getLogger('web')


def subscribe(client_1c):
    """Init RabbitMQ queues subscriber.
    """
    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        send_data_1c_callback = functools.partial(send_data_1c, args=(client_1c,))
        channel.queue_declare(queue='data_to_1C')
        channel.basic_consume('data_to_1C', auto_ack=True, on_message_callback=send_data_1c_callback)

        channel.start_consuming()
        connection.close()
    except Exception as err:
        logger.error(f'QueueSubscribeError: {err}')


def send_data_1c(ch, method, properties, body, args):
    """Handle orders: parse and save
    """
    try:
        client = args[0]
        data = json.loads(body)

        factory = XMLFactory()
        file_path = factory.create_xml_file(data)
        zip_file = xml_to_zip(file_path)
        client.put_file_to_web_service(zip_file)
    except Exception as err:
        logger.error(f'{err}')
