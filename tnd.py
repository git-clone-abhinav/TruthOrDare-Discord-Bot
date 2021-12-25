import discord
from discord.ext import commands

class tnd(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    # ---------------------------------------------------PING----------------------------------------------
    @commands.command(aliases=['speed','connection'])
    async def ping(self, ctx):
        embed1 = discord.Embed(
            description=f":eyes: {round(self.client.latency * 1000)} ms",
            colour=discord.Color.from_rgb(183,142,255)
        )
        await ctx.send(embed=embed1)
    # -------------------------------------------------ABHINAV--------------------------------------------
    @commands.command(aliases=['abhi'])
    async def abhinav(self, ctx):
        await ctx.send(":eyes:")

    # --------------------------------------------------TND-----------------------------------------------
    @commands.command()
    async def tnd(self, ctx):
        message = "haalo ji haalo"
        await ctx.send(message)


def setup(client):
    client.add_cog(tnd(client))