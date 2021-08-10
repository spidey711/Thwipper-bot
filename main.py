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
prefixes = ["t!","_","thwip"]
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=[prefix for prefix in prefixes], intents=intents, case_insensitive=True)
color = discord.Color.blue()
deleted_messages = {}
# MUSIC
current = {}
FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
ydl_op = {'format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'128',}],}
# FACTS
facts_list = []
# WIT
plot_list = []
dialogue_list = []
# MEMES
pinterest = ["https://in.pinterest.com/joshuacgreenste/funny-superhero-memes/","https://in.pinterest.com/greenlanter5424/funny-superheroes-memes/","https://in.pinterest.com/comicnity/superhero-memes/"]
meme_links = []
# SQL
file = open("env.txt","r")
txt_from_file = str(file.read())
start_password = txt_from_file.find("MySQL=") + len("MySQL=")
end_password = txt_from_file.find('"',start_password + 3) + 1
mysql_password = str(eval(txt_from_file[start_password:end_password]))
conn = ms.connect(host="localhost", user="root", passwd=mysql_password, database="discord")
cursor = conn.cursor()
# EXTRAS
url_author_python = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png"
url_date_time = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKxv6EIh3VisynQX9TNkA7l15CvR0eJ8nWMA&usqp=CAU"
url_calendar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsb98d6ZOyxwxLUf1Y97yWFKW0Pz6JzuyBww&usqp=CAU"
url_thumbnails = ["https://i.pinimg.com/236x/31/fc/50/31fc5099e24775b613a69fa5bf4f8064.jpg","https://i.pinimg.com/236x/e5/f5/54/e5f55401dfb0588daaa0c3baad528ae8.jpg","https://i.pinimg.com/236x/be/80/cf/be80cf957b028e16083d534f3890cda1.jpg","https://i.pinimg.com/236x/02/6c/7d/026c7d47fd43ff30180fdc7c91e155c2.jpg","https://i.pinimg.com/236x/14/ca/dc/14cadcf0d437fe2d670bff20254e3422.jpg","https://i.pinimg.com/236x/3d/dd/ec/3dddecd82efb45026771dba7287aa010.jpg","https://i.pinimg.com/236x/4d/16/7e/4d167e9a51166d0ce955c4eac6b26d7c.jpg","https://i.pinimg.com/236x/46/56/8c/46568c65f50f4cd5dce76c1ea1833258.jpg","https://i.pinimg.com/236x/74/e6/d8/74e6d846301bd4e3722ed465240b894f.jpg","https://i.pinimg.com/236x/4f/ef/67/4fef67d2a553dba286ab311354370d28.jpg","https://i.pinimg.com/236x/f4/7d/1b/f47d1b34c2988f10a33f77c33e966d4c.jpg","https://i.pinimg.com/236x/4b/5e/bf/4b5ebfaba10beb08d3cae0a4ed684bdb.jpg","https://i.pinimg.com/236x/87/df/c7/87dfc7f867d4afff7c73923664a560af.jpg","https://i.pinimg.com/236x/b4/79/69/b47969fdf761ee63bf60adfdf7ba6554.jpg","https://i.pinimg.com/236x/48/0f/17/480f17eaaf087d44e540ee0a2d512297.jpg","https://i.pinimg.com/236x/4f/ab/0e/4fab0e67c4ba300f03bb5f03421ea7db.jpg","https://i.pinimg.com/236x/f6/06/ef/f606efe1e45c96ee6585cadebc6c8f74.jpg","https://c4.wallpaperflare.com/wallpaper/42/823/767/spiderman-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/517/160/840/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/107/848/913/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://wallpapercave.com/wp/AVIUso6.jpg","https://wallpapercave.com/wp/n9L3kJf.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-man-miles-morales-minimal-art-4k-43.jpg","https://images.hdqwalls.com/wallpapers/thumb/northern-spider-5k-f3.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-and-deadpool-4k-ys.jpg","https://images.hdqwalls.com/wallpapers/thumb/spiderman-into-the-spider-verse-y7.jpg","https://wallpapercave.com/wp/wp2018132.png","https://wallpapercave.com/wp/wp2018145.jpg","https://wallpapercave.com/wp/wp2018203.jpg","https://images3.alphacoders.com/593/thumbbig-593562.webp","https://images6.alphacoders.com/107/thumbbig-1071152.webp","https://images6.alphacoders.com/107/thumbbig-1070974.webp","https://i.pinimg.com/236x/38/a4/f6/38a4f62d74d7aeb2ae2396c991fcde52.jpg","https://i.pinimg.com/236x/ed/76/cc/ed76cc8bfe41347d979c93e23fbe51a0.jpg","https://i.pinimg.com/236x/91/87/2d/91872d5c92e8339036106bc832656a49.jpg","https://i.pinimg.com/236x/e3/94/05/e39405072916bb996caee3a4045f573a.jpg","https://i.pinimg.com/236x/36/2c/42/362c4298860d79a4b49acd9370cabe04.jpg","https://i.pinimg.com/236x/cf/3c/f4/cf3cf4ef7239868b1abc243168c41647.jpg","https://i.pinimg.com/236x/b1/3e/e7/b13ee7a8a8d72fbe39153569b5618c21.jpg","https://i.pinimg.com/236x/d9/ef/b8/d9efb89361f4a8d04f2e4e8d8d8067e8.jpg","https://i.pinimg.com/236x/d7/1c/9a/d71c9a5f09e61fcea6ffc3d61f7d5011.jpg","https://i.pinimg.com/236x/3b/cc/8c/3bcc8cde6be346db7c84eaa52e8f9072.jpg","https://i.pinimg.com/236x/ea/0c/ca/ea0ccaa55471689fda39043d80bc7a07.jpg","https://i.pinimg.com/236x/0a/7e/41/0a7e413a95d88ae13487a796d40237ef.jpg","https://i.pinimg.com/236x/d5/ea/83/d5ea830dee3385bfe9fa9871e3190b40.jpg","https://i.pinimg.com/236x/3d/d6/6c/3dd66c95df0b377767bf24e16d77b5ee.jpg"]
url_author_sql = "https://miro.medium.com/max/361/1*WzqoTtRUpmJR26dzlKdIwg.png"
url_author_music = "https://i.pinimg.com/originals/f9/33/3d/f9333dd53a0a35d08362004e17b75976.jpg"
url_author_queue = ["https://i.pinimg.com/236x/10/06/35/100635a268123393a208b3e6efb5ec0d.jpg","https://i.pinimg.com/236x/d8/a1/fc/d8a1fcbc9482a9ae7a9352620dd3e4ea.jpg"]

def youtube_download(ctx, url):
    if True:
        with youtube_dl.YoutubeDL(ydl_op) as ydl:
            URL = ydl.extract_info(url, download=False)['formats'][0]['url']
    return URL

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    stop = 0
    # STATUS
    activity = discord.Game(name="Spider-Man (2018)", type=3)
    await bot.change_presence(activity=activity)
    # WITS
    global plot_list
    x = requests.get("https://www.cbr.com/greatest-spider-man-stories/").content.decode().replace("<em>"," ").replace("</em>"," ")
    for i in range(0, 10000):
        a = x.find("<p>", stop)
        b = x.find("</p>", stop)
        stop = b + len("</p>")
        wits = ""
        if not x[a:b]:
            continue
        else:
            wits = x[a:b]
            plot_list += [wits.replace("<p>"," ")]
    # DIALOGUES
    global dialogue_list
    site = requests.get("https://geektrippers.com/spiderman-quotes/").content.decode().replace("<br>","\n").replace("<strong>"," ").replace("</strong>"," ").replace("<em>"," ").replace("</em>"," ").replace("&#8217;","'").replace("&#8221;",'"\n\r').replace("&#8230;","...").replace("&#8220;",'"').replace("&nbsp;"," ").replace("&#8211;","-").replace("&#8216;","'")
    for i in range(0, 1000):
        q = site.find('<p class="has-background" style="background-color:#dedfe0">', stop) + len('<p class="has-background style="background-color:#dedfe0">')
        w = site.find("</p>", stop)
        stop = w + len("</p>")
        dialogues = ""
        if not site[q:w]:
            continue
        else:
            dialogues = site[q:w]
            dialogue_list += [dialogues]
    # # FACTS
    global facts_list
    b = requests.get("https://www.thefactsite.com/1000-interesting-facts/").content.decode().replace("<i>","*").replace("</i>","*").replace("&#8220;",'"').replace("&#8221;",'"').replace("&#8217;","'")
    for i in range(0,117):
        n1 = b.find('<p class="list">', stop) + len('<p class="list">')
        n2 = b.find("</p>", stop)
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
    for i in range(0,500):
        a = html_content.find("GrowthUnauthPinImage__Image", stop)
        b = html_content.find('src="', a) + len('src="')
        c = html_content.find('" ', b)
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
        conn.commit()
    updation.start()

@bot.event
async def on_message_delete(message):
    if not message.channel.id in list(deleted_messages.keys()):
        deleted_messages[message.channel.id] = []
    deleted_messages[message.channel.id].append((str(message.author), message.content))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="announcements")
    embed = discord.Embed(title="We have a new member!", description="Welcome {}!".format(member.mention), color=color)
    embed.set_thumbnail(url="https://www.goodfon.com/download/welcome-home-welcome-home-de/1366x768/")
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="announcements")
    embed = discord.Embed(title="See ya!", description="{} has decided to leave the server".format(member.mention), color=color)
    embed.set_thumbnail(url="https://www.dreamstime.com/neon-sign-good-bye-speech-bubble-frame-dark-background-neon-sign-good-bye-speech-bubble-frame-dark-background-light-image151416182")
    await channel.send(embed=embed)

