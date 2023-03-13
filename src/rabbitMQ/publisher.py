import json
import logging
import os
import datetime

import pika

logger = logging.getLogger('web')


def publish_new_completed_order():
    """Publish order's message
    with test data in RabbitMQ queue.
    """
    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)

        data = [{
                'id': '72e5b400-bd6c-43e6-97e6-ca2ddf8fe36c',
                'amount': '1000',
                'account': 'CESAR',
                'currency': 'USD',
                'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                'local_currency': '100000.9',
                'rate': '70.67',
                'doc_number': '0000-999999',
                'comment': 'blablabla'
            },
            {
                'id': 'aaab8df5-388b-4b1c-9948-42720c42921a',
                'amount': '999',
                'account': 'VITOL',
                'currency': 'USD',
                'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                'local_currency': '87000.9',
                'rate': '70.67',
                'doc_number': '0000-999998',
                'comment': 'blablabla'
            }
        ]

        channel = connection.channel()
        channel.queue_declare(queue='new_completed_orders')
        channel.basic_publish(exchange='', routing_key='new_completed_orders',
                              body=json.dumps(data, ensure_ascii=False),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))

        connection.close()
    except Exception as e:
        logger.error('PUBLISHER ERROR: ' + str(e))
