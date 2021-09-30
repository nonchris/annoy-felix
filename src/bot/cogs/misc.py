from random import randint

import discord
from discord.ext import commands, tasks

from ..log_setup import logger
from ..utils import utils as ut


### @package misc
#
# Collection of miscellaneous helpers.
#

class Misc(commands.Cog):
    """
    Various useful Commands for everyone
    """

    def __init__(self, bot):
        self.bot = bot
        self.annoy_felix.start()

    @commands.command(name='ping', help="Check if Bot available")
    async def ping(self, ctx):
        """!
        ping to check if the bot is available

        @param ctx Context of the message
        """
        logger.info(f"ping: {round(self.bot.latency * 1000)}")

        await ctx.send(
            embed=ut.make_embed(
                name='Bot is available',
                value=f'`{round(self.bot.latency * 1000)}ms`')
        )

    @tasks.loop(seconds=5.0)
    async def annoy_felix(self):
        send = randint(0, 1)
        print(send)
        if send:
            guild: discord.Guild = self.bot.get_guild(884484070707437619)
            channel: discord.TextChannel = guild.get_channel(893061956683038721)
            print("Sending")
            await channel.send("Hallo Felix")



def setup(bot):
    bot.add_cog(Misc(bot))
