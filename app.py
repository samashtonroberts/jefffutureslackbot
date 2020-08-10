import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from prompt_creator import make_future_prompt

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# For simplicity we'll store our app data in-memory with the following data structure.
# prompts_sent = {"channel": {"user_id": OnboardingTutorial}}
prompts_sent = {}

def send_prompt(user_id: str, channel: str):
    # Create a new prompt.
    new_prompt = make_future_prompt()

    # Post the new prompt in Slack
    response = slack_web_client.chat_postMessage(**new_prompt)

    # Store the message sent in prompts_sent
    if channel not in prompts_sent:
        prompts_sent[channel] = {}
    prompts_sent[channel][user_id] = new_prompt

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")


    if text and text.lower() == "start":
        return start_onboarding(user_id, channel_id)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)
