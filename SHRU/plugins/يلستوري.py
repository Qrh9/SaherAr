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

from telethon import events

from telethon import events

@Qrh9.ar_cmd(pattern=r"uplod$")
async def upload_story(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()

        # Check if the replied message contains media
        if reply_msg.media:
            # Upload the media as a story
            story = await event.client.upload_file(reply_msg.media)

            # Get story duration
            duration = reply_msg.media.document.attributes[0].duration

            # Get story description if there's text
            description = reply_msg.text if reply_msg.text else "**none**"

            # Edit the message
            await event.edit(
                f"**New story uploaded!!**\n"
                f"```\n"
                f"Story length: {duration} seconds\n"
                f"Story id: {story.id}\n"
                f"Story description: {description}\n"
                f"```"
            )
        else:
            await event.edit("Please reply to a photo or video to upload as a story.")
    else:
        await event.edit("Please reply to a photo or video to upload as a story.")
