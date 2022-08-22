# This file contains all music functions.

import nextcord
import random
import urllib
import regex

from utils.responses import connections, disconnections
from utils.functions import CONTEXT, convert_to_url, embed, Music as msc, get_async, time_converter
from utils.links import url_author_music
from nextcord.ext import commands

class Music(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.msc = msc(self.bot) 
    
        
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
            if self.msc.checkvoice(ctx):
                voice_client = ctx.guild.voice_client  
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
    async def play_music(self, ctx: CONTEXT, *, char):

        user: nextcord.Member = getattr(ctx, 'author', getattr(ctx, 'user', None))
        if (not ctx.guild.voice_client) and user.voice and user.voice.channel:
            await self.join_vc(ctx)
        
        if self.msc.checkvoice(ctx):
            # web scrape
            try:
                voice = ctx.guild.voice_client
                markup = await get_async(
                    "https://www.youtube.com/results?search_query={}".format(convert_to_url(char))
                )
                vid = regex.findall(r"watch\?v=(\S{11})", markup)
                url = "https://www.youtube.com/watch?v=" + vid[0]
                INFO = self.msc.info(url=url)
                URL_direct = self.msc.download(INFO)

                if not ctx.guild.voice_client.is_playing(): 
                    voice.stop()
        
                await ctx.send(
                    embed=embed(
                        description=f"**Now playing: **{INFO.get('title')}",
                        color=self.bot.color(ctx.guild),
                        author={
                            "name": "Spider-Punk Radio™",
                            "icon_url": url_author_music
                        },
                        thumbnail=INFO.get("thumbnail", None),
                        fields={
                            "Uploader": INFO.get("uploader", "Unavailable"),
                            "Duration": time_converter(INFO.get("duration", 10))
                        }
                    )
                )
                self.msc.play(voice, URL=URL_direct)
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