Scripture
=========

Introduction
------------
Scripture is a project for easy log management. The initial goal of the project is to simplify the logging from Python applications via a queue to AWS S3 or to file. Even though Python + S3/file logging is the initial step, we will implement more languages and backends as the project moves forward.

Requirements
------------

* RabbitMQ
* Python 2.7
* Python pika

Development environment setup
-----------------------------

Install RabbitMQ on Mac OS X with MacPorts

    port install rabbitmq

Install RabbitMQ Manager

    sudo rabbitmq-plugins enable rabbitmq_management

Start RabbitMQ

    sudo rabbitmq-server

Install Python packages

    pip install pika