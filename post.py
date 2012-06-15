#!/usr/bin/env python

"""
Send messages to the queue
"""

import sys
import pika
import scripture.logger as logger

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange = 'log_test', type = 'topic')

message = 'A debug message'
channel.basic_publish(exchange = 'log_test',
                      routing_key = 'local0.debug',
                      body = message)
logger.LOGGER.info("Sent '%s'" % message)
                      
message = 'An informational message'
channel.basic_publish(exchange = 'log_test',
                      routing_key = 'local0.info',
                      body = message)
logger.LOGGER.info("Sent '%s'" % message)

connection.close()

sys.exit(0)
