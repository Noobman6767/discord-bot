import os
import discord
from discord.ext import tasks
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ROLE_PING = "<@&1503410703879504013>"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

test_sent = False

@client.event
async def on_ready():
    global test_sent
    print(f"Logged in as {client.user}")
    
    if not test_sent:
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="Bot Test Message",
                description="Bot is online and working! ✅",
                color=discord.Color.green()
            )
            await channel.send(content=ROLE_PING, embed=embed)
            test_sent = True
    
    if not daily_reminder.is_running():
        daily_reminder.start()

@tasks.loop(minutes=1)
async def daily_reminder():
    now = datetime.now(ZoneInfo("Europe/Vienna"))
    if now.hour == 18 and now.minute == 37:
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="Daily Access Reminder",
                description="It's high time to do your access! 🙂",
                color=discord.Color.blue()
            )
            embed.set_footer(text="Automated Reminder")
            await channel.send(
                content=ROLE_PING,
                embed=embed
            )

client.run(TOKEN)
