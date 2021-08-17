try:
    from important import token, sql_pass
    import discord
    from discord.utils import get
    from discord.ext import commands, tasks
    import os
    import sys
    import pytz
    import random
    import asyncio
    import calendar
    import datetime
    import regex
    import ffmpeg
    import requests
    import pytube
    import youtube_dl 
    import wikipedia
    import urllib.request
    from cryptography.fernet import Fernet
    from googlesearch import search
    import mysql.connector as ms
    print("All modules successfully imported")
except Exception as e:
    print(str(e))
# SETUP
prefixes = ["t!","_","thwip ", "thwipper "]
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=[prefix for prefix in prefixes], intents=intents, case_insensitive=True)
color = discord.Color.from_rgb(217,226,231)
# SNIPE
deleted_messages = {}
# NUMBER OF REQUESTS
num = 0
# MUSIC
server_index = {}
FFMPEG_OPTS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
    'options': '-vn'
    }
ydl_op = {
    'format':'bestaudio/best',
    'postprocessors':[
        {
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality':'128',
        }],}
# ENCRYPTER DECRYPTER
key = Fernet.generate_key()
cipher = Fernet(key)
# WIT
plot_list = []
dialogue_list = []
# SQL
conn = ms.connect(host="localhost", user="root", passwd=sql_pass, database="discord")
cursor = conn.cursor()
# EXTRAS
hello_urls = ["https://d1lss44hh2trtw.cloudfront.net/assets/article/2018/09/07/how-to-greet-citizens-marvels-spider-man-about-town-trophy_feature.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_abBUARSNVkp-RQ2_gkcgVfa3N6t82VB0kA&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0v0ClnfyO_GOAIzCFRsBFS-OAfcRxRyViXTExPXk3v82_X6BWjqejoWJLm0UT_4m9anU&usqp=CAU","https://geekerhertz.com/images/5ba364c97ea1d.jpg","https://www.clickondetroit.com/resizer/UXG-vEgiShoNSebt4F22ATC4zEY=/640x360/smart/filters:format(jpeg):strip_exif(true):strip_icc(true):no_upscale(true):quality(65)/arc-anglerfish-arc2-prod-gmg.s3.amazonaws.com/public/C2F65R6EKZERHMDNGLI3MRIXGQ.jpg","https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/09/how-to-take-selfies-marvels-spider-man-ps4.jpg","https://pbs.twimg.com/media/DmeykRmU0AAvsQ3.jpg","https://www.mandatory.com/assets/uploads/2018/09/Screen-Shot-2018-09-10-at-7.10.56-PM.png"]
url_en_dec = "https://149351115.v2.pressablecdn.com/wp-content/uploads/2021/01/blog-security-4.png"
url_wiki = "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png"
url_author_python = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png"
url_date_time = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKxv6EIh3VisynQX9TNkA7l15CvR0eJ8nWMA&usqp=CAU"
url_calendar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsb98d6ZOyxwxLUf1Y97yWFKW0Pz6JzuyBww&usqp=CAU"
url_thumbnails = ["https://i.pinimg.com/236x/31/fc/50/31fc5099e24775b613a69fa5bf4f8064.jpg","https://i.pinimg.com/236x/e5/f5/54/e5f55401dfb0588daaa0c3baad528ae8.jpg","https://i.pinimg.com/236x/be/80/cf/be80cf957b028e16083d534f3890cda1.jpg","https://i.pinimg.com/236x/02/6c/7d/026c7d47fd43ff30180fdc7c91e155c2.jpg","https://i.pinimg.com/236x/14/ca/dc/14cadcf0d437fe2d670bff20254e3422.jpg","https://i.pinimg.com/236x/3d/dd/ec/3dddecd82efb45026771dba7287aa010.jpg","https://i.pinimg.com/236x/4d/16/7e/4d167e9a51166d0ce955c4eac6b26d7c.jpg","https://i.pinimg.com/236x/46/56/8c/46568c65f50f4cd5dce76c1ea1833258.jpg","https://i.pinimg.com/236x/74/e6/d8/74e6d846301bd4e3722ed465240b894f.jpg","https://i.pinimg.com/236x/4f/ef/67/4fef67d2a553dba286ab311354370d28.jpg","https://i.pinimg.com/236x/f4/7d/1b/f47d1b34c2988f10a33f77c33e966d4c.jpg","https://i.pinimg.com/236x/4b/5e/bf/4b5ebfaba10beb08d3cae0a4ed684bdb.jpg","https://i.pinimg.com/236x/87/df/c7/87dfc7f867d4afff7c73923664a560af.jpg","https://i.pinimg.com/236x/b4/79/69/b47969fdf761ee63bf60adfdf7ba6554.jpg","https://i.pinimg.com/236x/48/0f/17/480f17eaaf087d44e540ee0a2d512297.jpg","https://i.pinimg.com/236x/4f/ab/0e/4fab0e67c4ba300f03bb5f03421ea7db.jpg","https://i.pinimg.com/236x/f6/06/ef/f606efe1e45c96ee6585cadebc6c8f74.jpg","https://c4.wallpaperflare.com/wallpaper/42/823/767/spiderman-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/517/160/840/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://c4.wallpaperflare.com/wallpaper/107/848/913/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg","https://wallpapercave.com/wp/AVIUso6.jpg","https://wallpapercave.com/wp/n9L3kJf.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-man-miles-morales-minimal-art-4k-43.jpg","https://images.hdqwalls.com/wallpapers/thumb/northern-spider-5k-f3.jpg","https://images.hdqwalls.com/wallpapers/thumb/spider-and-deadpool-4k-ys.jpg","https://images.hdqwalls.com/wallpapers/thumb/spiderman-into-the-spider-verse-y7.jpg","https://wallpapercave.com/wp/wp2018132.png","https://wallpapercave.com/wp/wp2018145.jpg","https://wallpapercave.com/wp/wp2018203.jpg","https://images3.alphacoders.com/593/thumbbig-593562.webp","https://images6.alphacoders.com/107/thumbbig-1071152.webp","https://images6.alphacoders.com/107/thumbbig-1070974.webp","https://i.pinimg.com/236x/38/a4/f6/38a4f62d74d7aeb2ae2396c991fcde52.jpg","https://i.pinimg.com/236x/ed/76/cc/ed76cc8bfe41347d979c93e23fbe51a0.jpg","https://i.pinimg.com/236x/91/87/2d/91872d5c92e8339036106bc832656a49.jpg","https://i.pinimg.com/236x/e3/94/05/e39405072916bb996caee3a4045f573a.jpg","https://i.pinimg.com/236x/36/2c/42/362c4298860d79a4b49acd9370cabe04.jpg","https://i.pinimg.com/236x/cf/3c/f4/cf3cf4ef7239868b1abc243168c41647.jpg","https://i.pinimg.com/236x/b1/3e/e7/b13ee7a8a8d72fbe39153569b5618c21.jpg","https://i.pinimg.com/236x/d9/ef/b8/d9efb89361f4a8d04f2e4e8d8d8067e8.jpg","https://i.pinimg.com/236x/d7/1c/9a/d71c9a5f09e61fcea6ffc3d61f7d5011.jpg","https://i.pinimg.com/236x/3b/cc/8c/3bcc8cde6be346db7c84eaa52e8f9072.jpg","https://i.pinimg.com/236x/ea/0c/ca/ea0ccaa55471689fda39043d80bc7a07.jpg","https://i.pinimg.com/236x/0a/7e/41/0a7e413a95d88ae13487a796d40237ef.jpg","https://i.pinimg.com/236x/d5/ea/83/d5ea830dee3385bfe9fa9871e3190b40.jpg","https://i.pinimg.com/236x/3d/d6/6c/3dd66c95df0b377767bf24e16d77b5ee.jpg"]
url_author_sql = "https://miro.medium.com/max/361/1*WzqoTtRUpmJR26dzlKdIwg.png"
url_author_music = "https://image.freepik.com/free-vector/cute-astronaut-playing-dj-electronic-music-with-headphone-cartoon-icon-illustration-science-technology-icon-concept_138676-2113.jpg"
url_thumbnail_music = ["https://img1.goodfon.com/wallpaper/nbig/1/67/spider-man-chelovek-pauk-pank.jpg","https://images.hdqwalls.com/wallpapers/spiderman-listening-music-4k-2019-fi.jpg","https://cdn.vox-cdn.com/thumbor/m_ZHHA2iEH0WH-8WlX3VQ_pbEZ4=/0x0:1496x727/1570x883/filters:focal(747x258:985x496):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/63096914/Screen_Shot_2019_02_12_at_4.38.43_PM.0.png","https://i.pinimg.com/originals/27/82/21/278221c49efc0426cb4976c598d473a2.jpg","https://i.pinimg.com/736x/43/4a/98/434a987f19fcc4566eeb2f7256ba430e.jpg","https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/39613bc3-140c-41fd-97e6-fcaa0d2690c9/dcms5i5-fa43588f-f74f-4e4d-a32c-f92fd411fd80.png/v1/fill/w_1024,h_485,q_80,strp/marvel_s_spider_man_spider_punk_2_by_jcrprints_dcms5i5-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDg1IiwicGF0aCI6IlwvZlwvMzk2MTNiYzMtMTQwYy00MWZkLTk3ZTYtZmNhYTBkMjY5MGM5XC9kY21zNWk1LWZhNDM1ODhmLWY3NGYtNGU0ZC1hMzJjLWY5MmZkNDExZmQ4MC5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.fN-6-HCnyWgLGYW2WfKEAD8zREmA9n7enfR4qKWRa-Y","https://cdnb.artstation.com/p/assets/images/images/031/120/033/large/jyerps-spider-man-miles-morales-cyberpunk.jpg?1602664632"]

