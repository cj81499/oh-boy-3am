import base64
from dotenv import load_dotenv
import os

from twitter import *

load_dotenv()

CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET")

oauth_token, oauth_secret = oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET)

print(f"OAUTH_TOKEN={oauth_token}")
print(f"OAUTH_SECRET={oauth_secret}")

# twitter = Twitter(auth=OAuth(
    # oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Now work with Twitter
# twitter.statuses.update(status='Hello, world!')
