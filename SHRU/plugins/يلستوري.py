#بربك تخمط هيج كود يا فاشل💀
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
import re 
from telethon import events 
from telethon.tl import types
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from ..Config import Config
import json
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
from telethon.tl.functions.channels import JoinChannelRequest
@Qrh9.ar_cmd(pattern=r"قصه$")
async def upload_story(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()


        if reply_msg.media:

            file = helpers._FileStream(reply_msg.media.document, reply_msg.media.document.size)


            story = await event.client.upload_file(file)


            duration = reply_msg.media.document.attributes[0].duration


            description = reply_msg.text if reply_msg.text else "**none**"

            # Edit the message
            await event.edit_or_reply(
                f"**New story uploaded!!**\n"
                f"```\n"
                f"Story length: {duration} seconds\n"
                f"Story id: {story.id}\n"
                f"Story description: {description}\n"
                f"```"
            )
        else:
            await event.edit_or_reply("Please reply to a supported media type (photo, video) to upload as a story.")
    else:
        await event.edit_or_reply("Please reply to a photo or video to upload as a story.")