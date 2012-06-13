#!/usr/bin/env python

"""
Send messages to the queue
"""

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange = 'direct_logs', type = 'direct')

channel.basic_publish(exchange = 'direct_logs',
                      routing_key = 'error',
                      body = 'Hello World!')

print " [x] Sent 'Hello World!'"

connection.close()

sys.exit(0)
