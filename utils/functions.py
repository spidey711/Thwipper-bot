import nextcord
from typing import Union

def dict2fields(d: dict, inline: bool=True):
    # put multiple fields in the embed with a single command
    return [{"name": i, "value": d[i], "inline": inline} for i in d]

def create_embed(
    title=None,
    description=None,
    thumbnail=None,
    url=None,
    color=nextcord.Color.dark_theme(),
    footer=None,
    author: Union[nextcord.Member, bool, dict] = False,
    fields=None,
    image=None,
    button: Union[dict, nextcord.ui.Button] = None,
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
            embed.set_author(name=author.name, icon_url=safe_pfp(author))

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