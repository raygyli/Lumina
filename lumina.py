import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from discord_bot import LuminaBot

def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    intents.dm_messages = True
    intents.members = True

    lumina = LuminaBot(command_prefix='!', intents=intents)
    
    lumina.run(TOKEN)


if __name__ == "__main__":
    main()
