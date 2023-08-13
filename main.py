from time import sleep
from kafka import KafkaProducer

topic_name ='my_topic1'
producer =KafkaProducer(bootstrap_servers ='localhost:9092')


for e in range(10):
    data =f"Message {e}"
    print(data)
    producer.send(topic_name,data.encode('utf-8'))
    sleep(5)

