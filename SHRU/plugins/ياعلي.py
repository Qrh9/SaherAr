from SHRU import Qrh9, bot
from SHRU import BOTLOG_CHATID
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import asyncio
from ..Config import Config
import requests
from telethon import Button, events
from telethon.tl.functions.messages import ExportChatInviteRequest
from ..core.managers import edit_delete, edit_or_reply
#ياعلي
#اخ اخ اخ اخ اخ اخ اخممممممط ياطويل العمر اخمطط 😂
#
REH = "**᯽︙ لأستخدام بوت اختراق الحساب عن طريق كود التيرمكس أضغط على الزر**"
JOKER_PIC = "https://telegra.ph/file/9169a1beb5d832a363f51.jpg"
Bot_Username = Config.TG_BOT_USERNAME
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        joker = Bot_Username.replace("@", "")
        query = event.text
        await bot.get_me()
        if query.startswith("هاك") and event.query.user_id == bot.uid:
            buttons = Button.url("• اضغط هنا عزيزي •", f"https://t.me/{joker}")
            if JOKER_PIC and JOKER_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JOKER_PIC, text=REH, buttons=buttons, link_preview=False
                )
            elif JOKER_PIC:
                result = builder.document(
                    JOKER_PIC,
                    title="𝘼𝙇𝙨𝙖𝙝𝙚𝙧✨",
                    text=REH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="𝘼𝙇𝙨𝙖𝙝𝙚𝙧✨",
                    text=REH,
                    buttons=buttons,
                    link_preview=False,
                )
        await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="هاك"))
async def repo(event):
    if event.fwd_from:
        return
    SX9OO = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    await bot.send_message(SX9OO, "/hack")
    response = await bot.inline_query(SX9OO, "هاك")
    await response[0].click(event.chat_id)
    await event.delete()

@Qrh9.ar_cmd(pattern="اشتراك")
async def reda(event):
    ty = event.text
    ty = ty.replace(".اشتراك", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**᯽︙ قم بكتابة نوع الاشتراك الاجباري كروب او خاص 🤔**")
    if ty == "كروب":
        if not event.is_group:
            return await edit_delete("**᯽︙ استعمل الأمر في الجروب المراد تفعيل الاشتراك الاجباري به**")
        if event.is_group:
            if gvarstatus ("subgroup") == event.chat_id:
                return await edit_delete(event, "**᯽︙ الاشتراك الاجباري مفعل لهذا الكروب**")
            if gvarstatus("subgroup"):
                return await edit_or_reply(event, "**᯽︙ الاشتراك الاجباري مفعل لكروب اخر قم بالغائه لتفعيله في كروب اخر**")
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(event, "**᯽︙ تم تفعيل الاشتراك الاجباري لهذه المجموعة ✓**")
    if ty == "خاص":
        if gvarstatus ("subprivate"):
            return await edit_delete(event, "**᯽︙ الاشتراك الاجباري للخاص مُفعل بالفعل ✓**")
        if not gvarstatus ("subprivate"):
            addgvar ("subprivate", True)
            await edit_or_reply(event, "**᯽︙ تم تفعيل الاشتراك الاجباري للخاص ✓**")
    if ty not in ["خاص", "كروب"]:
        return await edit_delete(event, "**᯽︙ قم بكتابة نوع الاشتراك الاجباري خاص او كروب 🤔**")
@Qrh9.ar_cmd(pattern="تعطيل")
async def reda (event):
    cc = event.text.replace(".تعطيل", "")
    cc = cc.replace(" ", "")
    if len (cc) < 2:
        return await edit_delete(event, "**᯽︙ قم بكتابة نوع الاشتراك الاجباري لإلغائه**")
    if cc == "كروب":
        if not gvarstatus ("subgroup"):
            return await edit_delete(event, "**᯽︙ لم تفعل الاشتراك الاجباري للكروب لإلغائه**")
        if gvarstatus ("subgroup"):
            delgvar ("subgroup")
            return await edit_delete(event, "**᯽︙ تم الغاء الاشتراك الاجباري للكروب بنجاح ✓**")
    if cc == "خاص":
        if not gvarstatus ("subprivate"):
            return await edit_delete(event, "**᯽︙ الاشتراك الاجباري للخاص غير مفعل لإلغائه**")
        if gvarstatus ("subprivate"):
            delgvar ("subprivate")
            return await edit_delete(event, "**᯽︙ تم إلغاء الاشتراك الاجباري للخاص ✓**")
    if cc not in ["خاص", "كروب"]:
        return await edit_delete(event, "**᯽︙ قم بكتابة نوع الاشتراك الاجباري لإلغائه ✓**")

@Qrh9.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("subprivate"):
        if event.is_private:
            try:
       
                idd = event.peer_id.user_id
                tok = Config.TG_BOT_TOKEN
                ch = gvarstatus ("pchan")
                if not ch:
                    return await Qrh9.tgbot.send_message(BOTLOG_CHATID, "** انت لم تضع قناة الاشتراك الاجباري قم بوضعها**")
                try:
                    ch = int(ch)
                except BaseException as r:
                    return await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"**حدث خطأ \n{r}**")
                url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
                req = requests.get(url)
                reqt = req.text
                if "chat not found" in reqt:
                    mb = await Qrh9.tgbot.get_me()
                    mb = mb.username
                    await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"**البوت الخاص بك @{mb} ليس في قناة الاشتراك الاجباري**")
                    return
                if "bot was kicked" in reqt:
                    mb = await Qrh9.tgbot.get_me()
                    mb = mb.username
                    await Qrh9.tgbot.send_message(BOTLOG_CHATID, "** البوت الخاص بك @{mb} مطرود من قناة الاشتراك الاجباري اعد اضافته**")
                    return
                if "not found" in reqt:
                    try:
                        c = await Qrh9.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await Qrh9.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**᯽︙ يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**", buttons=[(Button.url("اضغط هنا", chn),)],
                            )
                            return await event.delete()
                        else:
                            await event.reply(f"**᯽︙ للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **", buttons=[(Button.url("اضغط هنا", f"https://t.me/{chn}"),)],
                            )
                            return await event.delete()
                    except BaseException as er:
                        await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "left" in reqt:
                    try:
                        c = await Qrh9.get_entity(ch)
                        chn = c.username
                        if c.username == None:
                            ra = await Qrh9.tgbot(ExportChatInviteRequest(ch))
                            chn = ra.link
                        if chn.startswith("https://"):
                            await event.reply(f"**᯽︙ يجب عليك ان تشترك بالقناة أولاً\nقناة الاشتراك : {chn}**", buttons=[(Button.url("اضغط هنا", chn),)],
                            )
                            return await event.message.delete()
                        else:
                            await event.reply(f"**᯽︙ للتحدث معي يجب عليك الاشتراك في القناة\n قناة الاشتراك : @{chn} **", buttons=[(Button.url("اضغط هنا", f"https://t.me/{chn}"),)],
                            )
                            return await event.message.delete()
                    except BaseException as er:
                        await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"حدث خطا \n{er}")
                if "error_code" in reqt:
                    await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"**حدث خطأ غير معروف قم باعادة توجيه الرسالة ل@ll1ilt لحل المشكلة\n{reqt}**")
                
                return
            except BaseException as er:
                await Qrh9.tgbot.send_message(BOTLOG_CHATID, f"** حدث خطا\n{er}**")


