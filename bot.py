import discord # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import asyncio

load_dotenv()
TOLKEN = os.getenv('TOLKEN')

BOT = discord.Client(intents=discord.Intents.all())

@BOT.event
async def on_ready():
    print(f'Bot conectado como {BOT.user}')

@BOT.event
async def on_message(message):
    if message.author.bot == BOT.user:
        return
    
    if message.content.lower() == 'oi':
        await message.channel.send(f"Oi, {message.author.display_name}!")


BOT.run(TOLKEN)
  
        