#!/usr/bin/env python

from kafka import KafkaProducer
import msgpack

KAFKA_SERVER = 'localhost:9092'
SUB_TOPIC = 'topic-request'

producer = KafkaProducer(bootstrap_servers = KAFKA_SERVER, value_serializer=msgpack.packb)


data = {
  "taskid": "80be08dd-e11b-435c-91f0-cf3cd7ad76e2",
  "fio": "Филатов Евгений",
  "region": "Москва",
  "nameorg": "Апекс",
  "yuraddress": "Щелковское",
  "address": "Одинцово ул Белорусская д 3 кв 300",
  "seria": "9802",
  "number": "413592",
  "innfiz": "502400276890",
  "inn": "7707332613",
}

producer.send(SUB_TOPIC, {'say': 'hello'})
producer.send(SUB_TOPIC, data)
producer.flush()