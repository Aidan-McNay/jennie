"""A starting app for the Jennie Slack Bot."""

import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.response import BoltResponse
from slack_bolt.adapter.socket_mode import SocketModeHandler
from typing import Callable, Dict, Optional, Any

# --------------------------------------------------------------------------
# Load environment variable secrets from .env
# --------------------------------------------------------------------------

load_dotenv()

# --------------------------------------------------------------------------
# Initialize the app with the bot token
# --------------------------------------------------------------------------

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# --------------------------------------------------------------------------
# Create a listener for messages with "hello"
# --------------------------------------------------------------------------


@app.message("Hello")
def message_hello(
    message: Dict[str, Any], say: Callable[..., Optional[BoltResponse]]
) -> None:
    """Send a message to the channel where the event was triggered."""
    say(f"Hey there, <@{message['user']}>!")


# --------------------------------------------------------------------------
# Start the app
# --------------------------------------------------------------------------

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
