from kafka import KafkaConsumer
from collections import Counter
import json

if __name__ == '__main__':

    consumer = KafkaConsumer('example_topic',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='example-group',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    action_counter = Counter()

    for message in consumer:
        action = message.value['action']
        action_counter[(message.value['user_id'], action)] += 1

    most_active_users = action_counter.most_common()

    for (user_id, action), count in most_active_users:
        print(f"User {user_id} is the user with the most amount of {action} actions: {count}")

    consumer.close()
