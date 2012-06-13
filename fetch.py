#!/usr/bin/env python

"""
Fetch messages from the queue
"""

##################################
#
#        SETTINGS
#
##################################

EXCHANGE = 'direct_logs'

SEVERITIES = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

ROUTING_KEY = 'error'

RABBITMQ_SERVER = 'localhost'

HANDLERS = {
    'active': 'file',
    'handlers': {
        'file': {
            'path': '/Users/sebastian/git/scripture/logs',
            'filename': 'test.log'
        }
    }
}

##################################
#
#        CODE
#
##################################

import sys
import pika
import scripture.handlers.file

def callback(ch, method, properties, message):
    if HANDLERS['active'] == 'file':
        scripture.handlers.file.log(message, config = HANDLERS['handlers']['file'])
    print " [x] Received %r" % (message,)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange = EXCHANGE, type = 'direct')
result = channel.queue_declare(exclusive =True)
queue_name = result.method.queue

channel.queue_bind(exchange = EXCHANGE, queue = queue_name, routing_key = ROUTING_KEY)

# Configure the consumer
channel.basic_consume(callback, queue = queue_name, no_ack = True)

print ' [*] Waiting for messages. To exit press CTRL+C'

# Start consuming (endless loop)
channel.start_consuming()

sys.exit(0)
