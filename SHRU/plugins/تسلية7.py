# =============================
# |         SHRU - QHR_1 - ll1ilt           |
# =============================

import os

from telegraph import exceptions, upload_file

from SHRU import Qrh9

from ..core.managers import edit_or_reply
from ..helpers.utils import _cattools, reply_id
from . import convert_toimage, deEmojify, phcomment, threats, trap, trash

plugin_category = "fun"


@Qrh9.ar_cmd(
    pattern="تراش$",
    command=("تراش", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}تراش",
    },
)
async def catbot(event):
    "⌔︙صانع الميمز."
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "᯽︙ قم بالرد على احد الصور")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ عدم الاستطاعة على الاستخراج من الرد الحالي"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "᯽︙ الصورة/الملصق المردود عليه يجب يكون اقل من 5 ميغابايت"
        )
    await event.reply(file=download_location)
    await output[0].edit("᯽︙ جار الصنع..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**⌔︙خطأ: **\n`{str(exc)}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await trash(cat)
    os.remove(download_location)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@Qrh9.ar_cmd(
    pattern="تهديد$",
    command=("تهديد", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}تهديد",
    },
)
async def catbot(event):
    "᯽︙ صانع الميمز."
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "᯽︙ قم بالرد على احد الصور")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ عدم الاستطاعة على الاستخراج من الرد الحالي"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "᯽︙ الصورة/الملصق المردود عليه يجب يكون اقل من 5 ميغابايت"
        )
    await output[0].edit("᯽︙ جار الصنع..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**᯽︙ خطأ: **\n`{str(exc)}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await threats(cat)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@Qrh9.ar_cmd(
    pattern="فخ(?:\s|$)([\s\S]*)",
    command=("فخ", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "Description": "creates a trap card",
        "usage": "{tr}trap (name of the person to trap) ; (trapper name)",
    },
)
async def catbot(event):
    "᯽︙ صانع الميمز."
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        text1, text2 = input_str.split(";")
    else:
        return await edit_or_reply(
            event,
            "⌔︙** يجـب الـرد على صورة او ملصق بـ**\n `.فخ (إسم الضحية);(إسم الفاعل)`",
        )
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "᯽︙ قم بالرد على احد الصور")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ عدم الاستطاعة على الاستخراج من الرد الحالي"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "᯽︙  الصورة/الملصق المردود عليه يجب يكون اقل من 5 ميغابايت "
        )
    await output[0].edit("⌔︙جار الصنع..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**⌔︙خطأ: **\n`{str(exc)}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await trap(text1, text2, cat)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)


@Qrh9.ar_cmd(
    pattern="بورن(?:\s|$)([\s\S]*)",
    command=("بورن", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "description": "pornhub comment creator",
        "usage": "{tr}phub (username);(text in comment)",
    },
)
async def catbot(event):
    "⌔︙جار الصنع.."
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        username, text = input_str.split(";")
    else:
        return await edit_or_reply(
            event,
            "**᯽︙ يجـب الـرد على صورة/ملصق بـ\n `.بورن (المعرف);(النص)`",
        )
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "᯽︙ قم بالرد على احد الصور")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ عدم الاستطاعة على الاستخراج من الرد الحالي"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "᯽︙ الصورة/الملصق المردود عليه يجـب يكون اقل من 5 ميغابايت "
        )

    await output[0].edit("᯽︙ جار الصنع..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**⌔︙خطأ: **\n`{str(exc)}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await phcomment(cat, text, username)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)
