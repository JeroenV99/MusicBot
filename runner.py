#!/usr/bin/env python3
import asyncio
import logging

import uvloop

from core.bot import Bot
from utils.DB import SettingsDB
from utils.magma.core import node

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


def run(bs, **kwargs):
    tasks = (Bot(bs, **kwargs).run(bs.token),)
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == "__main__":
    """
    Replace bot_settings with something such as:

    BotSettings("0", token="NDU5NDIyMjkwNzQ5MTYxNDgz.Dg-7lw.3CCZLueITsh0T_wDfKPKXeBAPUE", prefix=",", ...)

    if you don't have a proper DB set up
    """
    logging.basicConfig(format="%(levelname)s -- %(name)s.%(funcName)s : %(message)s", level=logging.INFO)
    db = SettingsDB.get_instance()
    bot_settings = loop.run_until_complete(db.get_bot_settings())

    node.tries = 1
    node.timeout = 2

    run(bot_settings, loop=loop)

