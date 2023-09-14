# Copyright (C) 2021 SHRU TEAM
# FILES WRITTEN BY  @SX9OO

import requests
from validators.url import url

from SHRU import Qrh9

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"


@Qrh9.ar_cmd(
    pattern="دنس(?:\s|$)([\s\S]*)",
    command=("دنس", plugin_category),
    info={
        "header": "To get Domain Name System(dns) of the given link.",
        "usage": "{tr}dns <url/reply to url>",
        "examples": "{tr}dns google.com",
    },
)
async def _(event):
    "To get Domain Name System(dns) of the given link."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "᯽︙  يجـب عليم الرد على الرابط او وضع الرابط مع الام", 5
        )
    check = url(input_str)
    if not check:
        catstr = "http://" + input_str
        check = url(catstr)
    if not check:
        return await edit_delete(event, "᯽︙  هذا الرابط غير مدعوم", 5)
    sample_url = f"https://da.gd/dns/{input_str}"
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, f"الـ دي أن اس لـ {input_str} هي \n\n{response_api}")
    else:
        await edit_or_reply(
            event, f"᯽︙ - لم استطع ايجاد `{input_str}` في الانترنت"
        )

# urltools for Qrh9 
@Qrh9.ar_cmd(
    pattern="مصغر(?:\s|$)([\s\S]*)",
    command=("مصغر", plugin_category),
    info={
        "header": "To short the given url.",
        "usage": "{tr}short <url/reply to url>",
        "examples": "{tr}short https://github.com/lMl10l1709/catuserbot",
    },
)
async def _(event):
    "shortens the given link"
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "᯽︙  يجـب عليم الرد على الرابط او وضع الرابط مع الامر", 5
        )
    check = url(input_str)
    if not check:
        catstr = f"http://" + input_str
        check = url(catstr)
    if not check:
        return await edit_delete(event, "᯽︙  هذا الرابط غير مدعوم", 5)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    sample_url = f"https://da.gd/s?url={input_str}"
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, f"᯽︙ تـم صنـع رابـط مصغر: {response_api}", link_preview=False
        )
    else:
        await edit_or_reply(event, "᯽︙  هـنالك شي خطـا حاول لاحقـا")

# urltools for Qrh9
  
@Qrh9.ar_cmd(
    pattern="اخفاء(?:\s|$)([\s\S]*)",
    command=("اخفاء", plugin_category),
    info={
        "header": "To hide the url with white spaces using hyperlink.",
        "usage": "{tr}hl <url/reply to url>",
        "examples": "{tr}hl https://da.gd/rm6qri",
    },
)
async def _(event):
    "To hide the url with white spaces using hyperlink."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "᯽︙  يجـب عليم الرد على الرابط او وضع الرابط مع الامر", 5
        )
    check = url(input_str)
    if not check:
        catstr = "http://" + input_str
        check = url(catstr)
    if not check:
        return await edit_delete(event, "᯽︙  هذا الرابط غير مدعوم", 5)
    await edit_or_reply(event, "[ㅤㅤㅤㅤㅤㅤㅤ](" + input_str + ")")
