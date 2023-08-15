from .schedubuddy import setup_schedule_buddy
from .kattis import setup_kattis
from .misc import setup_misc_cog
from .snipe import setup_snipe
from .course_info import setup_course_info

import asyncio
from aiohttp import ClientSession


async def setup_all_cogs(bot, guilds, client=None):
    if not client:
        client = ClientSession()
    asyncio.gather(
        setup_schedule_buddy(bot, guilds, client),
        setup_kattis(bot, guilds),
        setup_misc_cog(bot, guilds),
        setup_snipe(bot, guilds, client),
        setup_course_info(bot, guilds),
    )