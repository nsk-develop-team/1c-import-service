import json
import logging
import os

import pika

logger = logging.getLogger('web')


def publish_new_data(data):
    """Publish 1C data message in RabbitMQ queue.
    """
    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)

        channel = connection.channel()
        channel.queue_declare(queue='data_to_1C')
        channel.basic_publish(exchange='', routing_key='data_to_1C',
                              body=json.dumps(data, ensure_ascii=False),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))

        connection.close()
    except Exception as e:
        logger.error('PUBLISHER ERROR: ' + str(e))
