#Fixes by Reda 
#Made by hussein
#-------------
import asyncio
import base64
import io
import math
import os
import random
import re
import string
import urllib.request
from os import remove
import cloudscraper
import emoji as catemoji
from bs4 import BeautifulSoup as bs
from PIL import Image
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.stickers import SuggestShortNameRequest
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.utils import get_input_document
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputStickerSetID,
    MessageMediaPhoto,
)

from SHRU import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import animator, crop_and_divide
from ..helpers.tools import media_type
from ..helpers.utils import _cattools
from ..sql_helper.globals import gvarstatus

plugin_category = "fun"

# modified and developed by @mrconfused , @jisan7509


combot_stickers_url = "https://combot.org/telegram/stickers?q="

EMOJI_SEN = [
    "Можно отправить несколько смайлов в одном сообщении, однако мы рекомендуем использовать не больше одного или двух на каждый стикер.",
    "You can list several emoji in one message, but I recommend using no more than two per sticker",
    "يمكنك إرسال قائمة بعدة رموز في رسالة واحدة، لكن أنصحك بعدم إرسال أكثر من رمزين للملصق الواحد.",
    "Du kannst auch mehrere Emoji eingeben, ich empfehle dir aber nicht mehr als zwei pro Sticker zu benutzen.",
    "Você pode listar vários emojis em uma mensagem, mas recomendo não usar mais do que dois por cada sticker.",
    "Puoi elencare diverse emoji in un singolo messaggio, ma ti consiglio di non usarne più di due per sticker.",
    "emoji",
]

KANGING_STR = [
    " ᯽︙ انتظر يتم صنع الملصق ",
]


def verify_cond(catarray, text):
    return any(i in text for i in catarray)


def pack_name(userid, pack, is_anim, is_video):
    if is_anim:
        return f"HuRe_{userid}_{pack}_anim"
    elif is_video:
        return f"HuRe_{userid}_{pack}_vid"
    return f"HuRe_{userid}_{pack}"


def char_is_emoji(character):
    return character in catemoji.UNICODE_EMOJI["en"]


def pack_nick(username, pack, is_anim, is_video):
    if gvarstatus("CUSTOM_STICKER_PACKNAME"):
        if is_anim:
            return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} حقوق.{pack} "
        elif is_video:
            return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} حقوق. {pack} "
        return f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} حقوق.{pack}"

    if is_anim:
        return f"@{username} {pack} "
    elif is_video:
        return f"@{username} {pack} "
    else:
        return f"@{username} {pack}"


async def delpack(catevent, conv, cmd, args, packname):
    try:
        await conv.send_message(cmd)
    except YouBlockedUserError:
        await catevent.edit("لقد قمت بحظر البوت @stickers . قم بألغاء الحظر عن البوت.")
        return None, None
    await conv.send_message("/delpack")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("Yes, I am totally sure.")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)


async def resize_photo(photo):
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        maxsize = (512, 512)
        image.thumbnail(maxsize)
    return image


async def newpacksticker(
    catevent,
    conv,
    cmd,
    args,
    pack,
    packnick,
    is_video,
    emoji,
    packname,
    is_anim,
    stfile,
    otherpack=False,
    pkang=False,
):
    try:
        await conv.send_message(cmd)
    except YouBlockedUserError:
        await catevent.edit("لقد قمت بحظر البوت @stickers قم بفك الحظر وحاول مره اخرى.")
        if not pkang:
            return None, None, None
        return None, None
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packnick)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if is_video:
        await conv.send_file("animate.webm")
    elif is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        os.remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    asyncio.sleep(1)
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/publish")
    if is_anim:
        await conv.get_response()
        await conv.send_message(f"<{packnick}>")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("/skip")
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message(packname)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return otherpack, packname, emoji
    return pack, packname


