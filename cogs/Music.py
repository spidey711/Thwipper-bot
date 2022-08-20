# This file contains all music functions.

import nextcord
import random

from utils.responses import connections, disconnections
from utils.functions import embed
from utils.links import url_author_music
from nextcord.ext import commands

class Music(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
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
                except AttributeError as ae:
                    await ctx.send(
                        embed=embed(
                            description=f"I am not connected to any voice channel.\n{ae}",
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


def setup(bot: commands.Bot, *args):
    bot.add_cog(Music(bot, *args))