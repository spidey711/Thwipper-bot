import random

from .functions import embed, CONTEXT, INTERACTION, Union
from .responses import connections

YDL_OP = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "128",
        }
    ],
}

help_embeds = []

def get_help_embeds(color: int, main: Union[CONTEXT, INTERACTION]):

    if isinstance(main, CONTEXT):
        author = main.author
        bot = main.bot
    else:
        author = main.user
        bot = main.client 

    return [
        embed(
            title="Music", 
            description="Thwipper's got its very own radio. **Spider-Punk Radio™**", 
            color=color, 
            author=author, 
            thumbnail=bot.user.avatar,
            fields={
                "Voice Controls":"🔉 `_cn` to get the bot to join voice channel\n🔇 `_dc` to remove bot from voice channel",
                "Player Controls":"🎶 `_p name/index` to play songs\n▶ `_res` to resume a song\n⏸ `_pause` to pause a song\n⏹ `_st` to stop a song\n🔂 `_rep` to repeat song\n⏭ `_skip` to skip song\n⏮ `_prev` for previous song",
                "Queue Controls":"🔼 `_q` scroll queue `up`\n🔽 `_q` scroll queue `down`\n🔠 `_lyrics name` to display current song's lyrics\n*️⃣ `_songinfo` to get current song's info\n✅ `_q name` to add a song to the queue\n❌ `_rem index` to remove song from queue\n💥 `_cq` to clear queue"
            },
            footer=random.choice(connections),
            image={
                
            }
        )
        
        
    ]
