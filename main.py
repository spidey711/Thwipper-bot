import discord
from discord.utils import get
from discord.ext import commands, tasks
import os
import sys
import pytz
import json
import random
import asyncio
import calendar
import datetime
import regex
import ffmpeg
import requests
import youtube_dl 
import urllib.request
from googlesearch import search
import mysql.connector as ms

# SETUP
bot = commands.Bot(command_prefix="t!")
intents = discord.Intents().all()
client = discord.Client(intents=intents)
# MUSIC
queue = {}
current = {}
FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
ydl_op = {'format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'96',}],}
# FACTS
facts_list = []
# Utility
num_req = 1
dev_users = []
# MEMES
meme_links = []
pinterest = ["https://in.pinterest.com/greenlanter5424/funny-superheroes-memes/","https://in.pinterest.com/nevaehgracesmom/superhero-memes/","https://in.pinterest.com/alexevitts98/superhero-funny/"]
# SQL
file = open("../env.txt","r")
txt_from_file = str(file.read())
print(txt_from_file)
start_password = txt_from_file.find("MySQL=") + len("MySQL=")
end_password = txt_from_file.find('"',start_password + 3) + 1
mysql_password = str(eval(txt_from_file[start_password:end_password]))
conn = ms.connect(host="localhost", user="root", passwd=mysql_password, database="discord")
cursor = conn.cursor()
# EXTRAS
url_date_time = "https://news.mit.edu/sites/default/files/images/202012/MIT-Time-Series-01-press.jpg"
url_thumbnails = ["https://i.pinimg.com/236x/f4/7d/1b/f47d1b34c2988f10a33f77c33e966d4c.jpg","https://i.pinimg.com/236x/4b/5e/bf/4b5ebfaba10beb08d3cae0a4ed684bdb.jpg","https://i.pinimg.com/236x/87/df/c7/87dfc7f867d4afff7c73923664a560af.jpg","https://i.pinimg.com/236x/b4/79/69/b47969fdf761ee63bf60adfdf7ba6554.jpg","https://i.pinimg.com/236x/48/0f/17/480f17eaaf087d44e540ee0a2d512297.jpg","https://i.pinimg.com/236x/4f/ab/0e/4fab0e67c4ba300f03bb5f03421ea7db.jpg","https://i.pinimg.com/236x/f6/06/ef/f606efe1e45c96ee6585cadebc6c8f74.jpg","https://c4.wallpaperflare.com/wallpaper/42/823/767/spiderman-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/517/160/840/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/107/848/913/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://wallpapercave.com/wp/AVIUso6.jpg","https://wallpapercave.com/wp/n9L3kJf.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-man-miles-morales-minimal-art-4k-43.jpg","https://images.hdqwalls.com/wallpapers/thumb/northern-spider-5k-f3.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-and-deadpool-4k-ys.jpg","https://images.hdqwalls.com/wallpapers/thumb/spiderman-into-the-spider-verse-y7.jpg","https://wallpapercave.com/wp/wp2018132.png","https://wallpapercave.com/wp/wp2018145.jpg","https://wallpapercave.com/wp/wp2018203.jpg","https://images3.alphacoders.com/593/thumbbig-593562.webp","https://images6.alphacoders.com/107/thumbbig-1071152.webp","https://images6.alphacoders.com/107/thumbbig-1070974.webp","https://i.pinimg.com/236x/38/a4/f6/38a4f62d74d7aeb2ae2396c991fcde52.jpg","https://i.pinimg.com/236x/ed/76/cc/ed76cc8bfe41347d979c93e23fbe51a0.jpg","https://i.pinimg.com/236x/91/87/2d/91872d5c92e8339036106bc832656a49.jpg","https://i.pinimg.com/236x/e3/94/05/e39405072916bb996caee3a4045f573a.jpg","https://i.pinimg.com/236x/36/2c/42/362c4298860d79a4b49acd9370cabe04.jpg","https://i.pinimg.com/236x/cf/3c/f4/cf3cf4ef7239868b1abc243168c41647.jpg","https://i.pinimg.com/236x/b1/3e/e7/b13ee7a8a8d72fbe39153569b5618c21.jpg"]
url_author_sql = "https://miro.medium.com/max/361/1*WzqoTtRUpmJR26dzlKdIwg.png"
url_author_music = "https://i.pinimg.com/236x/7f/d2/b8/7fd2b8ebf56ad7ad5587de70c80bcf88.jpg"
url_author_python = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png"

def youtube_download(ctx,url):
    if True:
        with youtube_dl.YoutubeDL(ydl_op) as ydl:
            URL = ydl.extract_info(url, download=False)['formats'][0]['url']
    return URL

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    # FACTS
    global facts_list
    b = requests.get("https://www.thefactsite.com/1000-interesting-facts/").content.decode().replace("<i>","*").replace("</i>","*").replace("&#8220;",'"').replace("&#8221;",'"').replace("&#8217;","'")
    stop = 0
    for i in range(0,117):
        n1 = b.find('<p class="list">',stop) + len('<p class="list">')
        n2 = b.find("</p>",stop)
        stop = n2 + len("</p>")
        output = ""
        if not b[n1:n2]:
            continue
        else:
            output = b[n1:n2]
            facts_list += [output]    
    # MEMES
    global meme_links
    raw = requests.get(random.choice(pinterest))
    html_content = raw.content.decode()
    stop = 0
    for i in range(0,500):
        a = html_content.find("GrowthUnauthPinImage__Image",stop)
        b = html_content.find('src="',a) + len('src="')
        c = html_content.find('" ',b)
        stop = c
        if i == 0:
            continue
        link = html_content[b:c]
        if link.find("</div>") != -1 or link.find("<html") != -1:
            continue
        meme_links += [link]
    # UPDATION
    @tasks.loop(seconds=5.0)
    async def updation():
        # dev_users
        global cursor
        operation_dev = "SELECT * FROM dev_users"
        cursor.execute(operation_dev)
        devs = cursor.fetchall()
        for dev in devs:
            if dev not in dev_users:
                dev_users.append(dev)
            else:
                continue
        # music queue 
        global queue
        operation_queue = "SELECT * FROM music_queue"
        cursor.execute(operation_queue)         
        items = cursor.fetchall()
        for item in items:
            if item not in queue:
                queue[item] = item[2]
            else:
                continue
        # sql table 
        global conn
        conn.commit()
    updation.start()

# //////////////////////////////////// SPECIAL ACCESS /////////////////////////////////////////

@bot.command(aliases=["allow","alw"])
async def allow_access(ctx, member:discord.Member):
    global url_author_python
    global cursor
    if ctx.author.id == 622497106657148939:
        cursor.execute("INSERT INTO dev_users(id)values({})".format(str(member.id)))
        embed = discord.Embed(description="{} has been allowed access".format(member), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=discord.Color.from_rgb(70, 96, 253))


@bot.command(aliases=["restrict","rstr"])
async def remove_access(ctx, member:discord.Member):
    global url_author_python
    global cursor
    if ctx.author.id == 622497106657148939:    
        cursor.execute("DELETE FROM dev_users WHERE id={}".format(member.id))    
        embed = discord.Embed(description="{} is now restricted".format(str(member.display_name)), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=discord.Color.from_rgb(70, 96, 253))    


@bot.command(aliases=["t"])
async def python_shell(ctx, *, expression):
    if ctx.author.id in dev_users:
        try:
            embed_acc = discord.Embed(title=str(expression), description=str(eval(expression)), color=discord.Color.from_rgb(70, 96, 253))
            embed_acc.set_author(name="Python Shell", icon_url=url_author_python)
            await ctx.send(embed=embed_acc)
        except Exception as e:
            embed_err = discord.Embed(title="𝗘𝗥𝗥𝗢𝗥", description=str(e), color=discord.Color.from_rgb(70, 96, 253))
            embed_err.set_author(name="Python Shell", icon_url=url_author_python)
            await ctx.send(embed=embed_err)
    else:
        embed_dc = discord.Embed(title="Access Denied", color=discord.Color.from_rgb(70, 96, 253))
        embed_dc.set_author(name="Python Shell",icon_url=url_author_python)
        await ctx.send(embed=embed_dc)
        

@bot.command()
async def clear(ctx, text, num=10000000000000):
    if ctx.author.id in dev_users:
        await ctx.channel.purge(limit=1)
        if str(text) == "OK":
            await ctx.channel.purge(limit=num)
        else:
            await ctx.send("Incorrect Password")
    else:
        await ctx.send("Access Denied")
    

@bot.command(aliases=["exit"])
async def stop_program(ctx):
    msgs = ["Bye {}!".format(ctx.author.name), "See ya {}!".format(ctx.author.name), "Till next time {} ;)".format(ctx.author.name)]
    if ctx.author.id == 622497106657148939:
        await ctx.send(random.choice(msgs))
        exit()
    else:
       await ctx.send("Access Denied")

#///////////////////////////////////// STANDARD //////////////////////////////////////////////

@bot.command(aliases=['hello', 'hi', 'hey', 'hey there', 'salut',"kon'nichiwa","hola","aloha"])
async def greet_bot(ctx):
    greetings = ["Hey {}!".format(ctx.author.name), "Hi {}!".format(ctx.author.name), "How's it going {}?".format(ctx.author.name), "What can I do for you {}?".format(ctx.author.name), "What's up {}?".format(ctx.author.name), "Hello {}!".format(ctx.author.name)]
    await ctx.send(random.choice(greetings))


@bot.command(aliases=['h'])
async def embed_help(ctx):
    global url_thumbnails
    embed = discord.Embed(title="🕸𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗠𝗲𝗻𝘂🕸",
                        description="Prefix => `t!`",
                        color=discord.Color.from_rgb(70, 96, 253))
    embed.add_field(name="𝗦𝘁𝗮𝗻𝗱𝗮𝗿𝗱",value="hello to greet bot\nh to get this embed", inline=False)
    embed.add_field(name="𝗨𝘁𝗶𝗹𝗶𝘁𝘆", value="ping to get user latency", inline=False)
    embed.add_field(name="𝗗𝗮𝘁𝗲 & 𝗧𝗶𝗺𝗲", value="dt to get IST date and time\ncal.m <year, month(in number)> to get calendar", inline=False)
    embed.add_field(name="𝗠𝘆𝗦𝗤𝗟", value="; <query> to use SQL Shell", inline=False)
    embed.add_field(name="𝗜𝗻𝘁𝗲𝗿𝗻𝗲𝘁",value="g <topic> to google\nfact to get an interesting fact\nmeme to get superhero memes",inline=False)
    embed.add_field(name="𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹",value="cn to get the bot to join voice channel\ndc to remove bot from voice channel",inline=False)
    embed.add_field(name="𝗣𝗹𝗮𝘆𝗲𝗿",value="p <name> or <index> to play songs\nres to resume a song\npause to pause a song\nst to stop a song", inline=False)
    embed.add_field(name="𝗤𝘂𝗲𝘂𝗲",value="q <name> to add a song to the queue\nrem <index> to remove a song\nv to view the queue\ncq to clear queue", inline=False)
    embed.set_thumbnail(url=random.choice(url_thumbnails))
    embed.set_footer(text="New Features Coming Soon! [🛠]\n1)Autoplay  2)Next  3)Previous  4)Loop Queue  5)Repeat Song  6)Remove  7)Wikipedia")
    await ctx.send(embed=embed)

# //////////////////////////////////// INTERNET //////////////////////////////////////////////

@bot.command(aliases=['g'])
async def browse(ctx, *, thing_to_search):
    results = " "
    for result in search(thing_to_search, tld='com', lang='en', safe='off', num=10, start=0,stop=10, pause=2.0):
        results += result + "\n\n"
    await ctx.send(results)


@bot.command(aliases=["fact"])
async def get_fact(ctx):
    try:
        await ctx.send(embed=discord.Embed(description=random.choice(facts_list), color=discord.Color.from_rgb(70, 96, 253)))
    except TypeError as te:
        await ctx.send(embed=discord.Embed(description=str(te), color=discord.Color.from_rgb(70, 96, 253)))
    

@bot.command(aliases=["meme"])
async def get_meme(ctx):
    await ctx.send(random.choice(meme_links))

#///////////////////////////////////// UTILITY ///////////////////////////////////////////////

@bot.command(aliases=["ping"])
async def get_ping(ctx):
    await ctx.send(embed=discord.Embed(description="𝙇𝙖𝙩𝙚𝙣𝙘𝙮 : {} ms".format(round(bot.latency * 1000)), color=discord.Color.from_rgb(70, 96, 253)))

# /////////////////////////////////////// DATE & TIME /////////////////////////////////////////

@bot.command(aliases=["dt"])
async def date_time_ist(ctx):
    tzinfo = pytz.timezone("Asia/Kolkata")
    dateTime = datetime.datetime.now(tz=tzinfo)
    embed = discord.Embed(color=discord.Color.from_rgb(70, 96, 253))
    embed.add_field(name='Date', value="%s/%s/%s" % (dateTime.day, dateTime.month, dateTime.year), inline=False)
    embed.add_field(name='Time', value="%s:%s:%s" % (dateTime.hour, dateTime.minute, dateTime.second), inline=False)
    embed.set_thumbnail(url=url_date_time)
    await ctx.send(embed=embed)   


@bot.command(aliases=["cal.m"])
async def get_calendar(ctx, year, month):
    global url_date_time
    try:
        embed = discord.Embed(description="```{}```".format(calendar.month(int(year), int(month))), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name='𝗖𝗮𝗹𝗲𝗻𝗱𝗮𝗿', icon_url=url_date_time)
        await ctx.send(embed=embed)
    except IndexError:
        embed = discord.Embed(description="{}, this month doesn't exist [📆]".format(ctx.author.name), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name='𝗖𝗮𝗹𝗲𝗻𝗱𝗮𝗿', icon_url=url_date_time)
        await ctx.send(embed=embed)

#///////////////////////////////////// STORAGE(SQL SHELL) ////////////////////////////////////

@bot.command(aliases=[";"])
async def sql_shell(ctx, *, expression):
    global cursor
    try:
        output = ""
        cursor.execute(expression)
        for item in cursor.fetchall():
            output += str(item) + "\n"
        conn.commit()
        embed = discord.Embed(title=str(expression), description=str(output), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name="MySQL Shell", icon_url=url_author_sql)   
        await ctx.send(embed=embed)
    except Exception as e:
        embed_err = discord.Embed(title="ERROR", description=str(e), color=discord.Color.from_rgb(70, 96, 253))
        embed_err.set_author(name="MySQL Shell", icon_url=url_author_sql)   
        await ctx.send(embed=embed_err)

#///////////////////////////////////////// MUSIC /////////////////////////////////////////////

@bot.command(aliases=["cn","connect"])
async def join_vc(ctx):
    try:
        if not ctx.message.author.voice:
            embed = discord.Embed(description="{}, connect to a voice channel first [🔊]".format(ctx.author.name), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name='Voice', icon_url=url_author_music)
            await ctx.send(embed=embed)
        else:    
            channel = ctx.message.author.voice.channel
            await channel.connect()
            message = await ctx.send("Connected")
            await asyncio.sleep(2)
            await message.edit(content="Use `t!p <name> or <index>` to play songs [🎸]") 
    except Exception as e:
        embed = discord.Embed(description=str(e) + " [✅]", color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name='Voice', icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["dc","disconnect"])
async def leave_vc(ctx):
    voice_client = ctx.message.guild.voice_client
    try:
        if voice_client.is_connected():
            await voice_client.disconnect() 
            message = await ctx.send("Disconnected")
            await asyncio.sleep(2)
            await message.edit(content="See ya later [👋🏻]")
    except AttributeError:
        embed = discord.Embed(description="I am not connected to a voice channel [❗]", color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name='Voice', icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["queue","q"])
async def queue_song(ctx, *, name):
    global cursor
    name = name.replace(" ", "+")
    htm = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + name) # the 11 lettered string which is like an ID for videos is stored inside the variable video
    video = regex.findall(r"watch\?v=(\S{11})", htm.read().decode())
    url = "https://www.youtube.com/watch?v=" + video[0] # we got the html code of the full search page
    htm_code = str(urllib.request.urlopen(url).read().decode()) # htm_code contains the entire HTML code of the web page where we see the video
    starting = htm_code.find("<title>") + len("<title>") # now we use .find method to find the title of the vid which is in between <title></title> tags
    ending = htm_code.find("</title>")        
    name_of_the_song = htm_code[starting:ending].replace("&#39;","'").replace("&amp;","&") # here we replace uncessary things like tags because we only want the title
    cursor.execute("INSERT INTO music_queue(song_name, song_url, server)VALUES('{name}','{url}','{serverid}')".format(name=name_of_the_song, url=url, serverid=str(ctx.guild.id)))
    embed = discord.Embed(description="{}".format(name_of_the_song).replace(" - YouTube", " "), color=discord.Color.from_rgb(70, 96, 253))
    embed.set_author(name="Song added", icon_url=url_author_music)
    await ctx.send(embed=embed)


