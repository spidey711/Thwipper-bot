import nextcord

from nextcord.ext import commands
from utils.functions import embed, pages

# Cog description
COG_CODE = """
```py
# This is how you create a basic cog
# Import essential packages
import nextcord
from nextcord.ext import commands
from utils.functions import embed, pages

# We're going to subclass commands.Cog and create __init__ function for this new subclasses class
# When I do `var: int`, it is called typing, but it doesn't necessarily follow in Python, but it helps in autocomplete
# For `var: int`, the variable 'var' will be an integer
class CogName(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot #initialising bot, also will have some vairables and functions that are useful

    @nextcord.slash_command(name="slash")
    async def slash(self, inter, arg1, arg2):
        # Bot is thinking... <- this is called defer
        await inter.response.defer()
        await inter.send("Message") #send message

```
The use of `inter` and slash command will be explained in `/learn slash`
"""

# Slash description
SLASH_CODE = """
Basic structure of a slash command in a cog is:
```py
@nextcord.slash_command(name="name", description="Some description")
async def slash(self, inter, arg1, arg2, arg3):
    await inter.response.defer()
    # Defer gives the bot time to think for 15 minutes, without defer, it is 3 seconds
    await inter.response.send_message("text", ephemeral=True)
    # Sending ephemeral message, only user can see
```
"""

class Learn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="learn")
    async def learn(self, inter):
        print(inter.user)

    @learn.subcommand(name="cogs", description="Learn about cogs in Thwipper")
    async def cogs_learn(self, inter):
        await inter.response.defer()
        e, view = embed(
            title="Cogs",
            author=self.bot.user,
            color=self.bot.color(inter.guild),
            footer={
                'text': 'This command may only be temporary',
                'icon_url': self.bot.user.avatar
            },

            description=COG_CODE,
            fields={
                'Nextcord': 'We use nextcord to write for our bots, it is a fork of `Danny\'s discord.py`.'
            },
            thumbnail=self.bot.user.avatar,
            button=nextcord.ui.Button(
                url="https://github.com/nextcord/nextcord/blob/master/examples/application_commands/cog_example.py",
                label="Go and check the docs",
                emoji="📜"
            )
        )
        await inter.send(
            embed=e, view=view
        )

    @learn.subcommand(name="slash", description="Learn about slash command in Thwipper")
    async def slash_learn(self, inter):
        e, view = embed(
            button=[
                nextcord.ui.Button(
                    url="https://github.com/nextcord/nextcord/blob/master/examples/application_commands/slash_command.py",
                    label="Slash Command"
                ),
                nextcord.ui.Button(
                    url="https://github.com/nextcord/nextcord/blob/master/examples/application_commands/sub_commands.py",
                    label="Slash Subcommand"
                )
            ],
            description=SLASH_CODE,
            title="Slash command",
            color=self.bot.color(inter.guild),
            author=self.bot.user,
            footer={
                'text': 'This command may only be temporary',
                'icon_url': self.bot.user.avatar
            }
        )
        await inter.send(
            embed=e, view=view
        )
        

def setup(bot: commands.Bot, *args):
    bot.add_cog(Learn(bot, *args))