"""
BRVNS Discord Bot
"""

import os
from src.brvns_client import BrvnsClient

# Main Method
if __name__ == "__main__":
    client: BrvnsClient = BrvnsClient()

    client.run(os.environ['TOKEN'])
