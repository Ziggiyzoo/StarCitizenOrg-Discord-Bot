"""
BRVNS Discord Bot
"""
from os import environ
from src import BrvnsBot

# Main Method
if __name__ == "__main__":
    # Check for required environment variables
    if "TOKEN" not in environ or environ['TOKEN'] == "":
        raise ValueError("No value for Environment Variable 'TOKEN' supplied. Exiting...")

    token: str = environ['TOKEN']

    Bot: BrvnsBot = BrvnsBot(debug_guilds = [997138062381416589])
    Bot.run(token)
