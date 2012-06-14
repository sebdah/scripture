#!/usr/bin/env python

"""
Send messages to the queue
"""

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange = 'log_test', type = 'topic')

channel.basic_publish(exchange = 'log_test',
                      routing_key = 'local0.info',
                      body = 'Hello World!')

print " [x] Sent 'Hello World!'"

connection.close()

sys.exit(0)
