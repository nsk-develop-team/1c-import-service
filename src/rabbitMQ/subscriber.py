import functools
import pika
import os
import json
import logging


from src.models import Order


def subscribe():
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    # New complete order from queue
    # new_completed_order_callback = functools.partial(new_completed_order, args=(1, 2)
    channel.queue_declare(queue='new_completed_order')
    channel.basic_consume('new_completed_order', auto_ack=True, on_message_callback=new_completed_order)

    channel.start_consuming()
    connection.close()


def new_completed_order(ch, method, properties, body):
    try:
        data = json.loads(body)
        order = Order(data)

        # TODO: realize sending order

    except Exception as e:
        logging.error('GET ORDER ERROR: ' + str(e))
