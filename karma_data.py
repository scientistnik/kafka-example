from kafka import KafkaConsumer
from kafka import KafkaProducer
import msgpack

class KarmaData:
  #KAFKA_SERVER = '192.168.240.10:9092'
  KAFKA_SERVER = 'localhost:9092'
  SUB_TOPIC = 'topic-request'
  SEND_TOPIC = 'topic-answer'

  def __init__(self, kafka = KAFKA_SERVER,sub_topic = SUB_TOPIC, send_topic = SEND_TOPIC):
    self.consumer = KafkaConsumer(bootstrap_servers = self.KAFKA_SERVER, value_deserializer=msgpack.loads)
    self.producer = KafkaProducer(bootstrap_servers = self.KAFKA_SERVER, value_serializer=msgpack.packb)

    self.KAFKA_SERVER = kafka
    self.SUB_TOPIC = sub_topic
    self.SEND_TOPIC = send_topic

    self.consumer.subscribe([self.SUB_TOPIC])

  def hearing(self, callback):
    for msg in self.consumer:
      callback(msg)

  def send(self, msg):
    self.producer.send(self.SEND_TOPIC, msg)
    self.producer.flush()