def time_converter(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours == 0:
        return "%02d mins %02d secs" % (mins, secs)
    if hours > 0:
        return "%d hrs %02d mins %02d hrs" % (hours, mins, secs)
def youtube_download(ctx, url):
    if True:
        with youtube_dl.YoutubeDL(ydl_op) as ydl:
            URL = ydl.extract_info(url, download=False)['formats'][0]['url']
    return URL
def requests_query():
    global cursor
    operation = "INSERT INTO requests(number)VALUES({})".format(num)
    cursor.execute(operation)
def number_of_requests():
    global num # num = 0
    num += 1
    requests_query()

@bot.event
async def on_ready():
    print("{0.user} is now online...".format(bot))
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
       
    # UPDATION
    @tasks.loop(seconds=5.0)
    async def updation():
        # REQUESTS UPDATE
        global cursor
        global num
        op = "SELECT MAX(number) FROM requests"
        cursor.execute(op)
        req1 = cursor.fetchall()
        req2 = str(req1).replace("[("," ").replace(",)]"," ")
        num = int(req2)
        conn.commit()
    updation.start()

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🔼":
        pass
    if reaction.emoji == "🔼":
        pass
    
@bot.event
async def on_message(message):
    if f"<@!{bot.user.id}>" in message.content:
            number_of_requests()
            embed = discord.Embed(title="About", description="Hey there! My name is `THWIPPER`.\nI was made by Spider-Man to tend to people's needs on discord while he is out in the city protecting the innocent from harm.", color=color)
            embed.set_thumbnail(url=bot.user.avatar_url)
            embed.set_footer(text="Type _use for command menu", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
    else:
        await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if not message.channel.id in list(deleted_messages.keys()):
        deleted_messages[message.channel.id] = []
    deleted_messages[message.channel.id].append((str(message.author), message.content))

# //////////////////////////////////// SPECIAL ACCESS /////////////////////////////////////////

@bot.command(aliases=["allow","alw"])
async def allow_access(ctx, member:discord.Member):
    number_of_requests()
    global cursor
    if ctx.author.id == 622497106657148939:
        print("{} has been allowed access.".format(member.name))
        cursor.execute("INSERT INTO dev_users(dev_id)values({})".format(str(member.id)))
        embed = discord.Embed(description="{} has been allowed access".format(member), color=color)
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=color)


@bot.command(aliases=["restrict","rstr"])
async def remove_access(ctx, member:discord.Member):
    number_of_requests()
    global url_author_python
    global cursor
    if ctx.author.id == 622497106657148939:    
        print("{} has been denied access.".format(member.name))
        cursor.execute("DELETE FROM dev_users WHERE dev_id={}".format(str(member.id)))    
        embed = discord.Embed(description="{} is now restricted".format(str(member)), color=color)
        embed.set_author(name="Python Shell", icon_url=url_author_python)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Access Denied", color=color)    
        

@bot.command()
async def clear(ctx, text, num=10000000000000):
    number_of_requests()
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
    number_of_requests()
    global cursor
    global conn
    msgs = ["Bye {}!".format(ctx.author.name), "See ya {}!".format(ctx.author.name), "Till next time {}".format(ctx.author.name)]
    if ctx.author.id == 622497106657148939:
        await ctx.send(random.choice(msgs))
        conn.commit()
        print(random.choice(msgs))
        exit()
    else:
        await ctx.send("Access Denied")
    
#///////////////////////////////////// STANDARD //////////////////////////////////////////////

@bot.command(aliases=['hello', 'hi', 'hey', 'hey there', 'salut',"kon'nichiwa","hola","aloha"])
async def greet_bot(ctx):
    number_of_requests()
    greetings = ["Hey {}!".format(ctx.author.name), "Hi {}!".format(ctx.author.name), "How's it going {}?".format(ctx.author.name), "What can I do for you {}?".format(ctx.author.name), "What's up {}?".format(ctx.author.name), "Hello {}!".format(ctx.author.name)]
    embed = discord.Embed(title=random.choice(greetings), color=color)
    embed.set_image(url=random.choice(hello_urls))
    await ctx.send(embed=embed)


@bot.command(aliases=['use','h'])
async def embed_help(ctx):
    number_of_requests()
    global url_thumbnails
    embed = discord.Embed(title="🕸𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗠𝗲𝗻𝘂🕸",
                        description="Prefixes => `[t!] [ _ ] [thwip] [thwipper]`",
                        color=color)
    embed.add_field(name="𝗦𝘁𝗮𝗻𝗱𝗮𝗿𝗱",value="hello to greet bot\nuse to get this embed\nquips to get a famous dialogue or plot\n@Thwipper to get more info about thwipper", inline=False)
    embed.add_field(name="𝗨𝘁𝗶𝗹𝗶𝘁𝘆", value="req to get number of requests\nping to get user latency\nserverinfo to get server's information\npfp to get user's profile picture\nsnipe to see deleted message", inline=False)
    embed.add_field(name="𝗘𝗻𝗰𝗿𝘆𝗽𝘁𝗲𝗿 𝗗𝗲𝗰𝗿𝘆𝗽𝘁𝗲𝗿", value="hush en <text> to encrypt message\nhush dec <text> to decrypt message\n", inline=False)
    embed.add_field(name="𝗗𝗧𝗖", value="dt to get IST date and time\ncal.m <year, month(in number)> to get calendar", inline=False)
    embed.add_field(name="𝗦𝗵𝗲𝗹𝗹𝘀", value="; <query> to use SQL Shell\npy for python shell\npinfo to get use of that python function", inline=False)
    embed.add_field(name="𝗜𝗻𝘁𝗲𝗿𝗻𝗲𝘁",value="w <topic> for wikipedia\ng <topic> to google\nl <song> to get lyrics",inline=False)
    embed.add_field(name="𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹",value="cn to get the bot to join voice channel\ndc to remove bot from voice channel",inline=False)
    embed.add_field(name="𝗣𝗹𝗮𝘆𝗲𝗿",value="p <name> or <index> to play songs\nres to resume a song\npause to pause a song\nst to stop a song\nbit to set quality of bitrate", inline=False)
    embed.add_field(name="𝗤𝘂𝗲𝘂𝗲",value="q <name> to add a song to the queue\nq to view queue\nskip to skip song\nprev for previous song\nthis to get current song\nrem <index> to remove song from queue\ncq to clear queue", inline=False)
    embed.set_thumbnail(url=random.choice(url_thumbnails))
    embed.set_footer(text="New Features Coming Soon! [🛠]\n3)Loop Queue  4)Repeat Song 5)Volume")
    await ctx.send(embed=embed)


@bot.command(aliases=["quips"])
async def get_quips(ctx):
    number_of_requests()
    global plot_list
    global dialogue_list
    quips_list = []
    for plot in plot_list:
        for dialogue in dialogue_list:
            quips_list.append(plot)
            quips_list.append(dialogue)
    titles = ["Oh man, I remember this one!","Here you go...","I gotta say, this still holds up today..."]
    footers = ["Man, this is killer material!","Now this is what I call a good wit!","Oh boy, this is one of my favorites!"]
    embed = discord.Embed(title=random.choice(titles), description=random.choice(quips_list), color=color)
    embed.set_thumbnail(url=random.choice(url_thumbnails))
    embed.set_footer(text=random.choice(footers), icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)
    print("Quip successfully sent!")

# //////////////////////////////////// INTERNET //////////////////////////////////////////////

@bot.command(aliases=['wiki','w'])
async def wikipedia_results(ctx, *, thing_to_search):
    try:
        try:    
            title = wikipedia.page(thing_to_search)
            embed = discord.Embed(description=wikipedia.summary(thing_to_search), color=color)
            embed.set_author(name=title.title, icon_url=url_wiki)
            embed.add_field(name='Search References', value=', '.join([x for x in wikipedia.search(thing_to_search)][:5]), inline=False)
            embed.set_footer(text="Searched by: {}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except wikipedia.PageError as pe:
            embed = discord.Embed(description=str(pe), color=color)
            embed.set_author(name='Error', icon_url=url_wiki)   
            await ctx.send(embed=embed)
            print("{} couldn't be showed due to PageError".format(title.title))
    except wikipedia.DisambiguationError as de:
        embed = discord.Embed(description=str(de), color=color)
        embed.set_author(name='Hmm...', icon_url=url_wiki)   
        await ctx.send(embed=embed)
        print("ERROR : Disambiguation Error")


@bot.command(aliases=['google','g'])
async def google_results(ctx, *, thing_to_search):
    number_of_requests()
    results = " "
    for result in search(thing_to_search, tld='com', lang='en', safe='off', num=6, start=0,stop=10, pause=1.0):
        results += result + "\n"
    await ctx.send("Search results for: **{}**".format(thing_to_search))
    await ctx.send(results)
    print("Results for google search sent...")


@bot.command(aliases=["lyrics","l"])
async def song_lyrics(ctx, *, song_name=""):
    try:
        number_of_requests()
        search_url = ("https://search.azlyrics.com/search.php?q=" + song_name.replace(" ","+"))
        url = ""
        markup = urllib.request.urlopen(search_url).read().decode()
        a = markup.find("text-left visitedlyr")
        b = int(int(markup.find('href="', a)) + len('href="'))
        c = markup.find('"', b)
        url = markup[b:c]
        if len(url) > 3:
            lyric_1 = urllib.request.urlopen(url).read().decode()
            lyric_2 = lyric_1[int(lyric_1.find("Sorry about that. -->") + len("Sorry about that. -->")):lyric_1.find("</div>", int(lyric_1.find("Sorry about that. -->") + 10))].replace("<br>"," ").replace("<i>", "_").replace("</i>", "_")
            song_title = lyric_1[lyric_1.find("<title>") + len("<title>"):lyric_1.find("</title>")] + "\n"
            if len(lyric_1) <= 1900:
                embed1 = discord.Embed(title=song_title, description=lyric_2.replace("&quot;", '"'), color=color)
                embed1.set_author(name="Song Lyrics", icon_url=url_author_music)
                embed1.set_thumbnail(url=random.choice(url_thumbnail_music))
                embed1.set_footer(text="Seached by: {}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed1)
                pass
            else:
                embed1 = discord.Embed(title=song_title, description=lyric_2[0:1900].replace("&quot;", '"'), color=color)
                embed1.set_author(name="Song Lyrics", icon_url=url_author_music)
                embed1.set_thumbnail(url=random.choice(url_thumbnail_music))
                embed2 = discord.Embed(description=lyric_2[1900:].replace("&quot;", '"'), color=color)
                embed2.set_author(name="Continued...", icon_url=url_author_music)
                embed2.set_thumbnail(url=random.choice(url_thumbnail_music))
                embed2.set_footer(text="Seached by: {}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed1)
                await ctx.send(embed=embed2)
            print("Lyrics sent successfully...")
        else:
            embed = discord.Embed(description="Couldn't find song...\nMake sure the song name is correct 🤔", color=color)
            embed.set_author(name="Song Lyrics", icon_url=url_author_music)
            await ctx.send(embed=embed)
            print("Song not found...")
    except Exception as e:
        embed = discord.Embed(description=str(e), color=color)
        embed.set_author(name="Error", icon_url=url_author_music)
        await ctx.send(embed=embed)
        print("Error", str(e))

#///////////////////////////////////// UTILITY ///////////////////////////////////////////////        

@bot.command(aliases=['req','requests'])
async def total_requests(ctx):
    number_of_requests()
    global cursor
    operation = "SELECT MAX(number) FROM requests"
    cursor.execute(operation)
    total = cursor.fetchall()
    embed = discord.Embed(description= "**Requests made: **" + str(total).replace("[(", " ").replace(",)]", " "), color=color)
    await ctx.send(embed=embed)


@bot.command()
async def snipe(ctx, num_msg=None):
    number_of_requests()
    if num_msg is None:
        await ctx.send("**Message:** {first}\n**Sender:** {last}".format(first=deleted_messages[ctx.channel.id][-1][1], last=deleted_messages[ctx.channel.id][-1][0]))
    if num_msg is not None:
        for message in deleted_messages:
            pass


@bot.command(aliases=["pfp"])
async def user_pfp(ctx, member:discord.Member=None):
    number_of_requests()
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
    number_of_requests()
    await ctx.send(embed=discord.Embed(description="**Latency:** {} ms".format(round(bot.latency * 1000)), color=color))


@bot.command(aliases=["serverinfo","si"])
async def server_information(ctx):
    number_of_requests()
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

# //////////////////////////////////////// Encrypter / Decrypter //////////////////////////////////

@bot.command(aliases=["hush"])
async def encrypt_data(ctx, mode, *, message):
    number_of_requests()
    global key, cipher
    res = message.encode()
    try:
        if mode == "en":
            embed = discord.Embed(title="Message Encrpyted", description="```{}```".format(str(cipher.encrypt(res))).replace("b'"," ").replace("'"," "), color=color)
            embed.set_thumbnail(url=url_en_dec)
            await ctx.send(embed=embed)
        if mode == "dec":
            embed = discord.Embed(title="Message Decrypted", description="```{}```".format(str(cipher.decrypt(res))).replace("b'"," ").replace("'"," "), color=color)
            embed.set_thumbnail(url=url_en_dec)
            await ctx.send(embed=embed)
    except Exception as e:
            embed = discord.Embed(title="Error", description=str(e), color=color)
            embed.set_thumbnail(url=url_en_dec)
            await ctx.send(embed=embed)

# /////////////////////////////////////// DATE & TIME /////////////////////////////////////////

@bot.command(aliases=["dt"])
async def date_time_ist(ctx):
    number_of_requests()
    tzinfo = pytz.timezone("Asia/Kolkata")
    dateTime = datetime.datetime.now(tz=tzinfo)
    embed = discord.Embed(color=color)
    embed.add_field(name='Date', value="%s/%s/%s" % (dateTime.day, dateTime.month, dateTime.year), inline=False)
    embed.add_field(name='Time', value="%s:%s:%s" % (dateTime.hour, dateTime.minute, dateTime.second), inline=False)
    embed.set_thumbnail(url=url_date_time)
    await ctx.send(embed=embed)   


@bot.command(aliases=["cal.m"])
async def get_calendar(ctx, year, month):
    number_of_requests()
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
    number_of_requests()
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
    number_of_requests()
    global cursor
    op_dev = "SELECT * FROM dev_users"
    cursor.execute(op_dev)
    dev_list = cursor.fetchall()
    denied = ["sys.exit()", "eval(sys.exit)", "token", "sql_pass", 'eval("token")', "eval('token')",'eval("sql_pass")',"key","cipher","eval('cipher')",'eval("cipher")',"eval('key')",'eval("key")']
    if str(ctx.author.id) in str(dev_list) or ctx.author.id == 622497106657148939:
        if expression == [msg for msg in denied]:
            embed = discord.Embed(description="This function will not be executed", color=color)
            embed.set_author(name="Access Denied", icon_url=url_author_python)
            await ctx.send(embed=embed)
        else:
            try:
                embed_acc = discord.Embed(title=str(expression), description=str(eval(expression)), color=color)
                embed_acc.set_author(name="Python Shell", icon_url=url_author_python)
                await ctx.send(embed=embed_acc)
            except Exception as e:
                embed_err = discord.Embed(title="ERROR", description=str(e), color=color)
                embed_err.set_author(name="Python Shell", icon_url=url_author_python)
                await ctx.send(embed=embed_err)
    else:
        embed_dc = discord.Embed(title="Access Denied", color=color)
        embed_dc.set_author(name="Python Shell",icon_url=url_author_python)
        await ctx.send(embed=embed_dc)


@bot.command(aliases=["pinfo"])
async def function_info(ctx, func):
    number_of_requests()
    try:
        if "(" in [char for char in func] and ")" in [char for char in func]:
            embed = discord.Embed(description="Sorry, can't do functions. Do without brackets to get information", color=color)
            embed.set_author(name="Access Denied", icon_url=url_author_python)
            await ctx.send(embed=embed)
        else:
            function = eval(func)
            embed = discord.Embed(description=function.__doc__, color=color)
            embed.set_author(name="Info: {}".format(func), icon_url=url_author_python)
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=str(e), color=color)
        embed.set_author(name="ERROR", icon_url=url_author_python)
        await ctx.send(embed=embed)

#///////////////////////////////////////// MUSIC /////////////////////////////////////////////

@bot.command(aliases=["cn","connect"])
async def join_vc(ctx):
    number_of_requests()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
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
            print("Connected Successfully...")
        if voice != None:
            embed = discord.Embed(description="Already connected to a voice channel ✅", color=color)
            embed.set_author(name='Voice', icon_url=url_author_music)
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description="Error:\n" + str(e), color=color)
        embed.set_author(name='Voice', icon_url=url_author_music)


@bot.command(aliases=["dc","disconnect"])
async def leave_vc(ctx):
    number_of_requests()
    try:
        if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
            voice_client = ctx.message.guild.voice_client
            try:
                if voice_client.is_connected():
                    await voice_client.disconnect() 
                    message = await ctx.send("Disconnected")
                    await asyncio.sleep(2)
                    await message.edit(content="See ya later 😎")
                    print("Disconnected Successfully...")
            except AttributeError:
                embed = discord.Embed(description="I am not connected to a voice channel", color=color)
                embed.set_author(name='Music Player', icon_url=url_author_music)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="{}, buddy, connect to the voice channel first 🔊".format(ctx.author.name), color=color)
            embed.set_author(name="Music Player", icon_url=url_author_music)
            await ctx.send(embed=embed)
    except AttributeError:
        embed = discord.Embed(description="I am not connected to a voice channel", color=color)
        embed.set_author(name='Music Player', icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["setbit","bit"])
async def set_bitrate(ctx, kbps):
    number_of_requests()
    global cursor
    op_dev = "SELECT * FROM dev_users"
    cursor.execute(op_dev)
    dev_list = cursor.fetchall()
    if str(ctx.author.id) in str(dev_list) or ctx.author.id == 622497106657148939:
        for items in ydl_op['postprocessors']:
            items['preferredquality'] = str(kbps)
            embed = discord.Embed(description='**Bitrate:** {} kbps'.format(kbps), color=color)
            embed.set_author(name='Audio Quality', icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        await ctx.send(title="Access Denied", description="{}, only dev users can edit bitrate".format(ctx.author.name))
    

@bot.command(aliases=["queue","q"])
async def queue_song(ctx, *, name=None):
    number_of_requests()
    global cursor
    if name is not None:
        name = name.replace(" ", "+")
        htm = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + name) # the 11 lettered string which is like an ID for videos is stored inside the variable video
        video = regex.findall(r"watch\?v=(\S{11})", htm.read().decode())
        url = "https://www.youtube.com/watch?v=" + video[0] # we got the html code of the full search page
        htm_code = str(urllib.request.urlopen(url).read().decode()) # htm_code contains the entire HTML code of the web page where we see the video
        starting = htm_code.find("<title>") + len("<title>") # now we use .find method to find the title of the vid which is in between <title></title> tags
        ending = htm_code.find("</title>")        
        name_of_the_song = htm_code[starting:ending].replace("&#39;","'").replace("&amp;","&") # here we replace uncessary things like tags because we only want the title
        cursor.execute("""INSERT INTO music_queue(song_name, song_url, server)VALUES("{name}","{url}","{id}")""".format(name=name_of_the_song, url=url, id=str(ctx.guild.id)))
        embed = discord.Embed(description="{}".format(name_of_the_song).replace(" - YouTube", " "), color=color)
        embed.set_author(name="Song added", icon_url=url_author_music)
        await ctx.send(embed=embed)
        print("Song added to {}'s queue successfully...".format(ctx.guild.name))
    if name is None:
        operation_view = "SELECT song_name FROM music_queue WHERE server={}".format(str(ctx.guild.id))
        cursor.execute(operation_view)
        songs = cursor.fetchall()
        string = ""
        song_index = 0
        if len(songs) > 0:
            for song in songs:
                string += str(song_index) + ". " + str(song).replace('("'," ").replace('",)'," ") + "\n"
                song_index += 1
            embed = discord.Embed(description="{a}\n**Number of songs:** {b}".format(a=string.replace(" - YouTube"," ").replace("('", " ").replace("',)"," "), b=len(songs)), color=color)
            embed.set_author(name="{}'s Queue".format(ctx.guild.name), icon_url=url_author_music)
            embed.set_thumbnail(url=random.choice(url_thumbnail_music))
            queue = await ctx.send(embed=embed)
            await queue.add_reaction("🔼")
            await queue.add_reaction("🔽")
        else:
            embed = discord.Embed(description="No songs in queue...\nUse t!q <song name>", color=color)
            embed.set_author(name="{}'s Queue".format(ctx.guild.name), icon_url=url_author_music)
            await ctx.send(embed=embed)


@bot.command(aliases=["auto"])
async def autoplay(ctx, toggle):
    number_of_requests()
    global cursor
    global FFMPEG_OPTS
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    operation_queue = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation_queue)
    songs = cursor.fetchall()
    num = 0
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        if toggle == "on":
            while num <= len(songs):
                if ctx.voice_client.is_playing() == True:
                    voice.stop()
                    embed = discord.Embed(description="**Song: **{}".format(songs[num][0]).replace(" - YouTube", " "), color=color)
                    embed.set_author(name="Now playing", icon_url=url_author_music)
                    embed.set_thumbnail(url=pytube.YouTube(url=songs[num][1]).thumbnail_url)
                    embed.add_field(name="Artist", value=pytube.YouTube(url=songs[num][1]).author, inline=True)
                    embed.add_field(name="Duration", value=pytube.YouTube(url=songs[num][1]).length, inline=True)
                    await ctx.send(embed=embed)
                    voice.play(discord.FFmpegPCMAudio(songs[num][1], **FFMPEG_OPTS))
                    duration = pytube.YouTube(url=songs[num][1]).length
                    await asyncio.sleep(duration)
                    num += 1
                    continue
                if ctx.voice_client.is_playing() == False:
                    embed = discord.Embed(description="**Song: **{}".format(songs[num][0]).replace(" - YouTube", " "), color=color)
                    embed.set_author(name="Now playing", icon_url=url_author_music)
                    embed.set_thumbnail(url=pytube.YouTube(url=songs[num][1]).thumbnail_url)
                    embed.add_field(name="Artist", value=pytube.YouTube(url=songs[num][1]).author, inline=True)
                    embed.add_field(name="Duration", value=pytube.YouTube(url=songs[num][1]).length, inline=True)
                    await ctx.send(embed=embed)
                    voice.play(discord.FFmpegPCMAudio(songs[num][1], **FFMPEG_OPTS))
                    duration = pytube.YouTube(url=songs[num][1]).length
                    await asyncio.sleep(duration)
                    num += 1
                    continue
        if toggle == "off":
            voice.stop()
            embed = discord.Embed(description="Autoplay : OFF", color=color)
            embed.set_author(name="Music Player", icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=['play','p'])
