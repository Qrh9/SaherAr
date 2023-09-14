import re

from telethon import Button, events
from telethon.events import CallbackQuery

from Qrh9.razan.resources.assistant import *
from Qrh9.razan.resources.mybot import *
from SHRU import Qrh9
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://telegra.ph/file/56a3dd726306259beded6.jpg"
ROE = "**♰ هـذه هي قائمة اوامـر سـورس الساحر ♰**"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [Button.inline("✨ اوامر الادمن ✨", data="Qrh90")],
                [
                    Button.inline("✨ اوامر البوت ✨", data="rozbot"),
                    Button.inline("✨ الحساب ✨", data="Jmrz"),
                    Button.inline("✨ المجموعات ✨", data="gro"),
                ],
                [
                    Button.inline("✨ الصيغ و الجهات ✨", data="sejrz"),
                    Button.inline("✨ الحماية و تلكراف ✨", data="grrz"),
                ],
                [
                    Button.inline("✨ اوامر التسلية ✨", data="tslrzj"),
                    Button.inline("✨ الترحيبات والردود ✨", data="r7brz"),
                ],
                [
                    Button.inline("✨ اومر المساعدة ✨", data="krrznd"),
                    Button.inline("✨ الملصقات وصور ✨", data="jrzst"),
                ],
                [
                    Button.inline("✨ التكرار والتنظيف ✨", data="krrznd"),
                    Button.inline("✨ الترفيه ✨", data="rfhrz"),
                ],
                [
                    Button.inline("✨ التكرار والتنظيف ✨", data="iiers"),
                    Button.inline("✨ الملصقات وصور ✨", data="jrzst"),
                ],
                [
                    Button.inline("✨ الأكستـرا ✨", data="iiers"),
                    Button.inline("✨ الانتحال والتقليد ✨", data="uscuxrz"),
                ],
            ]
            if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JEP_IC, text=ROE, buttons=buttons, link_preview=False
                )
            elif JEP_IC:
                result = builder.document(
                    JEP_IC,
                    title="SHRU",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="SHRU",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    ll1ilt = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(ll1ilt, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"Qrh90")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("التالي", data="jrzst"),
      Button.inline("القائمة الرئيسية", data="ROE"),]]
    await event.edit(ROZADM, buttons=buttons)

@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("التالي", data="tslrzj"),
     Button.inline("رجوع", data="Qrh90")]]
    await event.edit(GRTSTI, buttons=butze)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="krrznd"),
     Button.inline("رجوع", data="jrzst")]]
    await event.edit(JMAN, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("التالي", data="rozbot"),
      Button.inline("رجوع", data="tslrzj")]]
    await event.edit(TKPRZ, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="Jmrz"),
     Button.inline("رجوع", data="krrznd")]]
    await event.edit(ROZBOT, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="r7brz"),
     Button.inline("رجوع", data="rozbot")]]
    await event.edit(JROZT, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="sejrz"),
     Button.inline("رجوع", data="Jmrz")]]
    await event.edit(JMTRD, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="gro"),
     Button.inline("رجوع", data="r7brz")]]
    await event.edit(ROZSEG, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="grrz"),
     Button.inline("رجوع", data="sejrz")]]
    await event.edit(JMGR1,buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="iiers"),
     Button.inline("رجوع", data="gro")]]
    await event.edit(ROZPRV, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="rfhrz"),
     Button.inline("رجوع", data="grrz")]]
    await event.edit(HERP, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("التالي", data="uscuxrz"),
     Button.inline("رجوع", data="iiers")]]
    await event.edit(T7SHIZ, buttons=buttons)


@Qrh9.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="Qrh90"),]]
    await event.edit(CLORN, buttons=buttons)
