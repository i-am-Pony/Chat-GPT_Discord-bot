# Chat-GPT_Discord-bot
Add Chat-GPT to Your Discord Server! Use this super easy method to add Chat-GPT to your Discord server FAST!
Remember this is a WIP and I am trying to implement this myself as I write this, so you may want to wait until I have fully implemented, or ask someone with more years of experience with Python to help you in the meantime.


<FIRST:>
You will need to create a bot in your Discord server.

To add a bot to your Discord server, you can follow these steps:

Go to the Discord Developer Portal and create a new application: https://discord.com/developers/applications
Click on the "Bot" section in the left-hand menu and then click on "Add Bot."
Customize the bot's name and image as desired.
Copy the bot's token by clicking on the "Copy" button under the "TOKEN" section.
Invite the bot to your server by replacing "YOUR_CLIENT_ID" with your bot's client ID in the following URL: https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot
Choose the server you want to add the bot to and authorize it.
Once the bot is added to your server, you can interact with it by mentioning it in a text channel or sending it a direct message. Note that you will need to write some code or use an existing bot framework to program the bot to respond to specific commands or messages.


<SECOND>
  You will need to write some code to use, to program the bot created above, to interact with Chat-GPT. 
  
Here is a sample code snippet in Python using the discord.py library that you can use to program the bot to interact with Chat-GPT:

  
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
  
  
This script uses the discord.py library to create a bot that connects to Discord, and uses the OpenAI API to generate responses to messages that it receives in the chat.

To use this code, you will need to create a .env file in the same directory as the script, and add your Discord bot token and OpenAI API key to it like this:
  

DISCORD_TOKEN=<your Discord bot token>
DISCORD_GUILD=<your Discord guild name>
OPENAI_API_KEY=<your OpenAI API key>
  
  
  Once you have added your credentials to the .env file, you can run the script to start your bot. You will need to invite your bot to your Discord server using the client ID generated when you created your bot.

You do not need to refresh or restart anything each time you make changes to the code - you can just save the file and re-run it to see the changes take effect. However, keep in mind that any changes you make will only apply to new messages that the bot receives - it will not retroactively change its response to messages that it has already received.
  
  Good Luck and Happy Coding.
