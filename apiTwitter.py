import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIvV3QEAAAAAvxZlVMHroWUoCBt9BoRLPQNQNtY%3DvvyU4oZsZ6LEvwsyWfXN5XomfZnmZonqdVT4olqqeb18pnTjMP"

client = tweepy.Client(bearer_token=bearer_token)

username = input("Ingresa el nombre de usuario (sin @): ")

try:
    user = client.get_user(username=username)
    user_id = user.data.id

    tweets = client.get_users_tweets(id=user_id, max_results=5)

    print(f"\nÚltimos tweets de @{username}:\n")
    for tweet in tweets.data:
        print(f"- {tweet.text}\n")

except Exception as e:
    print("❌ Error:", e)
