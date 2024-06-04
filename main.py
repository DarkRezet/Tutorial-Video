import disnake
from disnake.ext import commands
import random
token=""
prefix="."

client=commands.Bot(command_prefix=prefix, intents=disnake.Intents.all())
client.remove_command(help)

@client.event
async def on_ready():
    print("Online")

@client.slash_command(name="help", description="help command")
async def help(ctx):
    embed=disnake.Embed(
        title="help",
        description=f"{prefix}help",
        color=disnake.Color.random())
    await ctx.send(embed=embed)

client.run(token)