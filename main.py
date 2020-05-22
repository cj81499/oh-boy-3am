import twitter
import os

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

if not all((CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)):
    print(".env is missing required field(s)")
    exit(1)


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """

    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET,
    )

    print("starting upload")
    with open("3am.mp4", "rb") as f:
        media_id = api.UploadMediaChunked(f)
        print(media_id)
    print("upload done")

    api.PostUpdate("Oh boy 3am!", media=[media_id])


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    hello_pubsub(None, None)