async def upload_story(client, reply_to_message, caption=None):
    try:
        # Edit the reply message to indicate story uploading
        uploading_msg = await reply_to_message.edit(f"**Uploading story...**\n\n______________________")

        # Check if the replied message is a photo or a video
        if reply_to_message.photo:
            media = types.InputPhoto(
                id=reply_to_message.photo.id,
                access_hash=reply_to_message.photo.access_hash,
                file_reference=reply_to_message.photo.file_reference,
                thumb=types.InputDocument(
                    id=reply_to_message.photo.thumbs[0].id,
                    access_hash=reply_to_message.photo.thumbs[0].access_hash,
                    file_reference=reply_to_message.photo.thumbs[0].file_reference,
                    file_size=reply_to_message.photo.thumbs[0].file_size,
                    location=reply_to_message.photo.thumbs[0].location,
                    type=reply_to_message.photo.thumbs[0].type,
                ),
                size=reply_to_message.photo.size,
            )
        elif reply_to_message.video:
            media = types.InputDocument(
                id=reply_to_message.video.id,
                access_hash=reply_to_message.video.access_hash,
                file_reference=reply_to_message.video.file_reference,
                date=reply_to_message.video.date,
                mime_type=reply_to_message.video.mime_type,
                size=reply_to_message.video.size,
                dc_id=reply_to_message.video.dc_id,
                version=reply_to_message.video.version,
                attributes=reply_to_message.video.attributes,
            )
        else:
            return await uploading_msg.edit("Error: Only photos and videos are supported for stories.")

        # Upload the media to the user's story
        media_id = await client(UploadMedia(
            file=media,
            stickers=[],
            ttl_seconds=86400,  # Story lasts for 24 hours
        ))

        # Set the caption as the story description
        story_caption = caption or "**none**"

        # Upload the story
        await client(UploadStory(
            media=types.InputStoryMediaPhoto(
                id=media_id,
                lat=0.0,
                long=0.0,
                reply_markup=None,
                random_id=0,
            ),
            stickers=[],
            ttl_seconds=86400,
            geo_point=types.InputGeoPointEmpty(),
            reply_to=types.InputStoryReply(
                random_id=0,
                user_id=0,
            ),
            multiple=False,
            attached_sticker=None,
            poll=None,
            question=None,
            answer=None,
            viewer_id=0,
            story_id=0,
            # Add the story caption as the story text
            text=story_caption,
        ))

        # Get the newly uploaded story details
        uploaded_story = await client(GetStories(
            id=None,
            limit=1,
            offset_id=0,
            hash=0,
            emojis="",
            filter=InputMessagesFilterPhoto() if reply_to_message.photo else InputMessagesFilterDocument(),
        ))
        uploaded_story = uploaded_story.chats[0].messages[0]

        # Edit the reply message to indicate successful story upload
        await uploading_msg.edit(
            f"**New story uploaded!!**\n\n"
            f"```\n"
            f"Story length: {uploaded_story.media.duration} seconds\n"
            f"Story id: {uploaded_story.id}\n"
            f"Story description: {story_caption}\n"
            f"```\n"
            f"______________________"
        )

    except Exception as e:
        print(f"Error uploading story: {e}")
        await uploading_msg.edit("Error: Failed to upload story.")

# Command handler


@Qrh9.ar_cmd(pattern="قصه$")
async def story_upload_handler(event):
    if event.is_reply and event.reply_to_msg_id:
        await upload_story(Qrh9, await event.get_reply_message(), caption=event.text[len(".مرر"):].strip())
    else:
        await event.reply("Reply to a photo or video to upload it as a story with an optional caption.")
