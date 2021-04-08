import os

import twitter

if not os.getenv("CI"):
    from dotenv import load_dotenv
    load_dotenv()

# Read environment variables
env = {
    key: os.getenv(key) for key in
    ("CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_SECRET")
}

if not all(env.values()):
    print("missing required environment variable(s)")
    exit(1)

# create twitter api object
twitter_api = twitter.Api(
    consumer_key=env.get("CONSUMER_KEY"),
    consumer_secret=env.get("CONSUMER_SECRET"),
    access_token_key=env.get("ACCESS_TOKEN"),
    access_token_secret=env.get("ACCESS_SECRET"),
)

# upload video media
print("start upload video")
with open("3am.mp4", "rb") as f:
    media_id = twitter_api.UploadMediaChunked(f)
print("finish upload video")

# post tweet w/ the media we uploaded
print("start posting tweet")
twitter_api.PostUpdate("Oh boy 3am!", media=[media_id])
print("finish posting tweet")
