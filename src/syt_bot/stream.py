from discord.ext import commands

from syt_bot.youtube import YTDLSource


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()
        else:
            await ctx.send("Not in a voice channel")

    @commands.command()
    async def leave(self, ctx):
        connected = ctx.author.voice
        if connected:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Not in a voice channel")

    @commands.command()
    async def stream(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error:  { e } ") if e else None
            )

        await ctx.send(f"Now playing:  { player.title } ")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to  { volume } %")

    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
