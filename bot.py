#!/bin/python3


import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
# Getting Token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
botname = os.getenv('name')
# import Util
# from discord.ext import commands, tasks


client = commands.Bot(command_prefix="$")
status = cycle(["Lemme give you some nasty dares", "Slurpy truths eh ?", "Don't have the courage ?","You are too weak to play"])
# Bot's Ready
@client.event
async def on_ready():
    print("Bot is ready.")
    print(f"Logged in as: {client.user.name} ID: {client.user.id}")
    print(f"Online in Guilds:")
    for server in client.guilds:
        print(f"Guild name: {server.name} : {server.id}")

# Embeds 

embed_logout = discord.Embed(
            description=f"Logging Out, Now !",
            colour=discord.Color.from_rgb(224,47,74)
        )

embed_logout_error = discord.Embed(
            description=f"You do not have permission to run this command!",
            colour=discord.Color.from_rgb(224,47,74)
        )

embed_command_not_found_error = discord.Embed(
            description=f"No Arguments passed !/ any other error",
            colour=discord.Color.from_rgb(224,47,74)
        )


if __name__ == "__main__":
    #extensions = {"general","code","mail"}
    extensions = ["tnd"]
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f"Loaded Cog {extension} successfully")
        except Exception as error:
            print(f"Failed to load Cog {extension}. Reason: {error}")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(name="load")
@commands.has_role("ToD Admin")
async def load(ctx, extension):
    if extension == "":
        embed_valid_cog = discord.Embed(description = "Please enter a valid cog.",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_valid_cog)
    try:
        client.load_extension(extension)
        embed_load = discord.Embed(description = f"Loaded **{extension}**",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_load)
    except Exception as error:
        embed_load_error = discord.Embed(description = f"Failed to load cog **{extension}**. Reason: **{error}**",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_load_error)


@client.command(name="unload")
@commands.has_role("ToD Admin")
async def unload(ctx, extension):
    if extension == "":
        #await ctx.send(embed = discord.Embed(title = botname,description = "Please enter a valid cog", colour=discord.Color.from_rgb(183,142,255))
        embed_valid_cog = discord.Embed(description = "Please enter a valid cog.",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_valid_cog)
    try:
        client.unload_extension(extension)
        embed_unload = discord.Embed(description = f"Unloaded **{extension}**",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_unload)
    except Exception as error:
        embed_unload_error = discord.Embed(description = f"Failed to unload cog **{extension}**. Reason: **{error}**",colour=discord.Color.from_rgb(183,142,255))
        await ctx.send(embed=embed_unload_error)


@client.command(name="reload")
@commands.has_role("ToD Admin")
async def reload(ctx, extension):
    if extension == "":
        embed_valid_cog = discord.Embed(description = "Please enter a valid cog.",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_valid_cog)
    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        embed_reload = discord.Embed(description = f"Reloaded **{extension}**",colour=discord.Color.from_rgb(224,47,74))
        await ctx.send(embed=embed_reload)
    except Exception as error:
        embed_reload_error = discord.Embed(description = f"Failed to reload cog **{extension}**. Reason: **{error}**",colour=discord.Color.from_rgb(183,142,255))
        await ctx.send(embed=embed_reload_error)
@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(embed=embed_logout_error)
    else:
        await ctx.send(embed=embed_command_not_found_error)


@client.command(name="logout")
@commands.has_role("ToD Admin")
async def logout(ctx):
    await ctx.send(embed=embed_logout)
    #await ctx.send("Ok, Logging Out")
    await client.logout()


@logout.error
async def logout_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(embed=embed_logout_error)
        #await ctx.send(f"You do not have permission to run this command!")
    else:
        raise error

client.run(TOKEN)