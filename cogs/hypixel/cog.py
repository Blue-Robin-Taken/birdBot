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
        checkChars = string.ascii_letters + '_-'
        finalString = ''
        for char in inputString:
            if char in checkChars:
                finalString += char
        return finalString

    @discord.slash_command(guild_ids=[os.environ['GUILD_ID']])
    async def get_minecraft_uuid(self, context: discord.ApplicationContext, user: str):
        mojangRequest = requests.get(
            f"https://api.mojang.com/users/profiles/minecraft/{await self.sanitize_characters(user.strip())}")
        mojangRequestJSON = json.loads(mojangRequest.text)
        if 'id' not in mojangRequestJSON.keys():
            return await context.respond('User does not exist', ephemeral=True)
        mojangUserUUID = mojangRequestJSON['id']
        embed = discord.Embed(
            title=f'User: {mojangRequestJSON["name"]}',
            description=f"UUID: {mojangUserUUID}",
            color=discord.Color.random()
        )
        await context.respond(embed=embed)

    @discord.slash_command(guilds_ids=[os.environ['GUILD_ID']])
    async def hypixel_stats(self, context: discord.ApplicationContext, user: str):
        mojangUserUUID = await self.sanitize_characters(user)
        if not len(user) > 16:
            # fetch to get the user's UUID
            mojangRequest = requests.get(
                f"https://api.mojang.com/users/profiles/minecraft/{await self.sanitize_characters(user.strip())}")
            mojangRequestJSON = json.loads(mojangRequest.text)

            if 'id' not in mojangRequestJSON.keys():
                return await context.respond('User does not exist', ephemeral=True)

            mojangUserUUID = mojangRequestJSON['id']
        # Make the request to Hypixel
        hypixelRequest = requests.get(f"https://api.hypixel.net/v2/player?uuid={mojangUserUUID}", headers={'API-KEY': os.environ['HYPIXEL_API_KEY']})
        hypixelRequestJSON = json.loads(hypixelRequest.text)

        await context.respond(mojangUserUUID)


def setup(bot):
    bot.add_cog(HypixelCog(bot))
