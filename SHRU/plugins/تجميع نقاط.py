#by Hussein For SHRU-SHRU
#   IDK
# يمنع منعاً باتاً تخمط الملف خلي عندك كرامه ولتسرقة
# Added some f. by ريو
from SHRU import l313l
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.events import NewMessage
import requests
import re
import asyncio
from telethon import events
from ..Config import Config
c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
bot_username5 = '@xnsex21bot'
ConsoleJoker = Config.T7KM
SHRU = ['yes']
its_Reham = False
@l313l.on(admin_cmd(pattern="(تجميع مليار|تجميع المليار)"))
async def _(event):
    if SHRU[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع نقاط بوت المليار، قبل كل شيء تأكد من أنك قمت بالانضمام إلى القنوات الاشتراك الاجباري للبوت لتجنب حدوث أخطاء.**")
        channel_entity = await l313l.get_entity(bot_username)
        await l313l.send_message('@EEObot', '/start')
        await asyncio.sleep(1)
        msg0 = await l313l.get_messages('@EEObot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(1)
        msg1 = await l313l.get_messages('@EEObot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if SHRU[0] == 'no':
                break
            await asyncio.sleep(1)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي، قم بتجميع النقاط بطريقة مختلفة') != -1:
                await l313l.send_message(event.chat_id, "**لا توجد قنوات للبوت.**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@EEObot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, "**خطأ، قد يكون تم حظرك.**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع!**")
    else:
        await event.edit("يجب الدفع لاستخدام هذا الأمر!")


@l313l.on(admin_cmd(pattern="(الغاء التجميع|الغاء تجميع)"))
async def cancel_collection(event):
    await l313l.send_message('@EEObot', '/start')
    await event.edit("** ᯽︙ تم الغاء التجميع من بوت المليار **")
    
@l313l.on(admin_cmd(pattern="(تجميع الجوكر|تجميع جوكر)"))
async def _(event):
    if SHRU[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت الساحر , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username2)
        await l313l.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if SHRU[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except Exception as er:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**\n{er}")
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@l313l.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if SHRU[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username3)
        await l313l.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await l313l.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await l313l.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if SHRU[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@l313l.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if SHRU[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username4)
        await l313l.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await l313l.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await l313l.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if SHRU[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
################################
@l313l.on(admin_cmd(pattern="(تجميع عرب|تجميع العرب)"))
async def _(event):
    if SHRU[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع نقاط بوت العرب, قبل كل شيء تأكد من أنك قمت بالانضمام إلى القنوات الاشتراك الاجباري للبوت لتجنب حدوث أخطاء.**")
        channel_entity = await l313l.get_entity(bot_username5)
        await l313l.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await l313l.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await l313l.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if SHRU[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي، قم بتجميع النقاط بطريقة مختلفة') != -1:
                await l313l.send_message(event.chat_id, "**لا توجد قنوات للبوت.**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, "**خطأ، قد يكون تم حظرك.**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع!**")
    else:
        await event.edit("يجب الدفع لاستخدام هذا الأمر!")

################################
@l313l.ar_cmd(pattern="راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        await event.edit("**᯽︙ تم تفعيل راتب وعد بنجاح سيتم أرسال راتب كل 11 دقيقة**")
        global is_active
        is_active_status = gvarstatus("is_active")
        if is_active_status != "True":
            addgvar("is_active", "True")
            await send_reham(event)
        else:
            await event.edit("**راتب وعد قيد التشغيل بالفعل!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_reham(event):
    is_active_status = gvarstatus("is_active")
    if is_active_status == "True":
        await event.respond('راتب')
        await asyncio.sleep(660)
        await send_reham(event)  
@l313l.ar_cmd(pattern="ايقاف راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        delgvar("is_active")
        await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
@l313l.ar_cmd(pattern="بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        await event.edit("**᯽︙ تم تفعيل بخشيش وعد بنجاح سيتم أرسال بخشيش كل 11 دقيقة**")
        global is_aljoker
        is_aljoker_status = gvarstatus("is_aljoker")
        if is_aljoker_status != "True":
            addgvar("is_aljoker", "True")
            await send_aljoker(event)
        else:
            await event.edit("**راتب وعد قيد التشغيل بالفعل!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_aljoker(event):
    is_aljoker_status = gvarstatus("is_aljoker")
    if is_aljoker_status == "True":
        await event.respond('بخشيش')
        await asyncio.sleep(660)
        await send_aljoker(event)  
@l313l.ar_cmd(pattern="ايقاف بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        delgvar("is_aljoker")
        await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✅**")
    else:
        await event.edit("**᯽︙ هذا الأمر يمكن استخدامه فقط في المجموعات!**")
@l313l.ar_cmd(pattern="استثمار وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        match = re.search(r"استثمار وعد(?:\s+(.*))?", event.raw_text)
        if match:
            message = match.group(1)
            if message:
                if message.isnumeric():
                    await event.edit(f"**᯽︙ تم تفعيل استثمار وعد بنجاح سيتم إرسال الرسالة '{message}' مع كلمة استثمار كل 10 دقائق**")
                    global its_hussein
                    its_hussein_status = gvarstatus("its_hussein")
                    if its_hussein_status != "True":
                        addgvar("its_hussein", "True")
                        await Reham_english(event, message)
                    else:
                        await event.edit("**استثمار وعد قيد التشغيل بالفعل!**")
                else:
                    await event.edit("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
            else:
                await event.edit("**تنبيه: يرجى كتابة رقم الاستثمار مع الأمر!**")
    else:
        await event.edit("**تنبيه: هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def Reham_english(event, message):
    its_hussein_status = gvarstatus("its_hussein")
    if its_hussein_status == "True":
        if message.isnumeric():
            await event.respond(f"استثمار {message}")
            await asyncio.sleep(660)
            await Reham_english(event, message)
        else:
            await event.respond("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
    else:
        if not message.isnumeric():
            await event.respond("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
@l313l.ar_cmd(pattern="ايقاف استثمار وعد(?:\s|$)([\s\S]*)")
async def Reham(event):
    if event.is_group:
        its_hussein_status = gvarstatus("its_hussein")
        if its_hussein_status == "True":
            delgvar("its_hussein")
            await event.edit("**تم إيقاف استثمار الوعد بنجاح!**")
        else:
            await event.edit("**استثمار وعد ليست قيد التشغيل حاليًا!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

@l313l.ar_cmd(pattern="سرقة وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    if event.is_group:
        message = event.pattern_match.group(1).strip()
        if message:
            await event.edit(f"**᯽︙ تم تفعيل سرقة وعد بنجاح سيتم إرسال الرسالة '{message}' مع كلمة سرقة كل 10 دقائق**")
            global its_reda
            its_reda_status = gvarstatus("its_reda")
            if its_reda_status != "True":
                addgvar("its_reda", "True")
                await send_message(event, message)
            else:
                await event.edit("**سرقة وعد قيد التشغيل بالفعل!**")
        else:
            await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def send_message(event, message):
    its_reda_status = gvarstatus("its_reda")
    if its_reda_status == "True":
        await event.respond(f"زرف {message}")
        await asyncio.sleep(660)
        await send_message(event, message)

@l313l.ar_cmd(pattern="ايقاف سرقة وعد(?:\s|$)([\s\S]*)")
async def Reham(event):
    if event.is_group:
        its_reda_status = gvarstatus("its_reda")
        if its_reda_status == "True":
            delgvar("its_reda")
            await event.edit("**تم إيقاف سرقة الوعد بنجاح!**")
        else:
            await event.edit("**استثمار وعد ليست قيد التشغيل حاليًا!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
        

@l313l.ar_cmd(pattern="استثمار بوت وعد")
async def aljoker_money_w3d(event):
    global its_Reham
    if event.is_group:
        await event.respond("فلوسي")
        while its_Reham:
            response = await event.client.listen(event.chat_id, timeout=10)
            if response and response.raw_text.startswith("⇜ فلوسك 54841 ريال 💸"):
                message = response.raw_text
                amount = araby.numbers.from_string(araby.strip_tashkeel(message.split()[2]))
                pyperclip.copy(str(amount))
                await event.respond(f"استثمار {amount}")
            await asyncio.sleep(60)
    else:
        await event.respond("**تنبيه: هذا الأمر يمكن استخدامه فقط في المجموعات!**")

@l313l.ar_cmd(pattern="تعطيل استثمار وعد")
async def disable_w3d(event):
    global its_Reham
    its_Reham = False
    await event.edit("**تم تعطيل عملية الاستثمار وعد.**")


@l313l.on(NewMessage(incoming=True))
async def handle_new_message(event):
    if event.reply_to and event.sender_id == 1421907917:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == l313l.uid and 'فلوسك صارت' in event.message.message and 'استثمار' in event.message.message:
            amount_t = event.message.message.split('فلوسك صارت')[-1].split('ريال')[0].strip()
            amount = re.sub(r'\D', '', amount_t)
            

@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع المليار") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username)
        await l313l.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await l313l.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await l313l.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"تم الانتهاء من التجميع ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await l313l.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
       
