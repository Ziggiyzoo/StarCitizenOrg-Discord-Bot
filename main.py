"""
BRVNS Discord Bot
"""

import os

from src.brvns_client import BrvnsClient

# Main Method
if __name__ == "__main__":
    # Check for required environment variables
    if "TOKEN" not in os.environ:
        raise ValueError("No value for Environment Variable 'TOKEN' supplied. Exiting...")

    client: BrvnsClient = BrvnsClient()
    client.run(os.environ['TOKEN'])
