import nextcord
import time
import pytz
import calendar

from nextcord.ext import commands
from utils.functions import embed
from datetime import datetime
from utils.links import url_dtc

class TimeZone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="datetime", description="See time in a date time")
    async def date_time_ist(self, inter, timezone: str=None):
        if timezone not in pytz.all_timezones:
            await inter.send(
                embed=embed(
                    title="Provide a value",
                    description="Please provide a value for timezone from the list",
                    color=self.bot.color(inter.guild),
                    thumbnail=self.bot.user.avatar,
                    author=inter.user,
                    fields={'It must be': '<t:{}> for you'.format(int(time.time()))}
                )
            )
            return
        tzinfo = pytz.timezone(timezone)
        dt = datetime.now(tzinfo)
        await inter.send(
            embed=embed(
                footer="Timezone: {}".format(timezone),
                fields={
                    'Date': "%s/%s/%s" % (dt.day, dt.month, dt.year),
                    'Time': "%s:%s:%s" % (dt.hour, dt.minute, dt.second)

                },
                color=self.bot.color(inter.guild)
            )
        )

    @date_time_ist.on_autocomplete("timezone")
    async def auto_timezone_complete(self, inter: nextcord.Interaction, timezone):
        await inter.response.send_autocomplete(
            [i for i in pytz.all_timezones if i.lower().startswith(timezone.lower())][:25]
        )

    @nextcord.slash_command(name="calendar", description="Get calendar")
    async def get_calendar(self, inter: nextcord.Interaction, year: int, month: int):
        try:
            e = embed(description="```{}```".format(calendar.month(int(year), int(month))), color=self.bot.color(inter.guild))
            e.set_author(name="Calendar")
            await inter.send(embed=e)
            
        except IndexError:
            e = nextcord.Embed(description="{}, this month doesn't exist 📆".format(inter.user.name), color=self.bot.color(inter.guild))
            e.set_author(name="Calendar", icon_url=url_dtc)
            await inter.send(embed=e)

        

def setup(bot, *args):
    bot.add_cog(TimeZone(bot, *args))