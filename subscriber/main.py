from flask import Flask, request
import base64

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive():
    try:
        envelope = request.get_json()

        if not envelope:
            print("No envelope received")
            return "", 200

        message = envelope.get("message", {})
        data = message.get("data", "")

        if data:
            decoded = base64.b64decode(data).decode("utf-8")
            print("Received message:", decoded)
        else:
            print("No data field found")

        return "", 200

    except Exception as e:
        print("Error processing message:", str(e))
        return "", 200
