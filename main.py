"""
BRVNS Discord Bot
"""

from os import environ

from src.brvns_client_API import BrvnsBot

# Main Method
if __name__ == "__main__":
    # Check for required environment variables
    if "TOKEN" not in environ or environ['TOKEN'] == "":
        raise ValueError("No value for Environment Variable 'TOKEN' supplied. Exiting...")

    Bot: BrvnsBot = BrvnsBot()
    Bot.run(environ['TOKEN'])
