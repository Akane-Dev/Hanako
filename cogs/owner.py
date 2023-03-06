import discord
from discord.ext import commands
import time

__version__ = "1.0.0"


class Owner(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    print("test")

  @commands.command(hidden=True)
  @commands.is_owner()
  async def build(self, ctx):
    await ctx.send("Building")
    time.sleep(10)
    await ctx.send("Built")
    
    


async def setup(bot):
    await bot.add_cog(Owner(bot))
