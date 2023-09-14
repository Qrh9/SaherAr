from telethon import events
import random, re
from SHRU.utils import admin_cmd
import asyncio 

# Wespr File by  @ll1ilt
# Copyright (C) 2021 SHRU TEAM
@borg.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    Qrh9b = event.pattern_match.group(1)
    rrrd7 = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, Qrh9b) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("᯽︙ اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᯽︙ الامر • `.الهمسة`\n᯽︙ استخدامه • لعرض كيفية كتابة همسة سرية\n\n᯽︙ الامر • `.اكس او `\n ᯽︙ استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n᯽︙ CH  - @SXYO3")
        
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᯽︙ شـرح كيـفية كـتابة همـسة سـرية**\n᯽︙ اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n᯽︙ مـثال  :   `.همسة ههلا @ll1ilt`")
        
@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
# كتابة وتعديل فريق الساحر  #@ll1ilt
async def gamez(event):
    if event.fwd_from:
        return
    jmusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jmusername, uunzz)
    await tap[0].click(event.chat_id)
    await event.delete()
