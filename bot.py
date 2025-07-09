import discord # type: ignore
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == 'oi':
        await message.channel.send('Olá!')

client.run(TOKEN)
