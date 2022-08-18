# This file contains functions built for moderators (more or less).

import nextcord
from utils.functions import embed, pages
from nextcord.ext import commands

class Mod(commands.Cog):
    CONTEXT = commands.context.Context
    MESSAGE = nextcord.message.Message
    INTERACTION = nextcord.Interaction

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        self.DELETED_MESSAGE: dict = {}


    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        for message in messages:
            await self.on_message_delete(message)


    @commands.Cog.listener()
    async def on_message_delete(self, message: MESSAGE):
        if not message.author.bot:
            if self.DELETED_MESSAGE.get(message.channel.id, False):
                self.DELETED_MESSAGE[message.channel.id].append((str(message.author), message.content))                
            else:
                self.DELETED_MESSAGE[message.channel.id] = [(str(message.author), message.content)]


    @commands.command(aliases=["delete", "del"])
    async def clear(self, ctx: CONTEXT, num: int = 10):
        await ctx.message.delete()
        await ctx.channel.purge(limit=num)


    @commands.command(aliases=["[x]"], description="Stop bot.")
    async def stop_bot(self, ctx):
        exit()


    @commands.command(aliases=["web", "snipe"], description="Get deleted messages.")
    async def snipe_messages(self, ctx: CONTEXT):
        l = self.DELETED_MESSAGE.get(ctx.channel.id)
        if not l:
            await ctx.send(
                embed=embed(
                    title="No messages found",
                    description="No one's regretted what they have typed and sent so far 🤔",
                    color=self.bot.color(ctx.guild),
                    footer={
                        "text": "Deleted messages will be cleared from time to time 🕸️",
                        "icon_url": self.bot.user.avatar
                    },
                    author=getattr(ctx, 'author', getattr(ctx, 'user', None))
                )
            )
            return
        fields, count, embeds = [[]], 0, []
        for user, message in l:
            if count % 5 == 0 and count:
                fields.append([])
            fields[-1].append(
                {
                    'name': user,
                    'value': message[:250],
                    'inline': False
                }
            )
            count+=1
        frame_embed = lambda field: embed(
            title="Thwip! 🕸️",
            # author=getattr(ctx, 'author', getattr(ctx, 'user', None)),
            color=self.bot.color(ctx.guild),
            footer="Catch the thieves, just like flies, look out! 😎",
            fields = field
        )
        embeds = [frame_embed(i) for i in fields]
        await pages(ctx, embeds, start = 0)

    
    @nextcord.slash_command(name="color", description="Set your color")
    async def color(self, inter: INTERACTION, color: str = None):
        if not (color.startswith("0x") or color.startswith("#")):
            await inter.response.send_message(
                "Sorry, I only support hex code, start with `0x` or `#`",
                ephemeral=True
            )
            return
        if color is None:
            await inter.response.send_message(
                "Current color is {}".format(hex(self.bot.color(inter.guild))),
                ephemeral=True
            )
            return
        color = int(color.replace("#", "0x"), base=16)
        self.bot.config_color[inter.guild.id] = color
        await inter.send(
            embed=embed(
                title="Done",
                description="Set server color as {}".format(hex(self.bot.color(inter.guild))),
                color=color,
                thumbnail=getattr(inter.guild, "icon"),
                author=inter.user,
            )
        )

def setup(bot, *args):
    bot.add_cog(Mod(bot, *args))