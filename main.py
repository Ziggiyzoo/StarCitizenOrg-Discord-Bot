"""
BRVNS Discord Bot
"""

import os
import src.BrvnsClient as BrvnsClient

# Main Method
if __name__ == "__main__":
    client: BrvnsClient = BrvnsClient.BrvnsClient()

    client.run(os.environ['TOKEN'])
