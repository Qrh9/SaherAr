# Copyright (C) 2021 SHRU TEAM
# FILES WRITTEN BY  @ll1ilt
import os
import re

from telethon import Button

from ..Config import Config
from . import Qrh9, edit_delete, reply_id

plugin_category = "tools"
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")

@Qrh9.ar_cmd(pattern="لستة$")
async def _(event):
    "To create button posts via inline"
    reply_to_id = await reply_id(event)
    # soon will try to add media support
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "᯽︙ يجب عليك وضع مسافـة لاستخدامها مع الامر ")
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
