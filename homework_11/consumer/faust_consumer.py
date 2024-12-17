import faust_consumer
from collections import Counter

app = faust_consumer.app('kafka-stream',
                         broker='kafka://localhost:9092')

users_topic = app.topic('example_topic',
                        value_type=str)

action_counter = Counter()


@app.agent(users_topic)
async def process(actions):
    async for message in actions:
        action = message.value['action']
        action_counter[(message.value['user_id'], action)] += 1


@app.timer(interval=5.0)
async def print_counts():
    most_active_users = action_counter.most_common()

    for (user_id, action), count in most_active_users:
        print(f"User {user_id} is the user with the most amount of {action} actions: {count}")

if __name__ == '__main__':
    app.main()
