import nextcord
import os
import regex
import utils.assets as assets

from dotenv import load_dotenv
from nextcord.ext import commands, tasks

load_dotenv()

config_color: dict = {}

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
bot.color = lambda g: config_color.get(g.id, DEFAULT_COLOR.id)

bot.run(os.getenv("token"))