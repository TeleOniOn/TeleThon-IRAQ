"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No Name set yet. [TeleOniOn.](t.me/TeleOniOn)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("➥• 🏷 TeleThon \n"
                     "➥•🔰  Version: 1.0.0\n"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "➥•🔅  Created By: [CH TeleOniOn](https://t.me/OniOn_bbot) || [CH IQ](https://t.me/TeleOniOn)\n"
                     "➥•🤖 BOT ORDERS @OniOn_bbot\n"
                     "➥• 🗂 The Files : [Here](https://t.me/YZZZY)\n"
                     "➥• Source link ♻️ : [Here](https://heroku.com/deploy?template=https://github.com/TeleOniOn/TeleThon-IRAQ)\n"
                    f"➥•🥳 My Master : {DEFAULTUSER}\n")
