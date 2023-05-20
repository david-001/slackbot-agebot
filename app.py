import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from datetime import datetime, date
import re

from dotenv import load_dotenv
load_dotenv()
import os
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

app = App(token=SLACK_APP_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)

def handle_age_request(channel, text):
    # Example string containing a date
    date_string = re.sub('<.*?>', '', text)
    date_string = re.sub(r"\s+", "", date_string)
    print(date_string)

    # Define the date format
    date_format = "%d-%m-%Y"

    # Convert the string to a datetime object
    date_object = datetime.strptime(date_string, date_format)
    dob = date_object.date()

    today = date.today()

    # Calculate the difference between the two dates
    delta = today - dob

    # Calculate the number of years
    years = delta.days // 365


    client.chat_postMessage(channel=channel, text=str(years))


@app.event("app_mention")
def handle_mention(event, say):
    channel = event.get('channel')
    text = event.get('text')
    handle_age_request(channel, text)


print("Start your bot")
handler = SocketModeHandler(app, app_token=SLACK_APP_TOKEN)
handler.start()
