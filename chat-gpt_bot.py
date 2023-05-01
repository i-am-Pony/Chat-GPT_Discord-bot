import os
import discord
from dotenv import load_dotenv
import openai
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search(r'[a-zA-Z0-9]', message.content):
        response = openai.Completion.create(
            engine="davinci",
            prompt=message.content,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        await message.channel.send(response.choices[0].text)
        
client.run(TOKEN)
