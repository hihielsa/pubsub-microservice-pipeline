from flask import Flask, request
from google.cloud import pubsub_v1
import os

app = Flask(__name__)

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
TOPIC_ID = "demo-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/publish", methods=["POST"])
def publish():
    data = request.get_json()
    message = data.get("text", "No message")

    publisher.publish(topic_path, message.encode("utf-8"))
    return f"Published: {message}", 200
