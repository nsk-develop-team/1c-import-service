import json
import logging
import os

import pika


def publish_new_completed_order():
    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)

        data = {'amount': '178100',
                'account': 'GLHF',
                'currency': 'USD',
                'created_date': '2022-02-20 17:67',
                'local_currency': 'RUB',
                'rate': '71.87'}

        channel = connection.channel()
        channel.queue_declare(queue='new_completed_order')
        channel.basic_publish(exchange='', routing_key='new_completed_order',
                              body=json.dumps(data, ensure_ascii=False),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))

        connection.close()
    except Exception as e:
        logging.error('PUBLISHER ERROR: ' + str(e))
