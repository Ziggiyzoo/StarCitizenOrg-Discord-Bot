"""
BRVNS Discord Client Object
"""

from discord import Client


class BrvnsClient(Client):
    """
    BRVNS Discord Client
    """

    async def on_ready(self):
        """
        Run when a User logs in

        :raises TypeError
        """

        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        """
        Run when a message is received

        :param message: The message object
        :type message:
        :return:
        :rtype:
        """

        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
