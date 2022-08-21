# This file contains all music functions.

import nextcord
import random
import urllib
import regex
import youtube_dl
import pytube

from utils.responses import connections, disconnections
from utils.functions import embed
from utils.links import url_author_music
from utils.assets import YDL_OP, FFMPEG_OPTS, time_converter
from nextcord.ext import commands

class Music(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @staticmethod
    def youtube_download(ctx, url):
        if True:
            with youtube_dl.YoutubeDL(YDL_OP) as ydl:
                URL = ydl.extract_info(url, download=False)["formats"][0]["url"]
        return URL
        
    # voice channel
    @commands.command(aliases=["cn", "join"], description="Bot joins the voice channel.")
    async def join_vc(self, ctx):
        
        voice = nextcord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            if not ctx.message.author.voice:
                await ctx.send(
                    embed=embed(
                        description=f"{ctx.author.name}, connect to a voice channel first 🔊",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        }
                    )
                )
            if voice == None:
                channel = ctx.message.author.voice.channel
                await channel.connect()
                await ctx.send(
                    embed=embed(
                        description=f"Connected to {ctx.guild.voice_client.channel.name}",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        },
                        footer={
                            "text": random.choice(connections),
                            "icon_url": ""
                        }
                    )
                )
            if voice != None:
                await ctx.send(
                    embed=embed(
                        description="Already connected to a voice channel ✅",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        },
                        footer={
                            "text": random.choice(connections),
                            "icon_url": ""
                        }
                    )
                )     
        except Exception as exception:
            await ctx.send(
                embed=embed(
                    description=f"Error:\n{str(exception)}",
                    color=self.bot.color(ctx.guild),
                    author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                    }
                )
            )


    @commands.command(aliases=["dc", "leave"], description="Bot will leave voice channel.")
    async def leave_vc(self, ctx):
        
        try:
            if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
                voice_client = ctx.message.guild.voice_client  
                try:
                    if voice_client.is_connected():
                        await ctx.send(
                            embed=embed(
                                description=f"Disconnected from {ctx.guild.voice_client.channel.name}",
                                color=self.bot.color(ctx.guild),
                                author={
                                    "name": "Spider-Punk Radio™",
                                    "icon_url": url_author_music
                                },
                                footer={
                                    "text": random.choice(disconnections),
                                    "icon_url": ""
                                }
                            )
                        )
                        await voice_client.disconnect()
                except AttributeError:
                    await ctx.send(
                        embed=embed(
                            description=f"I am not connected to any voice channel.",
                            color=self.bot.color(ctx.guild),
                            author={
                                "name": "Spider-Punk Radio™",
                                "icon_url": url_author_music
                            }
                        )
                    )
            else:
                await ctx.send(
                    embed=embed(
                        description=f"{ctx.author.name}, connect to a voice channel first 🔊",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        }
                    )
                )
        except AttributeError:
            await ctx.send(
                embed=embed(
                    description="I am not connected to any voice channel.",
                    color=self.bot.color(ctx.guild),
                    author={
                        "name": "Spider-Punk Radio™",
                        "icon_url": url_author_music
                    }
                )
            )

    # play music (playing from queue will be implemented eventually, right now it's just direct play.)
    @commands.command(aliases=["play", "p"], description="Play music.")
    async def play_music(self, ctx, *, char):
        
        voice = nextcord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        if ctx.author.id in [member.id for member in ctx.voice_client.channel.members]:
            # web scrape
            try:
                char = char.replace(" ", "+")
                markup = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + char)
                vid = regex.findall(r"watch\?v=(\S{11})", markup.read().decode())
                url = "https://www.youtube.com/watch?v=" + vid[0]
                markup_code = str(urllib.request.urlopen(url).read().decode())
                starting = markup_code.find("<title>") + len("<title>")
                ending = markup_code.find("</title>")
                song_name = {
                    markup_code[starting:ending]
                    .replace("&#39", "'")
                    .replace("&amp", "&")
                    .replace(" - YouTube", "")
                }
                URL_direct = Music.youtube_download(ctx, url)

                if ctx.voice_client.is_playing(): pass
                else: voice.stop()
        
                await ctx.send(
                    embed=embed(
                        description=f"**Now playing: **{song_name}",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        },
                        thumbnail=pytube.YouTube(url=url).thumbnail_url,
                        fields={
                            "Uploader": pytube.YouTube(url=url).author,
                            "Duration": time_converter(pytube.YouTube(url=url).length)
                        }
                    )
                )
                voice.play(nextcord.FFmpegPCMAudio(URL_direct, **FFMPEG_OPTS))
            except AttributeError:
                await ctx.send(
                    embed=embed(
                        description="I am not connected to any voice channel.",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        }
                    )
                )

                # things to fix in direct play:
                    #1 {song name} -> remove {}
                    #2 field inline
                    #3 voice.play

def setup(bot: commands.Bot, *args):
    bot.add_cog(Music(bot, *args))