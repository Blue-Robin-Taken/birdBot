import discord
from discord.ext import commands
import os


class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def get_users_only(members: [discord.Member]):
        """
        Function to get the total members of the guild only, not bots.
        :param members: List of guild members
        :return: Integer
        """
        count = 0
        for member in members:
            if not member.bot:
                count += 1

        return count

    @discord.slash_command(guild_ids=[os.environ['GUILD_ID']])
    async def server_stats(self, context: discord.ApplicationContext):

        embed = discord.Embed(
            title='Server Stats',
            description=f'Server Members: {context.guild.member_count}\n '
                        f'Server Members (minus bots): {await self.get_users_only(context.guild.fetch_members())}',
            color=discord.Colour.random()
        )
        await context.respond(embed=embed)


def setup(bot):
    bot.add_cog(StatsCog(bot))
