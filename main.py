import datetime
import os
import discord
from discord.ext import tasks,commands

bot = commands.Bot(intents=discord.Intents.default(), command_prefix='$')

setTime = datetime.time(hour=5, minute=30)
channel_id= ''

@tasks.loop(time=setTime)
async def goodMorning():
    channel = bot.get_channel(channel_id)
    await channel.send("Good Morrrning")
    
@bot.command()
async def start(ctx):
    global channel_id
    channel_id = ctx.channel.id
    if not goodMorning.is_running():
        goodMorning.start()
    await ctx.channel.send('Goodmorning messages at 5:30AM will now be sent in this channel')
    

bot.run(os.environ['TOKEN'])