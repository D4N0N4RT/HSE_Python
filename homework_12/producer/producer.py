import time
import json
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer


KAFKA_BROKER = "localhost:9092"
TRANSACTIONS_TOPIC = "transactions"

DB_CONFIG = {
    "host": "postgres",
    "port": 5432,
    "database": "python_db",
    "user": "user",
    "password": "pass"
}


def generate_transaction(user_id):
    transaction_id = random.randint(1000, 9999)
    amount = round(random.uniform(50, 2000), 2)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23),
                                           minutes=random.randint(0, 59))
    location = random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])

    return {
        "transaction_id": transaction_id,
        "user_id": user_id,
        "amount": amount,
        "timestamp": timestamp.isoformat(),
        "location": location
    }


def send_to_kafka(producer):
    # Генерируем и отправляем транзакции в топик 'transactions'
    for user_id in range(1, 101):  # Для 100 пользователей
        for _ in range(10):  # Каждому пользователю по 10 транзакций
            transaction = generate_transaction(user_id)
            producer.send(TRANSACTIONS_TOPIC, transaction)

    producer.close()


def main():
    # Initialize Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print("Starting to send transactions to Kafka...")
    try:
        send_to_kafka(producer)

    except KeyboardInterrupt:
        print("Process interrupted.")
    finally:
        producer.close()
        print("Kafka producer closed.")


if __name__ == "__main__":
    time.sleep(15)
    main()
