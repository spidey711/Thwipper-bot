import nextcord

from utils.functions import (
    CONTEXT,
    INTERACTION, 
    get_async, 
    convert_to_url,
    embed,
    dict2str
)
from nextcord.ext import commands

class API(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.CACHE_ = {
            "chem": {}
        }

    @nextcord.slash_command(name="api")
    async def api(self, inter: INTERACTION):
        print(inter.user)

    @api.subcommand(name="chemistry", description="Search for periodic table")
    async def chem(self, inter: INTERACTION, element: str = "Hydrogen"):
        await inter.response.defer()
        if element not in self.CACHE_["chem"]:
            RAW = await get_async(
                "https://api.popcat.xyz/periodic-table?element={}".format(convert_to_url(element)),
                kind="json"
            )
            self.CACHE_["chem"][element] = RAW
        else:
            RAW = self.CACHE_["chem"][element]

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
        
def setup(bot: commands.Bot, *args):
    bot.add_cog(API(bot, *args))
