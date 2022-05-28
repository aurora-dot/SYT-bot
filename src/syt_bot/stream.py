from discord.ext import commands

from syt_bot.youtube import YTDLSource


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        if voice_channel and voice_channel.is_playing():
            voice_channel.pause()
            await ctx.send("Paused", delete_after=10)

    @commands.command()
    async def resume(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        if voice_channel and not voice_channel.is_playing():
            voice_channel.resume()
            await ctx.send("Resumed", delete_after=10)

    @commands.command()
    async def stop(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        if voice_channel and voice_channel.is_playing():
            voice_channel.stop()
            await ctx.send("Stopped", delete_after=10)

    @commands.command()
    async def stream(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error:  { e } ") if e else None
            )

        await ctx.send(f"Now playing:  { player.title } ", delete_after=10)

    @commands.command()
    async def volume(self, ctx, volume: int):
        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to  { volume } %", delete_after=10)

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