async def play_music(ctx, *, char):
    number_of_requests()
    global server_index
    global FFMPEG_OPTS
    # Server Specific Queue
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall()
    # Setup 
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
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
                    # duration_direct = pytube.YouTube(url=url).length/60
                    if ctx.voice_client.is_playing() != True:
                        embed = discord.Embed(description="**Song: **{}".format(name_of_the_song).replace(" - YouTube", " "), color=color)
                        embed.set_author(name="Now playing", icon_url=url_author_music)
                        embed.set_thumbnail(url=pytube.YouTube(url=url).thumbnail_url)
                        embed.add_field(name="Uploader", value=pytube.YouTube(url=url).author, inline=True)
                        embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=url).length), inline=True)
                        await ctx.send(embed=embed)
                        voice.play(discord.FFmpegPCMAudio(URL_direct, **FFMPEG_OPTS))
                        print("Now playing: {}...".format(name_of_the_song))
                    else:
                        voice.stop()
                        embed = discord.Embed(description="**Song: **{}".format(name_of_the_song).replace(" - YouTube", " "), color=color)
                        embed.set_author(name="Now playing", icon_url=url_author_music)
                        embed.set_thumbnail(url=pytube.YouTube(url=url).thumbnail_url)
                        embed.add_field(name="Uploader", value=pytube.YouTube(url=url).author, inline=True)
                        embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=url).length), inline=True)
                        await ctx.send(embed=embed)
                        voice.play(discord.FFmpegPCMAudio(URL_direct, **FFMPEG_OPTS))
                        print("Now playing: {}...".format(name_of_the_song))
                if char.isdigit() == True:
                    if str(ctx.guild.id) not in server_index:
                        server_index[str(ctx.guild.id)] = int(char)
                        print("Server Index Dict is updated...")
                    else:
                        pass
                    if str(ctx.guild.id) in server_index:
                        server_index[str(ctx.guild.id)] = int(char)
                    try:  
                        URL_queue = youtube_download(ctx, server_queue[int(char)][1])
                        if ctx.voice_client.is_playing() != True:
                            embed = discord.Embed(description="**Song: **{}".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=color)
                            embed.set_author(name="Now playing", icon_url=url_author_music)
                            embed.set_thumbnail(url=pytube.YouTube(url=server_queue[int(char)][1]).thumbnail_url)
                            embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[int(char)][1]).author, inline=True)
                            embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[int(char)][1]).length), inline=True)
                            await ctx.send(embed=embed)
                            voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                            print("Now playing: {}...".format(server_queue[int(char)][0]))
                        else:
                            voice.stop()
                            embed = discord.Embed(description="**Song: **{}".format(server_queue[int(char)][0]).replace(" - YouTube", " "), color=color)
                            embed.set_author(name="Now playing", icon_url=url_author_music)
                            embed.set_thumbnail(url=pytube.YouTube(url=server_queue[int(char)][1]).thumbnail_url)
                            embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[int(char)][1]).author, inline=True)
                            embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[int(char)][1]).length), inline=True)
                            await ctx.send(embed=embed)
                            voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                            print("Now playing: {}...".format(server_queue[int(char)][0]))
                    except IndexError:
                        embed = discord.Embed(description="Looks like there is no song at this index", color=color)
                        embed.set_author(name="Oops...", icon_url=url_author_music)
                        await ctx.send(embed=embed)
            except AttributeError:
                embed = discord.Embed(description='I am not connected to a voice channel'.format(ctx.author.name), color=color)
                embed.set_author(name="Voice", icon_url=url_author_music)
                await ctx.send(embed=embed)  
        else:
            embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
            embed.set_author(name="Music Player", icon_url=url_author_music)
            await ctx.send(embed=embed)
    except AttributeError:
        embed = discord.Embed(description='I am not connected to a voice channel'.format(ctx.author.name), color=color)
        embed.set_author(name="Voice", icon_url=url_author_music)
        await ctx.send(embed=embed)  


