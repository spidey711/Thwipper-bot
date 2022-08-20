# This file contains functions which will be used in a lot of other files.

import nextcord
import aiohttp
import aiofiles
import urllib

from nextcord.ext import commands
from typing import List, Union
from nextcord.ui import button, View
from io import BytesIO

CONTEXT = commands.context.Context
INTERACTION = nextcord.Interaction

def convert_to_url(name: str):
    name = urllib.parse.quote(name)
    return name

def dict2fields(d: dict, inline: bool=True):
    # put multiple fields in the embed with a single command
    return [{"name": i, "value": d[i], "inline": inline} for i in d]

def dict2str(d: dict, sep_symbol: str = ":"):
    return "\n".join(["`{}`{} {}".format(i, sep_symbol, j) for i, j in d.items()])

def embed(
    title=None,
    description=None,
    thumbnail=None,
    url=None,
    color=nextcord.Color.dark_theme(),
    footer=None,
    author: Union[nextcord.Member, bool, dict] = False,
    fields=None,
    image=None, 
    button: List[Union[dict, nextcord.ui.Button]] = None,
    **kwargs,
) -> nextcord.Embed:
    embed = nextcord.Embed()
    if color != nextcord.Color.dark_theme():
        if type(color) == int:
            embed = nextcord.Embed(color=nextcord.Color(value=color))
        else:
            embed = nextcord.Embed(color=color)
    if title:
        embed.title = title
        
    if description:
        embed.description = description

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    if image:
        embed.set_image(url=image)

    if url:
        embed.url = url

    if fields:
        if isinstance(fields, dict):
            fields = dict2fields(fields, inline=False)
        for i in fields:
            embed.add_field(**i)

    if footer:
        if isinstance(footer, str):
            embed.set_footer(text=footer)
        else:
            embed.set_footer(
                text=footer.get("text", "Footer Error"),
                icon_url=footer.get("icon_url", "https://toppng.com/uploads/preview/red-question-mark-png-11552242986dielb7cmf4.png"))

    if author:
        if isinstance(author, str):
            embed.set_author(name=author)
        elif isinstance(author, dict):
            embed.set_author(**author)
        elif isinstance(author, (nextcord.member.Member, nextcord.user.ClientUser)):
            embed.set_author(name=author.name, icon_url=author.avatar)

    if button:
        view = nextcord.ui.View(timeout=None)
        if isinstance(button, (nextcord.ui.Button, dict)):
            button = [button]
        for i in button[:5]:
            b = i
            if isinstance(b, dict):
                b = nextcord.ui.Button(
                    label=b.get("label", "Link"),
                    emoji=b.get("emoji", "🔗"),
                    url=b.get("url"),
                )
            view.add_item(b)
        return embed, view
    return embed

class ButtonPages(View):
    style=nextcord.ButtonStyle.red

    def __init__(self, main: Union[CONTEXT, INTERACTION], pages: List[nextcord.Embed], start = 0):
        super().__init__(timeout=None)
        self.PAGES = pages
        self.main = main
        self.author = getattr(self.main, 'author', getattr(self.main, 'user', None))
        self.current = start
        if self.current>=len(pages):
            self.current = 0

    async def edit_page(self, inter: INTERACTION):
        page = self.PAGES[self.current]
        await inter.edit(embed=page)

    def author_check(self, inter: INTERACTION):
        if self.author.id == inter.user.id:
            return True
        return False

    @button(label="Previous", style=style) # emoji="⬅️"
    async def previous(self, _, inter: INTERACTION):
        if self.current - 1 >= 0 and self.author_check(inter):
            self.current -= 1
            await self.edit_page(inter)

    @button(label="Next", style=style) # emoji="➡️"
    async def next(self, _, inter: INTERACTION):
        if self.current + 1 < len(self.PAGES) and self.author_check(inter):
            self.current += 1
            await self.edit_page(inter)    

async def pages(main: Union[CONTEXT, INTERACTION], pages: List[nextcord.Embed], start: int = 0):
    if start >= len(pages): start = 0
    await main.send(
        embed=pages[start],
        view=ButtonPages(main, pages, start)
    )

async def get_async(url: str, headers: dict = {}, kind: str = "content"):
    """
    Simple Async get request
    """
    output = ""
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            if kind == "json":
                try:
                    output = await resp.json()
                except Exception as e:
                    print(e)
                    output = await resp.text()
            elif kind.startswith("file>"):
                f = await aiofiles.open(kind[5:], mode="wb")
                await f.write(await resp.read())
                await f.close()
                return
            elif kind == "fp":
                output = BytesIO(await resp.read())
            else:
                output = await resp.text()

        await session.close()
    return output


async def post_async(api: str, header: dict = {}, json: dict = {}):
    async with aiohttp.ClientSession() as session:
        async with session.post(api, headers=header, json=json) as resp:
            if resp.headers["Content-Type"] != "application/json":
                return await resp.read()
            return await resp.json()