import nextcord
import os

from utils.Storage import Variables
from nextcord.ext import commands
from utils.functions import (
    CONTEXT,
    INTERACTION, 
    get_async, 
    convert_to_url,
    embed,
    dict2str
)


class PERMANENT_CACHE:
    def __init__(self):
        self.CACHE_ = {
            "chem": {},
            "imdb": {}
        }        
        self.var = Variables("cogs/__pycache__/APIcache")
        if self.var.show_data():            
            self.CACHE_ = self.var.show_data()
        else:
            self.var.pass_all(**self.CACHE_)
            self.var.save()

    async def cache_request(self, command: str, keyword: str, *args, **kwargs):
        if keyword not in self.CACHE_[command]:
            self.CACHE_[command][keyword] = await get_async(*args, **kwargs)
        self.var.pass_all(
            **self.CACHE_
        )
        self.var.save()
        return self.CACHE_[command][keyword]

class API(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cache = PERMANENT_CACHE()

    @nextcord.slash_command(name="api")
    async def api(self, inter: INTERACTION):
        print(inter.user)

    @api.subcommand(name="chemistry", description="Search for periodic table")
    async def chem(self, inter: INTERACTION, element: str = "Hydrogen"):
        await inter.response.defer()
        RAW = await self.cache.cache_request(
            "chem", 
            element,
            "https://api.popcat.xyz/periodic-table?element={}".format(convert_to_url(element)),
            kind="json"
        )

        if "error" in RAW:
            await inter.send(
                embed=embed(
                    title="Error",
                    color=self.bot.color(inter.guild),
                    description=RAW["error"],
                    thumbnail=self.bot.user.avatar,
                    author=inter.user,
                    footer={
                        'text': 'Something seems wrong',
                        'icon_url': self.bot.user.avatar
                    }
                )
            )
            return 
        f = await get_async(
            RAW.get("image"), kind="fp"
        )
        await inter.send(
            embed=embed(
                title="{} [ {} ]".format(RAW.get("name"), RAW.get("symbol")),
                description=RAW.get("summary"),
                thumbnail="attachment://thumbnail.png",
                fields={
                    'Properties': dict2str({
                        'Phase': RAW.get("phase"),
                        'Atomic Number': RAW.get("atomic_number"),
                        'Atomic Mass': RAW.get("atomic_mass"),
                        'Period': RAW.get("period"),
                        'Symbol': RAW.get("name")
                    })
                }
            ),
            file=nextcord.File(fp=f, filename="thumbnail.png")
        )

    @api.subcommand(name="imdb", description="Get IMDB movie")
    async def imdb(self, inter: INTERACTION, movie: str):
        await inter.response.defer()
        
        
def setup(bot: commands.Bot, *args):
    bot.add_cog(API(bot, *args))