async def add_to_pack(
    catevent,
    conv,
    args,
    packname,
    pack,
    userid,
    username,
    is_video,
    is_anim,
    stfile,
    emoji,
    cmd,
    pkang=False,
):
    try:
        await conv.send_message("/addsticker")
    except YouBlockedUserError:
        await catevent.edit("لقد قمت بحظر البوت @stickers bot. قم بفك الحظر عنه واعد المحاولة.")
        if not pkang:
            return None, None
        return None, None
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    x = await conv.get_response()
    while ("50" in x.text) or ("120" in x.text):
        try:
            val = int(pack)
            pack = val + 1
        except ValueError:
            pack = 1
        packname = pack_name(userid, pack, is_anim, is_video)
        packnick = pack_nick(username, pack, is_anim, is_video)
        await catevent.edit(f"`تبديل الحزمه الى {pack} بسبب امتلائها`")
        await conv.send_message(packname)
        x = await conv.get_response()
        if x.text == "الحزمة المحددة غير صحيحه.":
            return await newpacksticker(
                catevent,
                conv,
                cmd,
                args,
                pack,
                packnick,
                is_video,
                emoji,
                packname,
                is_anim,
                stfile,
                otherpack=True,
                pkang=pkang,
            )
    if is_video:
        await conv.send_file("animate.webm")
        os.remove("animate.webm")
    elif is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        os.remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/done")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return packname, emoji
    return pack, packname


@l313l.ar_cmd(
    pattern="ملصق(?:\s|$)([\s\S]*)",
    command=("ملصق", plugin_category),
    info={
        "header": "To kang a sticker.",
        "description": "Kang's the sticker/image/video/gif/webm file to the specified pack and uses the emoji('s) you picked",
        "usage": "{tr}kang [emoji('s)] [number]",
    },
)
async def kang(args):  # sourcery no-metrics
    "To kang a sticker."
    photo = None
    emojibypass = False
    is_anim = False
    is_video = False
    emoji = None
    message = await args.get_reply_message()
    user = await args.client.get_me()
    if not user.username:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"HuRe_{user.id}"
    else:
        username = user.username
    userid = user.id
    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            photo = await args.client.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            await args.client.download_media(message.media.document, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.media.document.attributes
            ):
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            await args.client.download_media(
                message.media.document, "AnimatedSticker.tgs"
            )
            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            emojibypass = True
            is_anim = True
            photo = 1
        elif message.media.document.mime_type in ["video/mp4", "video/webm"]:
            emojibypass = False
            is_video = True
            photo = 1
            if message.media.document.mime_type == "video/webm":
                attributes = message.media.document.attributes
                for attribute in attributes:
                    if isinstance(attribute, DocumentAttributeSticker):
                        if message.media.document.size / 1024 > 255:
                            catevent = await edit_or_reply(
                                args, "__⌛ File size big,,, Downloading..__"
                            )
                            sticker = await animator(message, args, catevent)
                            await edit_or_reply(
                                catevent, f"`{random.choice(KANGING_STR)}`"
                            )
                        else:
                            catevent = await edit_or_reply(
                                args, f"`{random.choice(KANGING_STR)}`"
                            )
                            sticker = await args.client.download_media(
                                message.media.document, "animate.webm"
                            )
                        emoji = attribute.alt
                        emojibypass = True
            else:
                catevent = await edit_or_reply(args, "__⌛ جارِ التحميل عزيزي..__")
                sticker = await animator(message, args, catevent)
                await edit_or_reply(catevent, f"`{random.choice(KANGING_STR)}`")
        else:
            await edit_delete(args, "`الملف غير مدعوم!`")
            return
    else:
        await edit_delete(args, "`لا يمكنني اخذ هذا الملصق...`")
        return
    if photo:
        splat = ("".join(args.text.split(maxsplit=1)[1:])).split()
        emoji = emoji if emojibypass else "😂"
        pack = 1
        if len(splat) == 2:
            if char_is_emoji(splat[0][0]):
                if char_is_emoji(splat[1][0]):
                    return await catevent.edit("check `.info stickers`")
                pack = splat[1]  # User sent both
                emoji = splat[0]
            elif char_is_emoji(splat[1][0]):
                pack = splat[0]  # User sent both
                emoji = splat[1]
            else:
                return await catevent.edit("check `.info stickers`")
        elif len(splat) == 1:
            if char_is_emoji(splat[0][0]):
                emoji = splat[0]
            else:
                pack = splat[0]
        packname = pack_name(userid, pack, is_anim, is_video)
        packnick = pack_nick(username, pack, is_anim, is_video)
        cmd = "/newpack"
        stfile = io.BytesIO()
        if is_video:
            cmd = "/newvideo"
        elif is_anim:
            cmd = "/newanimated"
        else:
            image = await resize_photo(photo)
            stfile.name = "sticker.png"
            image.save(stfile, "PNG")
        response = urllib.request.urlopen(
            urllib.request.Request(f"http://t.me/addstickers/{packname}")
        )
        htmlstr = response.read().decode("utf8").split("\n")
        if (
            "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
            not in htmlstr
        ):
            async with args.client.conversation("@Stickers") as conv:
                packname, emoji = await add_to_pack(
                    catevent,
                    conv,
                    args,
                    packname,
                    pack,
                    userid,
                    username,
                    is_video,
                    is_anim,
                    stfile,
                    emoji,
                    cmd,
                )
            if packname is None:
                return
            await catevent.edit(
                f"`تم اخذ الملصق بنجاح!\
                    \nهذه هي الحزمه الخاصه بك` [هنا](t.me/addstickers/{packname}) `والايموجي الخاص بلملصق هو {emoji}`",
                parse_mode="md"
            )
        else:
            await catevent.edit("`جارِ انشاء حزمة جديد ياورده...`")
            async with args.client.conversation("@Stickers") as conv:
                otherpack, packname, emoji = await newpacksticker(
                    catevent,
                    conv,
                    cmd,
                    args,
                    pack,
                    packnick,
                    is_video,
                    emoji,
                    packname,
                    is_anim,
                    stfile,
                )
            if is_video and os.path.exists(sticker):
                os.remove(sticker)
            if otherpack is None:
                return
            if otherpack:
                await edit_delete(
                    catevent,
                    f"`تم اخذ الملصق بنجاح !\
                    \nوهاي الحزمه مالتك` [here](t.me/addstickers/{packname}) `وهذا الايموجي مال الملصق {emoji}`",
                    parse_mode="md",
                    time=10,
                )
            else:
                await edit_delete(
                    catevent,
                    f"`تم اخذ الملصق مثل الورد!\
                    \nوهاي الحزمه مالتك` [here](t.me/addstickers/{packname}) `وهذا الايموجي مال الملصق {emoji}`",
                    parse_mode="md",
                    time=10,
                )


