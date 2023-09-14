import re

from telethon.utils import get_display_name

from SHRU import Qrh9

from ..core.managers import edit_or_reply
from ..sql_helper import blacklist_sql as sql
from ..utils import is_admin

plugin_category = "admin"

#copyright for SHRU © 2021
@Qrh9.ar_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    catadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not catadmin:
        return
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"᯽︙ ليـس لدي صـلاحيات الـحذف في {get_display_name(await event.get_chat())}.\
                     So removing blacklist words from this group",
                )
                for word in snips:
                    sql.rm_from_blacklist(event.chat_id, word.lower())
            break


@Qrh9.ar_cmd(
    pattern="منع(?:\s|$)([\s\S]*)",
    command=("منع", plugin_category),
    info={
        "header": "To add blacklist words to database",
        "description": "The given word or words will be added to blacklist in that specific chat if any user sends then the message gets deleted.",
        "note": "if you are adding more than one word at time via this, then remember that new word must be given in a new line that is not [hi hello]. It must be as\
            \n[hi \n hello]",
        "usage": "{tr}addblacklist <word(s)>",
        "examples": ["{tr}addblacklist fuck", "{tr}addblacklist fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To add blacklist words to database"
    text = event.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(
        event,
        "᯽︙ تم اضافة {} الكلمة في قائمة المنع بنجاح".format(
            len(to_blacklist)
        ),
    )


@Qrh9.ar_cmd(
    pattern="الغاء منع(?:\s|$)([\s\S]*)",
    command=("الغاء منع", plugin_category),
    info={
        "header": "To remove blacklist words from database",
        "description": "The given word or words will be removed from blacklist in that specific chat",
        "note": "if you are removing more than one word at time via this, then remember that new word must be given in a new line that is not [hi hello]. It must be as\
            \n[hi \n hello]",
        "usage": "{tr}rmblacklist <word(s)>",
        "examples": ["{tr}rmblacklist fuck", "{tr}rmblacklist fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To Remove Blacklist Words from Database."
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    successful = sum(
        bool(sql.rm_from_blacklist(event.chat_id, trigger.lower()))
        for trigger in to_unblacklist
    )
    await edit_or_reply(
        event, f"᯽︙ تم ازالة الكلمة {successful} / {len(to_unblacklist)} من قائمة المنع بنجاح"
    )


@Qrh9.ar_cmd(
    pattern="قائمة المنع$",
    command=("قائمة المنع", plugin_category),
    info={
        "header": "To show the black list words",
        "description": "Shows you the list of blacklist words in that specific chat",
        "usage": "{tr}listblacklist",
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To show the blacklist words in that specific chat"
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "᯽︙ قائمة المنع في الدردشة الحالية :\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👈 {trigger} \n"
    else:
        OUT_STR = " ᯽︙ لم تقم باضافة كلمات سوداء ارسل  `.منع` لمنع كلمة"
    await edit_or_reply(event, OUT_STR)
