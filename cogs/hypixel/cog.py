import discord
from discord.ext import commands
import os
import requests
import json
import string

class HypixelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def sanitize_characters(inputString):
        checkChars = string.ascii_letters + '_'
        finalString = ''
        for char in inputString:
            if char in checkChars:
                finalString += char
        return finalString

    @discord.slash_command(guilds_ids=[os.environ['GUILD_ID']])
    async def hypixel_stats(self, context: discord.ApplicationContext, user: str):
        mojangUserUUID = ""
        if not len(user) > 16:
            # fetch to get the user's
            mojangUserUUID = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{await self.sanitize_characters(user.strip())}")
        await context.respond(mojangUserUUID.content)


def setup(bot):
    bot.add_cog(HypixelCog(bot))