@bot.command(aliases=["play","p"])
async def play_music(ctx, *, char):
    global ydl_op
    global queue
    global cursor
    global FFMPEG_OPTS
    # Web Scrape
    char = char.replace(" ","+")
    htm = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + char)
    video = regex.findall(r"watch\?v=(\S{11})", htm.read().decode())
    url = "https://www.youtube.com/watch?v=" + video[0]
    htm_code = str(urllib.request.urlopen(url).read().decode())
    starting = htm_code.find("<title>") + len("<title>")
    ending = htm_code.find("</title>")
    name_of_the_song = htm_code[starting:ending].replace("&#39;","'").replace("&amp;","&").replace("&quot;", " ")
    # Personalized Queue Init
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall() 
    URL_QUEUE = youtube_download(ctx, server_queue[int(char)][1])
    # Setup for playing music
    URL_PLAY = youtube_download(ctx, url)
    voice = get(bot.voice_clients, guild=ctx.guild)
    playing = ctx.voice_client.is_playing()
    pause = ctx.voice_client.is_paused()
    if char.isnumeric() == True:
        if playing != True:
            embed = discord.Embed(description="{}".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="Now playing", icon_url=url_author_music)
            voice.play(discord.FFmpegPCMAudio(URL_QUEUE, **FFMPEG_OPTS))
            await ctx.send(embed=embed)
        else:
            voice.stop()
            embed = discord.Embed(description="{}".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="Now playing", icon_url=url_author_music)
            voice.play(discord.FFmpegPCMAudio(URL_QUEUE, **FFMPEG_OPTS))
            await ctx.send(embed=embed)
    else:
        if playing != True:
            embed = discord.Embed(description="{}".format(name_of_the_song).replace(" - YouTube", " "), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="Now playing", icon_url=url_author_music)
            voice.play(discord.FFmpegPCMAudio(source=URL_PLAY, executable=FFMPEG_OPTS))
            await ctx.send(embed=embed)
        else:
            voice.stop()
            embed = discord.Embed(description="{}".format(name_of_the_song).replace(" - YouTube", " "), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="Now playing", icon_url=url_author_music)
            voice.play(discord.FFmpegPCMAudio(URL_PLAY, executable=FFMPEG_OPTS))
            await ctx.send(embed=embed)


