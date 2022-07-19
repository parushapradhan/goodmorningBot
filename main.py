import os
import discord
import asyncio
from discord.ext import tasks,commands
from datetime import datetime, timedelta

intents = discord.Intents().all()

bot = commands.Bot(intents=intents, command_prefix='$')

channel_id= ''

def seconds_until_morning():
    now = datetime.now()
    target = (now + timedelta(days=1)).replace(hour=5, minute=30, second=0, microsecond=0)
    diff = (target - now).total_seconds()
    return diff
  
@tasks.loop(seconds = 1)
async def good_morning():
    await asyncio.sleep(seconds_until_morning())
    for guild in bot.guilds:
        guild = bot.get_guild(guild.id)
    for member in guild.members:
        if not member.bot:
            await member.send("Good Morning")

@bot.event
async def on_ready():
    if not good_morning.is_running():
        good_morning.start()
    
bot.run(os.environ['TOKEN'])  
