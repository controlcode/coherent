import logging
import pika

from flask_restful import Resource
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))

class Submit(Resource):
    """Rest endpoint to submit queue tasks"""

    @staticmethod
    def post(task):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 6672))
        channel = connection.channel()
        channel.queue_declare(queue='coh')
        channel.basic_publish(exchange='', routing_key='coh', body=task)
        logger.info("Task submitted to queue", task=task)
        connection.close()