@bot.command(aliases=["view","v"])
async def view_queue(ctx):
    global queue
    global cursor
    global current
    operation_view = "SELECT song_name FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation_view)
    songs = cursor.fetchall()
    string = ""
    song_index = 0
    if len(songs) > 0:
        for song in songs:
            string += str(song_index) + ". " + str(song) + "\n"
            song_index += 1
        embed = discord.Embed(title="𝗤𝘂𝗲𝘂𝗲", description=string.replace(" - YouTube"," ").replace("('", " ").replace("',)"," "), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_thumbnail(url="https://i.pinimg.com/236x/10/06/35/100635a268123393a208b3e6efb5ec0d.jpg")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="No songs in queue [⭕]", color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name="𝗤𝘂𝗲𝘂𝗲", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["pause"])
async def pause_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    try:
        if playing == True:    
            voice_client.pause()
            message = await ctx.send("Song paused")
            await message.add_reaction("⏸")
        else:
            if pause == True:
                await ctx.send(embed=discord.Embed(description="Song is already paused [❗]", color=discord.Color.from_rgb(70, 96, 253)))
            else:
                embed = discord.Embed(description="No song playing currently [❗]", color=discord.Color.from_rgb(70, 96, 253))
                await ctx.send(embed=embed)
    except Exception as e: 
        embed = discord.Embed(description=str(e), color=discord.Color.from_rgb(70, 96, 253))
        embed.set_author(name="𝗘𝗥𝗥𝗢𝗥", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["resume","res"])
