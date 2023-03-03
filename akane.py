import os
import discord
from threading import Thread
from itertools import cycle
from discord.ext import commands, tasks


Token = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)

HugUrl = "https://64.media.tumblr.com/7568b179761b5faf3ef747e8edfa2498/723bd3eaa6d71f7e-71/s540x810/3ac41c2d549ec6180156da8d5bb55f1be01fbf0d.gif"

a = True
status = cycle(['Use $wish for help', 'Use $Wish for help'])


@client.event
async def on_ready():
    keep_alive()
    change_status.start()
    print("Your bot is ready")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def hello(ctx):
    await ctx.send("Hello!")


@client.command()
async def hug(ctx, member: discord.Member = None):
    if member != None:
        await ctx.send(f"Hugged {member.mention} {HugUrl}")
    if member == None:
        await ctx.send(f"Hugged {ctx.author.mention} {HugUrl}")


@client.command()
async def wish(ctx):
    await ctx.send(f"Haii i'm Hanako-Kun, You can use the following commands to talk to me \n`$Hello` I'll say Hello to you \n`$Hug` I'll hug the User you @ and if you don't @ someone I'll hug you \n `Im currently Running in minimal functionality mode`")


client.run(Token)
# Hanakorun = Thread(target=client.run(Token))
# Hanakorun.start()