@l313l.on(admin_cmd(pattern="حزمة"))
async def HuRepkg(_):
    Jep = await _.get_reply_message()
    if not Jep:
        return await edit_or_reply(_, "**- يجب عليك الرد على حزمة.**")
    if len(_.text) <= 9:
        return await edit_or_reply(_, "**- يجب عليك وضع اسم الحزمة مع الأمر.**")
    if len(_.text) > 9:
        _packname = _.text.split(" ", maxsplit=1)[1]
    else:
        _packname = f"{_.sender_id}"
    _id = Jep.media.document.attributes[1].stickerset.id
    _hash = Jep.media.document.attributes[1].stickerset.access_hash
    _get_stiks = await _.client(functions.messages.GetStickerSetRequest(types.InputStickerSetID(id=_id, access_hash=_hash), hash=0))
    stiks = []
    for i in _get_stiks.documents:
        mul = get_input_document(i)
        stiks.append(
            types.InputStickerSetItem(
                document=mul,
                emoji=(i.attributes[1]).alt,
            )
        )
    try:
        short_name = (await _.client(SuggestShortNameRequest(_packname))).short_name
        HuRe_Jep = await bot(
            functions.stickers.CreateStickerSetRequest(
                user_id=_.sender_id,
                title=_packname,
                short_name=f"u{short_name}_by_{bot.me.username}",
                stickers=stiks,
            )
        )
    except BaseException as er:
        LOGS.exception(er)
        return await edit_or_reply(_, str(er))
    await edit_or_reply(
        _, f"**- تم اخذ الحزمة بنجاح ✓ \nالحزمة  → [اضغط هنا](https://t.me/addstickers/{HuRe_Jep.set.short_name})**")

