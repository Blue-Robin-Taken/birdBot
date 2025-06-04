import discord
from discord.ext import commands
import os

class HypixelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guilds_ids=[os.environ['GUILD_ID']])
    async def hypixel_stats(self, context: discord.ApplicationContext):
        await context.respond('Hello!')


def setup(bot):
    bot.add_cog(HypixelCog(bot))
