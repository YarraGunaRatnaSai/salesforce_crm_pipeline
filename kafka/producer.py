from kafka import KafkaProducer
import json

def send_message(topic, message):
    """
    Send a message to a Kafka topic.
    """
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    producer.send(topic, message)
    producer.close()

if __name__ == "__main__":
    sample_message = {"event": "data_integration_started", "status": "success"}
    send_message("data_integration_events", sample_message)
