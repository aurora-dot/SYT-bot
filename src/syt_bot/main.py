import discord
from discord.ext import commands

from syt_bot.secrets import SECRETS
from syt_bot.stream import Music

discord.opus.load_opus(SECRETS.OPUS_PATH)
intents = discord.Intents.all()


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    description="Relatively simple music bot example",
    intents=intents,
)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.event
async def on_ready():
    print(f"Logged in as  { bot.user }  (ID:  { bot.user.id } )")
    print("------")


def main():
    bot.add_cog(Music(bot))
    bot.run(SECRETS.DISCORD_API_KEY)
