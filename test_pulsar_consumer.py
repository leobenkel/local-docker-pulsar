#!/usr/bin/python

import pulsar
import sys

client = pulsar.Client('pulsar://pulsar-server:6650')
consumer = client.subscribe('my-topic',
                            subscription_name='my-sub')

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    sys.stdout.flush()
    consumer.acknowledge(msg)

client.close()
