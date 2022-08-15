# IMPORTS

import nextcord
import os
import re
import utils.assets as assets
from utils.functions import embed
from dotenv import load_dotenv
from nextcord.ext import commands, tasks

# LOADING ENVIRONMENT
load_dotenv()

# VARIABLES
config_color: dict = {}

# CONFIGURING BOT
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
bot.color = lambda g: config_color.get(g.id, DEFAULT_COLOR)

# BOT VARIABLES
bot.config_color: dict = config_color

@bot.event
async def on_ready():
    print("READY")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if f"<@{bot.user.id}>" == message.content:
        embed = embed(
            title="Your friendly neighborhood spider-bot",
            description=f"Hi {message.author.name}!\nI am `Thwipper`. My name comes from the onomatopoeia of Spider-Man's Webshooters. Pretty slick, eh? I have lots of cool features that you may find interesting. Check them out with `_help` command. As always, more exciting features are always in the works. Stay tuned and have fun with them.\n_Excelsior!_",
            color=bot.color(message.guild),
            thumbnail=bot.user.avatar,
            fields={
                "Made by": "[Tamonud](https://www.github.com/spidey711)",
                "Source Code": "[Github Repo](https://www.github.com/spidey711/Thwipper-bot)"
            }
        )
        await message.reply(embed=embed)

for i in os.listdir("cogs/"):
    if i.endswith(".py"): bot.load_extension("cogs."+i[:-3])

# RUN BOT
bot.run(os.getenv("token"))