# IMPORTS

import nextcord
import os
import regex
import utils.assets as assets
from dotenv import load_dotenv
from nextcord.ext import commands, tasks

load_dotenv()

# BASIC SETUP

prefixes = ["t!", "_"]
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot( 
    command_prefix=prefixes,
    intents=intents,
    case_insensitive=True,
)
DEFAULT_COLOR = nextcord.Color.from_rgb(223, 31, 45)

# RUN BOT

bot.run(os.getenv("token"))