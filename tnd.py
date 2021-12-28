import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
# Getting Token from .env file
load_dotenv()
filepath = os.getenv('truthfile')
class tnd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.players = []

    # Commands
    # ---------------------------------------------------PING----------------------------------------------
    @commands.command(aliases=['speed','connection'])
    async def ping(self, ctx):
        embed1 = discord.Embed(
            description=f":eyes: {round(self.client.latency * 1000)} ms",
            colour=discord.Color.from_rgb(183,142,255)
        )
        await ctx.send(embed=embed1)
    # ---------------------------------------------------FUN---------------------------------------------
    @commands.command(aliases=['abhi'])
    async def abhinav(self, ctx):
        await ctx.send(":eyes:")

    @commands.command()
    async def priyanshu(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/889120191617839135.gif?size=80")

    @commands.command()
    async def nastymf(self, ctx):
        await ctx.send("https://tenor.com/view/your-mom-humping-gif-14958931")
    # --------------------------------------------------TND-----------------------------------------------
    @commands.command()
    async def t(self, ctx):
        if self.players == []:
            await ctx.send("Game not started yet, type `.start` to start")
        else:
            with open(filepath, 'r') as f:
                lines = f.readlines()
            f.close()
            await ctx.send(random.choice(lines))

    @commands.command()
    async def start(self, ctx):
        await ctx.send("**Game has Started**, type `.enroll` to enroll into the game.")

    @commands.command()
    async def enroll(self, ctx):
        self.players.append(ctx.author.id)
        await ctx.send(f"{ctx.author.mention} got enrolled in the player's list")

    @commands.command()
    async def players(self, ctx):
        name = []
        for player in self.players:
            await ctx.send(player)
            name = client.get_member(id)
        await ctx.send(name)

    @commands.command()
    async def end(self, ctx):
        self.players = []
        await ctx.send("**Game Finished**")

        
def setup(client):
    client.add_cog(tnd(client))