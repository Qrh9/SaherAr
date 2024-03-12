# Copyright (C) 2023 SHRU TEAM
# FILES WRITTEN BY  @RedParx

from telethon import events
from telethon.utils import get_display_name

from SHRU import Qrh9
from SHRU.core.logger import logging

from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
    update_previous_welcome,
)
from . import BOTLOG_CHATID

plugin_category = "utils"
LOGS = logging.getLogger(__name__)


@Qrh9.on(events.ChatAction)
async def _(event):
    cws = get_current_welcome_settings(event.chat_id)
    if (
        cws
        and (event.user_joined or event.user_added)
        and not (await event.get_user()).bot
    ):
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await event.client.get_me()
        title = get_display_name(await event.get_chat()) or "this chat"
        participants = await event.client.get_participants(chat)
        count = len(participants)
        mention = f"<a href='tg://user?id={a_user.id}'>{a_user.first_name}</a>"
        my_mention = f"<a href='tg://user?id={me.id}'>{me.first_name}</a>"
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        file_media = None
        current_saved_welcome_message = None
        if cws:
            if cws.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
                )
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
                link_preview = True
            elif cws.reply:
                current_saved_welcome_message = cws.reply
                link_preview = False
        current_message = await event.reply(
            current_saved_welcome_message.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=file_media,
            parse_mode="html",
            link_preview=link_preview,
        )
        update_previous_welcome(event.chat_id, current_message.id)


@Qrh9.ar_cmd(
    pattern="ترحيب(?:\s|$)([\s\S]*)",
    command=("ترحيب", plugin_category),
    info={
        "header": "To welcome new users in chat.",
        "description": "Saves the message as a welcome note in the chat. And will send welcome message to every new user in group who ever joins newly in group.",
        "option": {
            "{mention}": "To mention the user",
            "{title}": "To get chat name in message",
            "{count}": "To get group members",
            "{first}": "To use user first name",
            "{last}": "To use user last name",
            "{fullname}": "To use user full name",
            "{userid}": "To use userid",
            "{username}": "To use user username",
            "{my_first}": "To use my first name",
            "{my_fullname}": "To use my full name",
            "{my_last}": "To use my last name",
            "{my_mention}": "To mention myself",
            "{my_username}": "To use my username.",
        },
        "usage": [
            "{tr}savewelcome <welcome message>",
            "reply {tr}savewelcome to text message or supported media with text as media caption",
        ],
        "examples": "{tr}savewelcome Hi {mention}, Welcome to {title} chat",
    },
)
async def save_welcome(event):
    "To set welcome message in chat."
    msg = await event.get_reply_message()
    string = "".join(event.text.split(maxsplit=1)[1:])
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"⌔︙رسالة الترحيب  :\
                \n⌔︙ايدي الدردشة  : {event.chat_id}\
                \n⌔︙يتم حفظ الرسالة التالية كملاحظة ترحيبية لـ 🔖 : {event.chat.title}, ",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
            )
            msg_id = msg_o.id
    await edit_or_reply("**᯽︙ هـنالك خـطأ في وضـع الـترحيب هـنا**")


@Qrh9.ar_cmd(
    pattern="حذف الترحيب$",
    command=("حذف الترحيب", plugin_category),
    info={
        "header": "To turn off welcome message in group.",
        "description": "Deletes the welcome note for the current chat.",
        "usage": "{tr}clearwelcome",
    },
)
async def del_welcome(event):
    "To turn off welcome message"
    if rm_welcome_setting(event.chat_id) is True:
        await edit_or_reply(event, "**᯽︙ تم حذف الترحيب بنجاح ✓**")
    else:
        await edit_or_reply(event, "**᯽︙ ليـس لـدي اي تـرحيبـات بالأصـل ✓**")


@Qrh9.ar_cmd(
    pattern="الترحيب$",
    command=("الترحيب", plugin_category),
    info={
        "header": "To check current welcome message in group.",
        "usage": "{tr}listwelcome",
    },
)
async def show_welcome(event):
    "To show current welcome message in group"
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        return await edit_or_reply(event, "**᯽︙ لم يتم حفظ اي ترحيب هنا**")
    if cws.f_mesg_id:
        msg_o = await event.client.get_messages(
            entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
        )
        await edit_or_reply(
            event, "᯽︙ أنا الان اقوم بالترحيب بالمستخدمين الجدد مع هذه الرسالة"
        )
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await edit_or_reply(
            event, "᯽︙ أنا الان اقوم بالترحيب بالمستخدمين الجدد مع هذه الرسالة"
        )
        await event.reply(cws.reply, link_preview=False)


@Qrh9.ar_cmd(
    pattern="الترحيب (تشغيل|ايقاف)$",
    command=("cleanwelcome", plugin_category),
    info={
        "header": "To turn off or turn on of deleting previous welcome message.",
        "description": "if you want to delete previous welcome message and send new one turn on it by deafult it will be on. Turn it off if you need",
        "usage": "{tr}cleanwelcome <on/off>",
    },
)
async def del_welcome(event):
    "To turn off or turn on of deleting previous welcome message."
    input_str = event.pattern_match.group(1)
    if input_str == "on":
        if gvarstatus("clean_welcome") is None:
            return await edit_delete(event, "**تم تشغيل الترحيب بنجاح ✓ **")
        delgvar("clean_welcome")
        return await edit_delete(
            event,
            "__From now on previous welcome message will be deleted and new welcome message will be sent.__",
        )
    if gvarstatus("clean_welcome") is None:
        addgvar("clean_welcome", "false")
        return await edit_delete(
            event, "__From now on previous welcome message will not be deleted .__"
        )
    await edit_delete(event, "** تم تعطيل الترحيب بنجاح ✓")