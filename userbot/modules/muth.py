# ported from X-TRA-TELEGRAM by @RoyalBoyPriyanshu

import random, re
import asyncio
from telethon import events
from userbot.events import register
from asyncio import sleep
import time
from userbot import CMD_HELP


@register(pattern=".muth")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 100)

    #input_str = event.pattern_match.group(1)

    #if input_str == "muth":

    await event.edit("Starting")

    animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

    for i in animation_ttl:
        
        await asyncio.sleep(animation_interval)
        
        await event.edit(animation_chars[i % 100])

CMD_HELP.update({
  "muth":
   "`.muth`\
\nUsage: Find yourself."
})            
