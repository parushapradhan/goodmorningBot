import os
import discord
import asyncio
from discord.ext import tasks,commands
from datetime import datetime, timedelta

bot = commands.Bot(intents=discord.Intents.default(), command_prefix='$')

channel_id= ''

def seconds_until_morning():
    now = datetime.now()
    target = (now + timedelta(days=1)).replace(hour=5, minute=30, second=0, microsecond=0)
    diff = (target - now).total_seconds()
    return diff
  
@tasks.loop(seconds = 1)
async def good_morning():
    await asyncio.sleep(seconds_until_morning())
    channel = bot.get_channel(channel_id)
    await channel.send("Good Morrrning")
  
@bot.command()
async def start(ctx):
  global channel_id
  channel_id = ctx.channel.id
  await ctx.channel.send('Goodmorning messages will now be sent in this channel everyday at 5:30AM')
  if not good_morning.is_running():
    good_morning.start()
    

bot.run(os.environ['TOKEN'])  