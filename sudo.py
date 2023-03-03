from copy import copy

import discord
from discord.ext import commands

__version__ = "1.0.0"

class SudoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        hidden = True
    )
    @commands.is_owner()
    async def sudo(self, ctx, victim: discord.Member, *, command):
        """Take control."""
        new_message = copy(ctx.message)
        new_message.author = victim
        new_message.content = ctx.prefix + command
        await self.bot.process_commands(new_message)


def setup(bot):
    bot.add_cog(SudoCog(bot))