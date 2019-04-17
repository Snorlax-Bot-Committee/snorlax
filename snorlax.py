import discord
from discord.ext import commands
import random

# create config.py file with bot token in base directory and import.
import config

description = '''Snorlax Bot'''
bot = commands.Bot(command_prefix='%', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ','.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.run(config.token)
