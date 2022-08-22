# IMPORTS
import nextcord
import os

from utils.assets import DEFAULT_COLOR
from utils.functions import embed
from utils.Storage import Variables
from dotenv import load_dotenv
from nextcord.ext import commands, tasks

# LOADING ENVIRONMENT
load_dotenv()

# VARIABLES
var = Variables("storage")
if var.show_data() == {}:
    var.pass_all(
        config_color = {},
        queue_song = {}
    )
    var.save()


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
bot.remove_command("help") # remove auto gen help menu

# BOT VARIABLES
RAW_DATA = var.show_data()
bot.config_color: dict = RAW_DATA.get("config_color", {})
bot.queue_song: dict = RAW_DATA.get("queue_song", {})
bot.color = lambda g: bot.config_color.get(g.id, DEFAULT_COLOR)


@bot.event
async def on_ready():
    print("Thwipper is now online.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if f"<@{bot.user.id}>" == message.content:
        embed = embed(
            title="Your friendly serverhood spider-bot!",
            description=f"Hi {message.author.name}!\nI am **Thwipper**. My name comes from the onomatopoeia of Spider-Man's Webshooters. Pretty slick, eh? I have lots of cool features that you may find interesting. Check them out with `_help` command. As always, more exciting features are always in the works. Stay tuned and have fun with them.\n_Excelsior!_",
            color=bot.color(message.guild),
            thumbnail=bot.user.avatar,
            fields={
                "Made by": "[Tamonud](https://www.github.com/spidey711)",
                "Source Code": "[Github Repo](https://www.github.com/spidey711/Thwipper-bot)"
            }
        )
        await message.reply(embed=embed)

@tasks.loop(minutes=1)
async def loop():
    var.edit(
        config_color = bot.config_color,
        queue_song = bot.queue_song
    )
    var.save()

# LOAD COGS
for i in os.listdir("cogs/"):
    if i.endswith(".py"): 
        bot.load_extension("cogs."+i[:-3])

# RUN BOT
bot.run(os.getenv("token"))