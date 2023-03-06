from copy import copy
import os
import discord
from flask import Flask
from threading import Thread
from itertools import cycle
from discord.ext import commands, tasks
import time
import praw
import urllib.request
import random
import asyncio

app = Flask('')


@app.route('/')
def main():
  return "Your Bot Is Ready"


def run():
  app.run(host="0.0.0.0", port=8000)
  print("Your server is on")


def keep_alive():
  server = Thread(target=run)
  server.start()


Token = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)

HugUrl = "https://64.media.tumblr.com/7568b179761b5faf3ef747e8edfa2498/723bd3eaa6d71f7e-71/s540x810/3ac41c2d549ec6180156da8d5bb55f1be01fbf0d.gif"

a = True
status = cycle(['Use $wish for help', 'Use $Wish for help'])


@bot.event
async def on_ready():
  keep_alive()
  change_status.start()
  print("Your bot is ready")


@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")


# @bot.command(hidden=True)
# @commands.is_owner()
# async def sudo(ctx, victim: discord.Member, *, command):
#   """Take control."""
#   new_message = copy(ctx.message)
#   new_message.author = victim
#   new_message.content = ctx.prefix + command
#   await bot.process_commands(new_message)



@bot.command()
async def hanakoimg(ctx):
  with open("list.txt", "r") as links:
    lines = links.readlines()
    img = []
    for l in lines:
      as_list = l.split(", ")
      img.append(as_list[0].replace("\n", ""))
  choice = random.choice(img)
  await ctx.send(choice)


@bot.command()
async def hug(ctx, member: discord.Member = None):
  with open("listhug.txt", "r") as links:
    lines = links.readlines()
    img = []
    for l in lines:
      as_list = l.split(", ")
      img.append(as_list[0].replace("\n", ""))
    choice = random.choice(img)
    if member != None:
      await ctx.send(f"Hugged {member.mention} {choice}")
    if member == None:
      await ctx.send(f"Hugged {ctx.author.mention} {choice}")


@bot.command()
async def lmgtfy(ctx, *, arg=None):
  if arg == None:
    await ctx.send(
      "https://letmegooglethat.com/?q=How+do+I+use+letmegooglethat.com")
  else:
    arg = arg.replace(' ', '+')
    await ctx.send("https://letmegooglethat.com/?q=" + arg)


@bot.command()
async def addlist(ctx, *, arg):
  if arg == None:
    await ctx.send("Thats not a proper arg")
  else:
    f = open("list.txt", "a")
    f.write(", " + "\n" + arg)
    f.close()
    await ctx.send(f"Added to list Thanks")


@bot.command()
async def addhug(ctx, *, arg):
  if arg == None:
    await ctx.send("Thats not a proper arg")
  else:
    f = open("listhug.txt", "a")
    f.write(", " + "\n" + arg)
    f.close()
    await ctx.send(f"Added to list Thanks")


@bot.command()
async def featurerequest(ctx, *, arg):
  if arg == None:
    await ctx.send("please add a feature that you want")
  else:
    f = open("ideas.txt", "a")
    f.write(arg + f" :{ctx.author.name}:" + "," + "\n")
    f.close()
    await ctx.send(f"Added to list Thanks")




@bot.command()
async def fr(ctx, *, arg):
  if arg == None:
    await ctx.send("please add a feature that you want")
  else:
    f = open("ideas.txt", "a")
    f.write(arg + f" :{ctx.author.name}:" + "," + "\n")
    f.close()
    await ctx.send(f"Added to list Thanks")


# str(list1).replace('[','').replace(']','')


@bot.command()
async def listfeatures(ctx):
  with open("ideas.txt", "r") as links:
    lines = links.readlines()
    img = []
    for l in lines:
      as_list = l.split(", ")
      img.append(as_list[0].replace("\n", ""))
      msg = str(img).replace('[', '').replace(']',
                                              '').replace("'",
                                                          '').replace(',', '')
      await ctx.send(f"{msg}")


@bot.command()
async def shrek(ctx):
  await ctx.send(
    "https://media.discordapp.net/attachments/922701318483746816/1074618569800810566/2011-shrek-movie.gif"
  )


@bot.command()
async def wish(ctx):
  embed = discord.Embed(
    title="Wish Menu",
    description=
    "Haii i'm Hanako-Kun, You can use the following commands to talk to me \n`$Hello` I'll say Hello to you \n`$Hug` I'll hug the User you @ and if you don't @ someone I'll hug you\n`$lmgtfy` Hanako passive-aggressively googles the sentence you type after it\n `$hanakoimg` picks a random image of hanako from a list\n `$addlist` add links to the list that hanako can use\n `$featurerequest` add a feature request to the list that may get added\n `$listfeatures` lists the features in the list made by `featurerequest`\n `$addhug` add links to the hug list that hanako can use (I did this because this message from one of my discord\n Click my name for invite)",
    color=0xFF5733)
  embed.set_image(
    url=
    "https://lh3.googleusercontent.com/u/0/drive-viewer/AAOQEOS5k2SEEbnZp3QP7EbdFG3ayMnsbJqqQ_RHIRsWuzDzfmXDmgESxfkEatmpNgyY9WuqOwIC4-EpyKqKdDUK-oyMosKT1Q=w1325-h627"
  )
  embed.set_author(
    name="Hanako",
    url="https://top.gg/bot/916238736977694760",
    icon_url=
    "https://cdn.discordapp.com/avatars/916238736977694760/cf7ab98087e1547a56870a9edb43db5d.webp?size=80"
  )
  embed.set_footer(
    text="Information requested by: {}".format(ctx.author.display_name))
  await ctx.send(embed=embed)


async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      # cut off the .py from the file name
      print("loaded cogs")
      await bot.load_extension(f"cogs.{filename[:-3]}")


async def main2():
  async with bot:
    await load_extensions()
    await bot.start(Token)


asyncio.run(main2())
