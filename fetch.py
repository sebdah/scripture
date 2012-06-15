#!/usr/bin/env python

"""
Fetch messages from the queue
"""

##################################
#
#        SETTINGS
#
##################################

EXCHANGE = 'log_test'

RABBITMQ_SERVER = 'localhost'

CONFIGURATION = {
    'version': 0,
    'listeners': [
        'local0.*',
    ],
    'config': {
        'local0': {
            'info': {
                'handlers': ['file',],
                'formatter': 'default',
                'loglevel': 'debug'
            }
        }
    },
    'formatters': {
        'default': '{{DATETIME_UTC}} - {{FACILITY}} - {{SEVERITY}} - {{MESSAGE}}',
    },
    'handlers': {
        'file': {
            'type': 'file_handler',
            'path': '/Users/sebastian/git/scripture/logs',
            'filename': 'test.log',
        },
    }
}

##################################
#
#        CODE
#
##################################

import sys
import pika
import scripture.scripture
import scripture.handlers.file
import scripture.logger as logger

# Create the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Declare the exchange
channel = connection.channel()
channel.exchange_declare(exchange = EXCHANGE, type = 'topic')

# Fetch a queue from the exchange
result = channel.queue_declare(exclusive = True)
queue_name = result.method.queue

# Register the routing keys
for listener in CONFIGURATION['listeners']:
    channel.queue_bind(exchange = EXCHANGE, queue = queue_name, routing_key = listener)

def callback(ch, method, properties, message):
    scripture.scripture.write_log(ch, method, properties, message, CONFIGURATION)

# Configure the consumer
channel.basic_consume(callback, queue = queue_name, no_ack = True)

logger.LOGGER.info('Waiting for messages. To exit press CTRL+C')

# Start consuming (endless loop)
channel.start_consuming()

sys.exit(0)