@bot.command(aliases=["this","song","ts"])
async def fetch_current_song(ctx):
    number_of_requests()
    global server_index
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall()
    try:
        embed = discord.Embed(description="**Song: **{a}\n**Index: **{b}".format(a=server_queue[server_index[str(ctx.guild.id)]][0], b=server_index[str(ctx.guild.id)]).replace(" - YouTube", " "), color=color)
        embed.set_author(name="Currently Playing", icon_url=url_author_music)
        embed.set_thumbnail(url=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).thumbnail_url)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=str(e), color=color)
        embed.set_author(name="Error", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["prev","previous"])
async def previous_song(ctx):
    number_of_requests()
    global server_index
    server_index[str(ctx.guild.id)] -= 1
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        try:  
            URL_queue = youtube_download(ctx, server_queue[server_index[str(ctx.guild.id)]][1])
            if ctx.voice_client.is_playing() != True:
                embed = discord.Embed(description="**Song: **{}".format(server_queue[server_index[str(ctx.guild.id)]][0]).replace(" - YouTube", " "), color=color)
                embed.set_author(name="Now playing", icon_url=url_author_music)
                embed.set_thumbnail(url=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).thumbnail_url)
                embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).author, inline=True)
                embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).length), inline=True)
                await ctx.send(embed=embed)
                voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                print("Now playing: {}...".format(server_queue[server_index[str(ctx.guild.id)]][0]))
            else:
                voice.stop()
                embed = discord.Embed(description="**Song: **{}".format(server_queue[server_index[str(ctx.guild.id)]][0]).replace(" - YouTube", " "), color=color)
                embed.set_author(name="Now playing", icon_url=url_author_music)
                embed.set_thumbnail(url=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).thumbnail_url)
                embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).author, inline=True)
                embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).length), inline=True)
                await ctx.send(embed=embed)
                voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                print("Now playing: {}...".format(server_queue[server_index[str(ctx.guild.id)]][0]))
        except IndexError:
            embed = discord.Embed(description="Looks like there is no song at this index", color=color)
            embed.set_author(name="Oops...", icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["skip","next"])