# //////////////////////////////////// SPECIAL ACCESS /////////////////////////////////////////

@bot.command(aliases=["allow","alw"])
async def allow_access(ctx, member:discord.Member):
    global cursor
    if ctx.author.id == 622497106657148939:
        cursor.execute("INSERT INTO dev_users(dev_id)values({})".format(str(member.id)))
        embed = discord.Embed(description="{} has been allowed access".format(member), color=color)
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=color)


@bot.command(aliases=["restrict","rstr"])
async def remove_access(ctx, member:discord.Member):
    global url_author_python
    global cursor
    if ctx.author.id == 622497106657148939:    
        cursor.execute("DELETE FROM dev_users WHERE dev_id={}".format(str(member.id)))    
        embed = discord.Embed(description="{} is now restricted".format(str(member)), color=color)
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=color)    
        

@bot.command()
async def clear(ctx, text, num=10000000000000):
    op_dev = "SELECT * FROM dev_users"
    cursor.execute(op_dev)
    dev_list = cursor.fetchall()
    if str(ctx.author.id) in str(dev_list) or ctx.author.id == 622497106657148939:
        await ctx.channel.purge(limit=1)
        if str(text) == "OK":
            await ctx.channel.purge(limit=num)
        else:
            await ctx.send("Incorrect Password")
    else:
        await ctx.send("Access Denied")
    

