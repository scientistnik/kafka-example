#!/usr/bin/env python

from kafka import KafkaConsumer
import msgpack

KAFKA_SERVER = 'localhost:9092'
SEND_TOPIC = 'topic-answer'

def test(msg):
  print(msg.value)

consumer = KafkaConsumer(bootstrap_servers = KAFKA_SERVER, value_deserializer=msgpack.loads)
consumer.subscribe([SEND_TOPIC])

for msg in consumer:
  print(msg.value)