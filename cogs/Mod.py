import nextcord
from utils.functions import embed, pages
from nextcord.ext import commands

class Mod(commands.Cog):
    CONTEXT = commands.context.Context
    MESSAGE = nextcord.message.Message

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        self.DELETED_MESSAGE: dict = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message: MESSAGE):
        if not message.author.bot:
            if self.DELETED_MESSAGE.get(message.channel.id, False):
                self.DELETED_MESSAGE[message.channel.id].append((message.author, message.content))                
            else:
                self.DELETED_MESSAGE[message.channel.id] = [(message.author, message.content)]

    @commands.command(aliases=["delete", "del"])
    async def clear(self, ctx: CONTEXT, num: int = 10):
        await ctx.message.delete()
        await ctx.channel.purge(limit=num)

    @commands.command()
    async def snipe(self, ctx: CONTEXT):
        l = self.DELETED_MESSAGE.get(ctx.channel.id)
        if not l:
            await ctx.send(
                embed=embed(
                    title="I see nothing",
                    description="I do not see any deleted messages here, if you're expecting a deleted message from a bot....",
                    image="https://c.tenor.com/fBvQV_5Lp6UAAAAC/we-dont-do-that-here-black-panther.gif",
                    color=self.bot.color(ctx.guild),
                    footer={
                        'text': 'We also have another issue where the bot could restart, Since we\'re not allowed to keep messages permanently, we will have to clear it everyonce in a while',
                        'icon_url': self.bot.user.avatar,
                    },
                    author=getattr(ctx, 'author', getattr(ctx, 'user', None))
                )
            )
            return
        fields, count, embeds = [dict()], 0, []
        for user, message in l:
            if count%5==0:
                fields.append({})
            fields[-1].update({str(user): message[:250]})
        frame_embed = lambda field: embed(
            title="Snipe",
            description="All of this will be deleted if the bot restarts",
            footer={
                'text': 'Snipe',
                'icon_url': self.bot.user.avatar,
            },
            author=getattr(ctx, 'author', getattr(ctx, 'user', None)),
            color=self.bot.color(ctx.guild),
            fields = field
        )
        embeds = [frame_embed(i) for i in fields]
        await pages(ctx, embeds, start = 0)

def setup(bot, *args):
    bot.add_cog(Mod(bot, *args))