@bot.command(aliases=["exit"])
async def stop_program(ctx):
    global conn
    msgs = ["Bye {}!".format(ctx.author.name), "See ya {}!".format(ctx.author.name), "Till next time {}".format(ctx.author.name)]
    if ctx.author.id == 622497106657148939:
        await ctx.send(random.choice(msgs))
        conn.commit()
        exit()
    else:
       await ctx.send("Access Denied")

#///////////////////////////////////// STANDARD //////////////////////////////////////////////

@bot.command(aliases=['hello', 'hi', 'hey', 'hey there', 'salut',"kon'nichiwa","hola","aloha"])
async def greet_bot(ctx):
    greetings = ["Hey {}!".format(ctx.author.name), "Hi {}!".format(ctx.author.name), "How's it going {}?".format(ctx.author.name), "What can I do for you {}?".format(ctx.author.name), "What's up {}?".format(ctx.author.name), "Hello {}!".format(ctx.author.name)]
    await ctx.send(random.choice(greetings))


@bot.command(aliases=["about"])
async def thwipper_info(ctx):
    embed = discord.Embed(title="About", description="Hey there! My name is `THWIPPER`.\nI was made by Spider-Man to tend to people's needs on discord while he is out in the city protecting the innocent from harm.", color=color)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(text="Type _use for command menu", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(aliases=['use','h'])
async def embed_help(ctx):
    global url_thumbnails
    embed = discord.Embed(title="🕸𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗠𝗲𝗻𝘂🕸",
                        description="Prefix => `t!`or `_`",
                        color=color)
    embed.add_field(name="𝗦𝘁𝗮𝗻𝗱𝗮𝗿𝗱",value="hello to greet bot\nuse to get this embed\nwit to get a famous dialogue or plot\nabout to get more info about thwipper", inline=False)
    embed.add_field(name="𝗨𝘁𝗶𝗹𝗶𝘁𝘆", value="ping to get user latency\nserverinfo to get server's information\npfp to get user's profile picture\nsnipe to see deleted message", inline=False)
    embed.add_field(name="𝗗𝗮𝘁𝗲 & 𝗧𝗶𝗺𝗲", value="dt to get IST date and time\ncal.m <year, month(in number)> to get calendar", inline=False)
    embed.add_field(name="𝗦𝗵𝗲𝗹𝗹𝘀", value="; <query> to use SQL Shell\npy for python shell\npinfo to get use of that python function", inline=False)
    embed.add_field(name="𝗜𝗻𝘁𝗲𝗿𝗻𝗲𝘁",value="g <topic> to google\nfact to get an interesting fact (under works)\nmeme to get superhero memes",inline=False)
    embed.add_field(name="𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹",value="cn to get the bot to join voice channel\ndc to remove bot from voice channel",inline=False)
    embed.add_field(name="𝗣𝗹𝗮𝘆𝗲𝗿",value="p <name> or <index> to play songs\nres to resume a song\npause to pause a song\nst to stop a song", inline=False)
    embed.add_field(name="𝗤𝘂𝗲𝘂𝗲",value="q <name> to add a song to the queue\nauto ON/OFF to toggle autoplay\ncq to clear queue", inline=False)
    embed.set_thumbnail(url=random.choice(url_thumbnails))
    embed.set_footer(text="New Features Coming Soon! [🛠]\n1)Next  2)Previous  3)Loop Queue  4)Repeat Song  5)Remove  6)Wikipedia")
    await ctx.send(embed=embed)


@bot.command(aliases=["wit"])
async def get_wit(ctx):
    global plot_list
    global dialogue_list
    wit_list = []
    for plot in plot_list:
        for dialogue in dialogue_list:
            wit_list.append(plot)
            wit_list.append(dialogue)
    titles = ["Oh man, I remember this one!","Here you go...","I gotta say, this still holds up today..."]
    footers = ["Man, this is killer material!","Now this is what I call a good wit!","Oh boy, this is one of my favorites!"]
    embed = discord.Embed(title=random.choice(titles), description=random.choice(wit_list), color=color)
    embed.set_thumbnail(url=random.choice(url_thumbnails))
    embed.set_footer(text=random.choice(footers), icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

# //////////////////////////////////// INTERNET //////////////////////////////////////////////

@bot.command(aliases=['g'])
async def browse(ctx, *, thing_to_search):
    results = " "
    for result in search(thing_to_search, tld='com', lang='en', safe='off', num=10, start=0,stop=10, pause=1.0):
        results += result + "\n"
    await ctx.send("Search results for: **{}**".format(thing_to_search))
    await ctx.send(results)


@bot.command(aliases=["fact"])
async def get_fact(ctx):
    try:
        await ctx.send(embed=discord.Embed(description=random.choice(facts_list), color=color))
    except TypeError as te:
        await ctx.send(embed=discord.Embed(description=str(te), color=color))
    

@bot.command(aliases=["meme"])
async def get_meme(ctx):
    await ctx.send(random.choice(meme_links))

#///////////////////////////////////// UTILITY ///////////////////////////////////////////////        

@bot.command()
async def snipe(ctx):
    await ctx.send("**Message:** {first}\n**Sender:** {last}".format(first=deleted_messages[ctx.channel.id][-1][1], last=deleted_messages[ctx.channel.id][-1][0]))


@bot.command(aliases=["pfp"])
async def user_pfp(ctx, member:discord.Member=None):
    compliments = ["Man, the daily bugle would pay a lot for this 🤩", "This is nice one! I like it 😎", "Oh Boy! JJJ is gonna be real happy 😃", "🔥🔥🔥","Great Profile Picture, I must say","Damn, where'd you get this? 💙"]
    if member is None:
        embed = discord.Embed(title="Profile Picture : {}".format(ctx.author.name), color=color)
        embed.set_image(url=ctx.author.avatar_url)
    else:
        embed = discord.Embed(title="Profile Picture : {}".format(member.name), color=color)
        embed.set_image(url=member.avatar_url)
    embed.set_footer(text=random.choice(compliments), icon_url="https://i.pinimg.com/236x/9f/9c/11/9f9c11d4eaa3d99bc9a8ece092f5e979.jpg")
    await ctx.send(embed=embed)


@bot.command(aliases=["ping"])
async def get_ping(ctx):
    await ctx.send(embed=discord.Embed(description="𝙇𝙖𝙩𝙚𝙣𝙘𝙮 : {} ms".format(round(bot.latency * 1000)), color=color))


@bot.command(aliases=["serverinfo","si"])
async def server_information(ctx):
    name = str(ctx.guild.name)
    ID = str(ctx.guild.id)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    num_mem = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    role_count = len(ctx.guild.roles)
    bots_list = [bot.mention for bot in ctx.guild.members if bot.bot]
    embed = discord.Embed(title="Server Details: {}".format(name), color=color)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=ID, inline=True)
    embed.add_field(name="Member Count", value=num_mem, inline=True)
    embed.add_field(name="Role Count", value=role_count, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Description", value=description, inline=False)
    embed.add_field(name="Created on", value=ctx.guild.created_at.__format__('%A, %B %d %Y @ %H:%M:%S'), inline=False)
    await ctx.send(embed=embed)

# /////////////////////////////////////// DATE & TIME /////////////////////////////////////////

@bot.command(aliases=["dt"])
async def date_time_ist(ctx):
    tzinfo = pytz.timezone("Asia/Kolkata")
    dateTime = datetime.datetime.now(tz=tzinfo)
    embed = discord.Embed(color=color)
    embed.add_field(name='Date', value="%s/%s/%s" % (dateTime.day, dateTime.month, dateTime.year), inline=False)
    embed.add_field(name='Time', value="%s:%s:%s" % (dateTime.hour, dateTime.minute, dateTime.second), inline=False)
    embed.set_thumbnail(url=url_date_time)
    await ctx.send(embed=embed)   


@bot.command(aliases=["cal.m"])
async def get_calendar(ctx, year, month):
    global url_date_time
    try:
        embed = discord.Embed(description="```{}```".format(calendar.month(int(year), int(month))), color=color)
        embed.set_author(name='𝗖𝗮𝗹𝗲𝗻𝗱𝗮𝗿', icon_url=url_date_time)
        await ctx.send(embed=embed)
    except IndexError:
        embed = discord.Embed(description="{}, this month doesn't exist [📆]".format(ctx.author.name), color=color)
        embed.set_author(name='𝗖𝗮𝗹𝗲𝗻𝗱𝗮𝗿', icon_url=url_calendar)
        await ctx.send(embed=embed)

#///////////////////////////////////// SHELLS ///////////////////////////////////////////

@bot.command(aliases=[";"])
async def sql_shell(ctx, *, expression):
    global cursor
    op_dev = "SELECT * FROM dev_users"
    cursor.execute(op_dev)
    dev_list = cursor.fetchall()
    if str(ctx.author.id) in str(dev_list) or ctx.author.id == 622497106657148939:
        try:
            output = ""
            cursor.execute(expression)
            for item in cursor.fetchall():
                output += str(item) + "\n"
            conn.commit()
            embed = discord.Embed(title=str(expression), description=str(output), color=color)
            embed.set_author(name="MySQL Shell", icon_url=url_author_sql)   
            await ctx.send(embed=embed)
        except Exception as e:
            embed_err = discord.Embed(title="ERROR", description=str(e), color=color)
            embed_err.set_author(name="MySQL Shell", icon_url=url_author_sql)   
            await ctx.send(embed=embed_err)
    else:
        embed = discord.Embed(description="Access Denied", color=color)


@bot.command(aliases=["py"])
async def python_shell(ctx, *, expression):
    global cursor
    op_dev = "SELECT * FROM dev_users"
    cursor.execute(op_dev)
    dev_list = cursor.fetchall()
    if str(ctx.author.id) in str(dev_list) or ctx.author.id == 622497106657148939:
        try:
            embed_acc = discord.Embed(title=str(expression), description=str(eval(expression)), color=color)
            embed_acc.set_author(name="Python Shell", icon_url=url_author_python)
            await ctx.send(embed=embed_acc)
        except Exception as e:
            embed_err = discord.Embed(title="𝗘𝗥𝗥𝗢𝗥", description=str(e), color=color)
            embed_err.set_author(name="Python Shell", icon_url=url_author_python)
            await ctx.send(embed=embed_err)
    else:
        embed_dc = discord.Embed(title="Access Denied", color=color)
        embed_dc.set_author(name="Python Shell",icon_url=url_author_python)
        await ctx.send(embed=embed_dc)


@bot.command(aliases=["pinfo"])
async def function_info(ctx, func):
    if func == "sys.exit()":
        embed = discord.Embed(description="I see what you're trying to do, not gonna happen dude", color=color)
        embed.set_author(name="Permission Denied", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        function = eval(func)
        embed = discord.Embed(description=function.__doc__, color=color)
        embed.set_author(name="Info: {}".format(func), icon_url=url_author_python)
        await ctx.send(embed=embed)

#///////////////////////////////////////// MUSIC /////////////////////////////////////////////

@bot.command(aliases=["cn","connect"])
async def join_vc(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not ctx.message.author.voice:
        embed = discord.Embed(description="{}, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name='Voice', icon_url=url_author_music)
        await ctx.send(embed=embed)
    if voice == None:    
        channel = ctx.message.author.voice.channel
        await channel.connect()
        message = await ctx.send("Connected")
        await asyncio.sleep(2)
        await message.edit(content="Use `t!p <name> or <index>` to play songs 🎵")
    if voice != None:
        embed = discord.Embed(description="Already connected to a voice channel ✅", color=color)
        embed.set_author(name='Voice', icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["dc","disconnect"])
async def leave_vc(ctx):
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        voice_client = ctx.message.guild.voice_client
        try:
            if voice_client.is_connected():
                await voice_client.disconnect() 
                message = await ctx.send("Disconnected")
                await asyncio.sleep(2)
                await message.edit(content="See ya later 😎")
        except AttributeError:
            embed = discord.Embed(description="I am not connected to a voice channel", color=color)
            embed.set_author(name='Music Player', icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to the voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
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
    cursor.execute("""INSERT INTO music_queue(song_name, song_url, server)VALUES("{name}","{url}","{id}")""".format(name=name_of_the_song, url=url, id=str(ctx.guild.id)))
    embed = discord.Embed(description="`{}`".format(name_of_the_song).replace(" - YouTube", " "), color=color)
    embed.set_author(name="Song added", icon_url=url_author_music)
    await ctx.send(embed=embed)


@bot.command(aliases=["view","v"])
async def view_queue(ctx):
    global cursor
    operation_view = "SELECT song_name FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation_view)
    songs = cursor.fetchall()
    string = ""
    song_index = 0
    if len(songs) > 0:
        for song in songs:
            string += str(song_index) + ". " + str(song).replace('("'," ").replace('",)'," ") + "\n"
            song_index += 1
        embed = discord.Embed(title="𝗤𝘂𝗲𝘂𝗲", description=string.replace(" - YouTube"," ").replace("('", " ").replace("',)"," "), color=color)
        embed.set_thumbnail(url=random.choice(url_author_queue))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="No songs in queue...\nUse t!q <song name>", color=color)
        embed.set_author(name="𝗤𝘂𝗲𝘂𝗲", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["auto"])
async def autoplay(ctx, toggle):
    global cursor
    global FFMPEG_OPTS
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    operation_queue = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation_queue)
    songs = cursor.fetchall()
    num = 0
    if toggle == "on":
        if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
            while num <= len(songs):
                voice.stop()
                voice.play(discord.FFmpegPCMAudio(songs[num][1], **FFMPEG_OPTS))
                num += 1
        else:
            await ctx.send("join vc first")
    if toggle == "off":
        voice.stop()


@bot.command(aliases=['play','p'])
async def play_music(ctx, *, char):
    global FFMPEG_OPTS
    # Server Specific Queue
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall()
    # Setup 
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        try:
            if char.isdigit() == False:
                # Web Scrape
                char = char.replace(" ","+")
                htm = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + char)
                video = regex.findall(r"watch\?v=(\S{11})", htm.read().decode())
                url = "https://www.youtube.com/watch?v=" + video[0]
                htm_code = str(urllib.request.urlopen(url).read().decode())
                starting = htm_code.find("<title>") + len("<title>")
                ending = htm_code.find("</title>")
                name_of_the_song = htm_code[starting:ending].replace("&#39;","'").replace("&amp;","&").replace(" - YouTube", " ")
                URL_direct = youtube_download(ctx, url)
                if ctx.voice_client.is_playing() != True:
                    embed = discord.Embed(description="Now playing: `{}`".format(name_of_the_song.replace(" - YouTube", " ")), color=color)
                    embed.set_author(name="Music Player", icon_url=url_author_music)
                    voice.play(discord.FFmpegPCMAudio(str(URL_direct), **FFMPEG_OPTS))
                    await ctx.send(embed=embed)
                else:
                    voice.stop()
                    embed = discord.Embed(description="Now playing: `{}`".format(name_of_the_song.replace(" - YouTube", " ")), color=color)
                    embed.set_author(name="Music Player", icon_url=url_author_music)
                    voice.play(discord.FFmpegPCMAudio(URL_direct, **FFMPEG_OPTS))
                    await ctx.send(embed=embed)
            if char.isdigit() == True: 
                try:  
                    URL_queue = youtube_download(ctx, server_queue[int(char)][1])
                    if ctx.voice_client.is_playing() != True:
                        embed = discord.Embed(description="Now playing: `{}`".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=color)
                        embed.set_author(name="Music Player", icon_url=url_author_music)
                        await ctx.send(embed=embed)
                        voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                    else:
                        voice.stop()
                        embed = discord.Embed(description="Now playing: `{}`".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=color)
                        embed.set_author(name="Music Player", icon_url=url_author_music)
                        await ctx.send(embed=embed)
                        voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                except IndexError:
                    embed = discord.Embed(description="Looks like there is no song at this index", color=color)
                    embed.set_author(name="Oops...", icon_url=url_author_music)
                    await ctx.send(embed=embed)
        except AttributeError:
            await ctx.send(embed=discord.Embed(description='I am not connected to a voice channel'.format(ctx.author.name), color=color))  
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["pause"])
async def pause_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    if ctx.author.id in [mem.id for mem in ctx.voice_client.channel.members]:
        try:
            if playing == True:    
                voice_client.pause()
                message = await ctx.send("Song paused")
                await message.add_reaction("⏸")
            else:
                if pause == True:
                    await ctx.send(embed=discord.Embed(description="Song is already paused ❗", color=color))
                else:
                    embed = discord.Embed(description="No song playing currently ❗", color=color)
                    await ctx.send(embed=embed)
        except Exception as e: 
            embed = discord.Embed(description=str(e), color=color)
            embed.set_author(name="𝗘𝗥𝗥𝗢𝗥", icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["resume","res"])
async def resume_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        try:
            if pause == True:
                voice_client.resume()
                message = await ctx.send("Song resumed")
                await message.add_reaction("▶")
            else:
                if playing == True:
                    embed = discord.Embed(description="Song isn't paused\nUse `t!pause` to pause the song.", color=color)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(embed=discord.Embed(description="No song playing currently\nUse `t!p <name>  or <index>` to play a song.", color=color))
        except Exception as e:
                embed = discord.Embed(description=str(e), color=color)
                embed.set_author(name="𝗘𝗥𝗥𝗢𝗥", icon_url=url_author_music)
                await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["stop","st"])
async def stop_song(ctx):
    voice_client = ctx.message.guild.voice_client
    pause = ctx.voice_client.is_paused()
    playing = ctx.voice_client.is_playing()
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        try:
            if playing == True or pause == True:    
                voice_client.stop()
                message = await ctx.send("Song stopped")
                await message.add_reaction("⏹")
            else:
                await ctx.send(embed=discord.Embed(description="Nothing is playing right now", color=color)
                )
        except Exception as e:
                embed = discord.Embed(description=str(e), color=color)
                embed.set_author(name="ERROR", icon_url=url_author_music)
                await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["clear_queue","cq"])
async def clear_song_queue(ctx):
    global cursor
    operation_queue = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation_queue)
    songs = cursor.fetchall()
    if len(songs) > 0:
        operation_clear_song = "DELETE FROM music_queue WHERE server={}".format(str(ctx.guild.id))
        cursor.execute(operation_clear_song)
        message = await ctx.send("Queue Cleared")
        await message.add_reaction("✅")
    else:
        embed_empty = discord.Embed(description="Queue is already empty ⭕", color=color)
        embed_empty.set_author(name="Hmm...", icon_url=url_author_music)
        await ctx.send(embed=embed_empty)

# /////////////////////////////////////////// EXTRA //////////////////////////////////////////////////

@bot.command(aliases=["web"])
async def thwipper(ctx):
    await ctx.send(embed=discord.Embed(title="*Thwip!*", color=color))

start_token = txt_from_file.find("token=") + len("token=")
end_token = txt_from_file.find('"',start_token + 3) + 1
bot.run(eval(txt_from_file[start_token:end_token]))
