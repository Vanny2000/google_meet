import os
import subprocess
from datetime import datetime, timedelta

import telebot
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Google Calendar API setup
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def check_and_generate_token():
    if not os.path.exists("token.json"):
        print("token.json not found. Generating new token...")
        subprocess.run(["python", "generate_token.py"], check=True)

    if not os.path.exists("token.json"):
        raise FileNotFoundError("Failed to generate token.json")


check_and_generate_token()
creds = Credentials.from_authorized_user_file("token.json", SCOPES)
service = build("calendar", "v3", credentials=creds)

# Telegram Bot setup
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def create_meet_link():
    event = {
        "summary": "Daily Scrum Meeting",
        "start": {
            "dateTime": datetime.now().isoformat(),
            "timeZone": os.getenv("TIMEZONE"),
        },
        "end": {
            "dateTime": (datetime.now() + timedelta(minutes=30)).isoformat(),
            "timeZone": os.getenv("TIMEZONE"),
        },
        "conferenceData": {
            "createRequest": {
                "requestId": f"daily-scrum-{datetime.now().strftime('%Y%m%d')}",
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        },
    }

    event = (
        service.events()
        .insert(calendarId="primary", body=event, conferenceDataVersion=1)
        .execute()
    )
    return event["hangoutLink"]


def send_telegram_message(meet_link):
    message = f"Daily Scrum Meeting Link: {meet_link}"
    bot.send_message(TELEGRAM_GROUP_ID, message)


def main():

    now = datetime.now()
    meet_link = create_meet_link()
    send_telegram_message(meet_link)
    print(
        f"Meeting link sent to Telegram group on {now.strftime('%Y-%m-%d')} at {now.strftime('%H:%M:%S')}."
    )


if __name__ == "__main__":
    main()