@l313l.on(admin_cmd(pattern="حزمه"))
async def HuRepkg(_):
    Jep = await _.get_reply_message()
    if not Jep:
        return await edit_or_reply(_, "**- يجب عليك الرد على حزمة.**")
    _stickerset = None
    for attr in Jep.media.document.attributes:
        if isinstance(attr, types.DocumentAttributeSticker):
            _stickerset = attr.stickerset
            break
    if _stickerset is None:
        return await edit_or_reply(_, "**- يجب عليك الرد على حزمة.**")
    _id = _stickerset.id
    _hash = _stickerset.access_hash
    _get_stiks = await _.client(functions.messages.GetStickerSetRequest(types.InputStickerSetID(id=_id, access_hash=_hash), hash=0))
    stiks = []
    for i in _get_stiks.documents:
        mul = get_input_document(i)
        stiks.append(
            types.InputStickerSetItem(
                document=mul,
                emoji=(i.attributes[1]).alt,
            )
        )
    try:
        _packname = ""
        if len(_.text) > 20:
            _packname = _.text.split(" ", maxsplit=1)[1]
        HuRe_Jep = await _.client(
            functions.messages.CreateChatRequest(
                users=[_.sender_id],
                title=_packname,
                random_id=random.randint(1, 1000000000),
                reply_markup=types.ReplyKeyboardMarkup(
                    rows=[
                        [
                            types.KeyboardButton(
                                types.InputStickerSetAnimatedEmoji(
                                    stickerset=types.InputStickerSetID(
                                        id=sticker.stickerset.id,
                                        access_hash=sticker.stickerset.access_hash,
                                    ),
                                    emoji=sticker.emoji,
                                )
                            )
                            for sticker in stiks
                        ]
                    ],
                    resize=True,
                    one_time=True,
                ),
            )
        )
    except Exception as er:
        LOGS.exception(er)
        return await edit_or_reply(_, str(er))
    await edit_or_reply(
        _,
        f"**- تم اخذ الحزمة بنجاح ✓ \nالحزمة  → [اضغط هنا](https://t.me/addstickers/{HuRe_Jep.set.short_name})**",
    )
@l313l.ar_cmd(
    pattern="معلومات_الملصق$",
    command=("معلومات_الملصق", plugin_category),
    info={
        "header": "To get information about a sticker pick.",
        "description": "Gets info about the sticker packk",
        "usage": "{tr}stkrinfo",
    },
)
async def get_pack_info(event):
    "To get information about a sticker pick."
    if not event.is_reply:
        return await edit_delete(
            event, "`لايمكنني جلب معلومات هذا الملصق ?!`", 5
        )
    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        return await edit_delete(
            event, "`قم بالرد على الملصق لاستخراج معلوماته`", 5
        )
    try:
        stickerset_attr = rep_msg.document.attributes[1]
        catevent = await edit_or_reply(
            event, "`جار استخراج معلومات الملصق , انتظر قليلاً..`"
        )
    except BaseException:
        return await edit_delete(
            event, "`هذا ليس ملصق قم بالرد ع الملصق`", 5
        )
    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        return await catevent.edit("`This is not a sticker. Reply to a sticker.`")
    get_stickerset = await event.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash,

            ),
hash=0
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    OUTPUT = (
        f"**᯽︙ عنوان الملصق:** `{get_stickerset.set.title}\n`"
        f"**᯽︙ الاسم القصير للملصق:** `{get_stickerset.set.short_name}`\n"
        f"**᯽︙ المـسؤل:** `{get_stickerset.set.official}`\n"
        f"**᯽︙ الارشيف:** `{get_stickerset.set.archived}`\n"
        f"**᯽︙ حزمة الملصق:** `{get_stickerset.set.count}`\n"
        f"**᯽︙ الايموجي المستخدم**\n{' '.join(pack_emojis)}"
    )
    await catevent.edit(OUTPUT)


@l313l.ar_cmd(
    pattern="الملصقات ?([\s\S]*)",
    command=("الملصقات", plugin_category),
    info={
        "header": "To get list of sticker packs with given name.",
        "description": "shows you the list of non-animated sticker packs with that name.",
        "usage": "{tr}stickers <query>",
    },
)
async def cb_sticker(event):
    "To get list of sticker packs with given name."
    split = event.pattern_match.group(1)
    if not split:
        return await edit_delete(event, "`اكتب اسم الحزمه للبحث عنها.`", 5)
    catevent = await edit_or_reply(event, "`جارِ البحث عن الحزمه....`")
    scraper = cloudscraper.create_scraper()
    text = scraper.get(combot_stickers_url + split).text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await edit_delete(catevent, "`لم يتم العثور على النتائج :(.`", 5)
    reply = f"**Sticker packs found for {split} are :**"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            packid = (pack.button).get("data-popup")
            reply += f"\n **• ID: **`{packid}`\n [{packtitle}]({packlink})"
    await catevent.edit(reply)