async def skip_song(ctx):
    number_of_requests()
    global server_index
    server_index[str(ctx.guild.id)] += 1
    operation = "SELECT * FROM music_queue WHERE server={}".format(str(ctx.guild.id))
    cursor.execute(operation)
    server_queue = cursor.fetchall()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
        try:  
            URL_queue = youtube_download(ctx, server_queue[server_index[str(ctx.guild.id)]][1])
            if ctx.voice_client.is_playing() != True:
                embed = discord.Embed(description="**Song: **{}".format(server_queue[server_index[str(ctx.guild.id)]][0]).replace(" - YouTube", " "), color=color)
                embed.set_author(name="Now playing", icon_url=url_author_music)
                embed.set_thumbnail(url=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).thumbnail_url)
                embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).author, inline=True)
                embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).length), inline=True)
                await ctx.send(embed=embed)
                voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                print("Now playing: {}...".format(server_queue[server_index[str(ctx.guild.id)]][0]))
            else:
                voice.stop()
                embed = discord.Embed(description="**Song: **{}".format(server_queue[server_index[str(ctx.guild.id)]][0]).replace(" - YouTube", " "), color=color)
                embed.set_author(name="Now playing", icon_url=url_author_music)
                embed.set_thumbnail(url=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).thumbnail_url)
                embed.add_field(name="Uploader", value=pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).author, inline=True)
                embed.add_field(name="Duration", value=time_converter(pytube.YouTube(url=server_queue[server_index[str(ctx.guild.id)]][1]).length), inline=True)
                await ctx.send(embed=embed)
                voice.play(discord.FFmpegPCMAudio(URL_queue, **FFMPEG_OPTS))
                print("Now playing: {}...".format(server_queue[server_index[str(ctx.guild.id)]][0]))
        except IndexError:
            embed = discord.Embed(description="Looks like there is no song at this index", color=color)
            embed.set_author(name="Oops...", icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["pause"])
