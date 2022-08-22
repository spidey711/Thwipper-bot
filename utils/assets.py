# This file contains assets.

import random
import nextcord

from .functions import embed, CONTEXT, INTERACTION, Union
from .responses import connections
from .links import thumbnails


# Help Menu
help_embeds = []
DEFAULT_COLOR = nextcord.Color.from_rgb(223, 31, 45).value

def get_help_embeds(color: int, main: Union[CONTEXT, INTERACTION]):

    if isinstance(main, CONTEXT):
        author = main.author
        bot = main.bot
    else:
        author = main.user
        bot = main.client 

    return [
        embed(
            title="⚙️ Utility ⚙️",
            description="These are pretty standard bot features. Have a look :)",
            color=color,
            author=author,
            thumbnail=bot.user.avatar,
            fields={
                "`_ping`": "Get bot's latency.",
                "`_web`": "Web up those deleted messages before they get away. (Snipe)",
                "`_serverinfo`": "Get information about your server.",
                "`_pfp @user`": "See yours and your friends' profile picture.",
                "`_polls`": "Shows a guide on how to do polls.",
                "`/dt timezone`": "Gives date and time of mentioned timezone.",
                "`/calendar year month`": "See the days and their dates of mentioned month.",
            }
        ),
        embed(
            title="🌎 Internet 🌎",
            description="Get info about movies, see memes etc.",
            color=color,
            author=author,
            thumbnail=thumbnails[0],
            fields={
                "`_wiki topic`": "Get information about a topic/subject from wikipedia.",
                "`_g topic`": "See search result links of searched topic.",
                "`_imdb movie`": "View all details about a movie, including summary.",
                "`_reddit topic`": "Have a laugh at 'em funny memes from reddit.",
                "`/api chemistry element`": "Get base level info about all known elements."
            }
        ),
        embed(
            title="🎵 Music 🎵", 
            description="Thwipper's got its very own radio. **Spider-Punk Radio™**", 
            color=color, 
            author=author, 
            thumbnail=thumbnails[1],
            fields={
                "Voice Controls":"🔉 `_cn` to get the bot to join voice channel\n🔇 `_dc` to remove bot from voice channel",
                "Player Controls":"🎶 `_p name/index` to play songs\n▶ `_res` to resume a song\n⏸ `_pause` to pause a song\n⏹ `_st` to stop a song\n🔂 `_rep` to repeat song\n⏭ `_skip` to skip song\n⏮ `_prev` for previous song",
                "Queue Controls":"🔼 `_q` scroll queue `up`\n🔽 `_q` scroll queue `down`\n🔠 `_lyrics name` to display current song's lyrics\n*️⃣ `_songinfo` to get current song's info\n✅ `_q name` to add a song to the queue\n❌ `_rem index` to remove song from queue\n💥 `_cq` to clear queue"
            }
        ),
        embed(
            title="🔐 Cipher 🔐",
            description="You already know where this is going.",
            color=color,
            author=author,
            thumbnail=thumbnails[2],
            fields={
                "`_hush en text`": "'en' -> Encrypt message",
                "`_hush dec text`": "'dec' -> Decrypt message"
            }
        ),
    ]