async def resume_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    try:
        if pause == True:
            voice_client.resume()
            message = await ctx.send("Song resumed")
            await message.add_reaction("▶")
        else:
            if playing == True:
                embed = discord.Embed(description="Song isn't paused [❗]\nUse `t!pause` to pause the song.", color=discord.Color.from_rgb(70, 96, 253))
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=discord.Embed(description="No song playing currently [❗]\nUse `t!p <name>  or <index>` to play a song.", color=discord.Color.from_rgb(70, 96, 253)))
    except Exception as e:
            embed = discord.Embed(description=str(e), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="𝗘𝗥𝗥𝗢𝗥", icon_url=url_author_music)
            await ctx.send(embed=embed)


@bot.command(aliases=["stop","st"])
async def stop_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    try:
        if playing == True or pause == True:    
            voice_client.stop()
            message = await ctx.send("Song stopped")
            await message.add_reaction("⏹")
        else:
            await ctx.send(embed=discord.Embed(description="Nothing is playing right now [❗]", color=discord.Color.from_rgb(70, 96, 253))
            )
    except Exception as e:
            embed = discord.Embed(description=str(e), color=discord.Color.from_rgb(70, 96, 253))
            embed.set_author(name="ERROR", icon_url=url_author_music)
            await ctx.send(embed=embed)


@bot.command(aliases=["clear_queue","cq"])
async def clear_song_queue(ctx):
    global queue
    global cursor
    if len(queue) > 0:
        operation_clear_song = "DELETE FROM music_queue WHERE server={}".format(ctx.guild.id)
        cursor.execute(operation_clear_song)
        queue.clear()
        message = await ctx.send("Queue Cleared")
        await message.add_reaction("✅")
    else:
        embed_empty = discord.Embed(description="Queue is already empty [⭕]", color=discord.Color.from_rgb(70, 96, 253))
        embed_empty.set_author(name="Hmm...", icon_url=url_author_music)
        await ctx.send(embed=embed_empty)

start_token = txt_from_file.find("token=") + len("token=")
end_token = txt_from_file.find('"',start_token + 3) + 1
bot.run(eval(txt_from_file[start_token:end_token]))