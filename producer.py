import random
from kafka import KafkaProducer
import json
from datetime import datetime

actions = ["login", "logout", "purchase", "click"]
data = []

for user_id in range(1, 100):
    for _ in range(random.randint(1, 10)):
        action = random.choice(actions)
        timestamp = datetime.now().isoformat()
        data.append({"user_id": user_id, "action": action, "timestamp": timestamp})

with open('client_actions.json', 'w') as f:
    json.dump(data, f)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all',
    retries=5,
    linger_ms=10
)

with open('client_actions.json') as f:
    data = json.load(f)
    for record in data:
        future = producer.send('example_topic', record)

producer.flush()
producer.close()