async def pause_song(ctx):
    number_of_requests()
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
            embed.set_author(name="Error", icon_url=url_author_music)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["resume","res"])
async def resume_song(ctx):
    number_of_requests()
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
                    embed = discord.Embed(description="Song is not paused 🤔", color=color)
                    embed.set_author(name="Music Player", icon_url=url_author_music)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(description="Nothing is playing right now", color=color)
                    embed.set_author(name="Music Player", icon_url=url_author_music)
                    await ctx.send(embed=embed)
        except Exception as e:
                embed = discord.Embed(description=str(e), color=color)
                embed.set_author(name="Error", icon_url=url_author_music)
                await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="{}, buddy, connect to a voice channel first 🔊".format(ctx.author.name), color=color)
        embed.set_author(name="Music Player", icon_url=url_author_music)
        await ctx.send(embed=embed)


@bot.command(aliases=["stop","st"])
async def stop_song(ctx):
    number_of_requests()
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


@bot.command(aliases=["rem","remove"])
async def remove_song(ctx, index):
    global cursor
    number_of_requests()
    operation_view = 'SELECT * FROM music_queue WHERE server="{}"'.format(str(ctx.guild.id))
    cursor.execute(operation_view)
    songs = cursor.fetchall()
    embed = discord.Embed(description="{}".format(songs[int(index)][0]), color=color)
    embed.set_author(name="Song removed", icon_url=url_author_music)
    await ctx.send(embed=embed)
    operation_remove = "DELETE FROM music_queue WHERE song_url = '{a}' AND server='{b}'".format(a=songs[int(index)][1], b=str(ctx.guild.id))
    cursor.execute(operation_remove)


@bot.command(aliases=["clear_queue","cq"])
async def clear_song_queue(ctx):
    number_of_requests()
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
        embed_empty = discord.Embed(description="Queue is already empty 🤷🏻‍♂️", color=color)
        embed_empty.set_author(name="Hmm...", icon_url=url_author_music)
        await ctx.send(embed=embed_empty)

# /////////////////////////////////////////// EXTRA //////////////////////////////////////////////////

@bot.command(aliases=["web","thwip"])
async def thwipper(ctx):
    number_of_requests()
    await ctx.send(embed=discord.Embed(title="*Thwip!*", color=color))

bot.run(token)
