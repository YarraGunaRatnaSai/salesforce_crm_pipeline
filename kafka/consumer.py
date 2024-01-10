from kafka import KafkaConsumer
import json

def consume_messages(topic):
    """
    Consume messages from a Kafka topic.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    for message in consumer:
        print(f"Received message: {message.value}")

if __name__ == "__main__":
    consume_messages("data_integration_events")
