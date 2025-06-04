import discord
import os

bot = discord.Bot()


@bot.listen()
async def on_ready():
    print('The bot has launched!')


bot.run(os.environ['TOKEN'])
