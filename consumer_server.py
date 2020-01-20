import json

from kafka import KafkaConsumer

import settings


def main():
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        auto_offset_reset="earliest",
        bootstrap_servers="localhost:9092",
        enable_auto_commit=False,
        group_id=0,
        value_deserializer=lambda mg: json.loads(mg.decode("utf-8")),
    )

    for message in consumer:
        print(message.value)


if __name__ == "__main__":
    main()