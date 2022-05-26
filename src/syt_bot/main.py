import discord

from syt_bot.secrets import SECRETS


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


def main():
    client = MyClient()
    client.run(SECRETS.DISCORD_API_KEY)
