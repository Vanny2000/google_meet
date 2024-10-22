# Daily Scrum Meeting Link Generator

This project automatically creates a Google Meet link for daily scrum meetings and sends it to a specified Telegram group.

## Prerequisites

- Python 3.7+
- A Google Cloud Platform account with the Google Calendar API enabled
- A Telegram bot token and group chat ID

## Setup

1. Clone the repository:

```
git clone https://github.com/Vanny2000/google_meet.git
cd google_meet
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Set up Google Calendar API:

- Go to the [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or select an existing one
- Enable the Google Calendar API
- Create credentials (OAuth 2.0 Client ID) for a desktop application
- Download the client configuration and save it as `credentials.json` in the project directory

6. Set up the Telegram bot:

- Create a new bot using the [BotFather](https://core.telegram.org/bots#6-botfather) on Telegram
- Note down the bot token
- Add the bot to your Telegram group
- Get the group chat ID (you can use the [@userinfobot](https://telegram.me/userinfobot) to find this)

7. Create a `.env` file in the project directory with the following content:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_GROUP_ID=your_group_chat_id_here
TIMEZONE=Your/Timezone
```

Replace the placeholder values with your actual bot token, group chat ID, and timezone.

8. Generate the token for Google Calendar API:

```
python generate_token.py
```

Follow the prompts to authorize the application.

## Usage

### Running the Script Manually

To run the script manually:

```
python main.py
```

This will create a Google Meet link and send it to the specified Telegram group.

### Setting Up Automatic Execution

Create a bash script, and run the script base on the cron
