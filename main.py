import discord
import os

bot = discord.Bot()
guildID = [os.environ['GUILD_ID']]


# --- Cog Implementation ---
cog_list = ['hypixel', 'stats']

for cog in cog_list:
    bot.load_extension('cogs.' + cog + '.cog')

# --- Event Handlers ---


@bot.listen()
async def on_ready():
    print('The bot has launched!')


bot.run(os.environ['TOKEN'])
