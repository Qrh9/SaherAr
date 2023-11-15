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
from SHRU import Qrh9

@Qrh9.ar_cmd(pattern="^.قصه$")
async def upload_story(event):
    """Uploads a photo or video as a story."""

    reply_message = await event.get_reply_message()

    if not reply_message:
        await event.reply("Please reply to a photo or video to upload it as a story.")
        return

    media = reply_message.media

    if not media:
        await event.reply("Please reply to a photo or video to upload it as a story.")
        return

    if media.photo:
        story_caption = reply_message.text or "No caption provided"
        story = await event.client.upload_story(media.photo, caption=story_caption)
    elif media.video:
        story_caption = reply_message.text or "No caption provided"
        story = await event.client.upload_story(media.video, caption=story_caption)
    else:
        await event.reply("Please reply to a photo or video to upload it as a story.")
        return

    story_length = str(story.duration) + " seconds" if story.video else "N/A"

    story_info = f"""
**Story Upload Successful**

Story length: {story_length}
Story ID: {story.id}
Story description: {story_caption}
"""

    await event.edit(story_info)
