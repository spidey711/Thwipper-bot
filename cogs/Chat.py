# This file contains greet functions and possible chatbot implementation.

import nextcord
import random

from nextcord.ext import commands
from utils.functions import dict2str, embed
from utils.links import hello_urls
from utils.responses import greetings

class Chat(commands.Cog):
    CONTEXT = commands.context.Context
    MESSAGE = nextcord.message.Message
    INTERACTION = nextcord.Interaction
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(aliases=["hi", "hello", "hey", "hola"], description="Simply greets members of a server.")
    async def greet_member(self, ctx):
        await ctx.send(
            embed=embed(
                author={
                    "name": f"Hey {ctx.author.name}!",
                    "icon_url": ctx.author.avatar       
                },
                color=self.bot.color(ctx.guild),
                image=random.choice(hello_urls),
                footer={
                    "text": random.choice(greetings),
                    "icon_url": self.bot.user.avatar
                }
            )
        )
        
    
def setup(bot, *args):
    bot.add_cog(Chat(bot, *args))