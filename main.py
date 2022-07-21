"""
BRVNS Discord Bot
"""

from os import environ

from src.brvns_client_API import BrvnsClient

# Main Method
if __name__ == "__main__":
    # Check for required environment variables
    if "TOKEN" not in environ or environ['TOKEN'] == "":
        raise ValueError("No value for Environment Variable 'TOKEN' supplied. Exiting...")

    Client: BrvnsClient = BrvnsClient()
    Client.run(environ['TOKEN'])
