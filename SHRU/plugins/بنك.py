import time
import re
from ..Config import Config
from ..sql_helper.bank import add_bank, del_bank, get_bank, update_bank, des_bank
from telethon import Button, events
import glob, os
import os.path
from ..helpers import get_user_from_event
from telethon import types
from random import randint
import random
from . import l313l
from ..core.managers import edit_delete, edit_or_reply

import asyncio

plugin_category = "utils"
#----Timers----#
t = {}
#--------------#
def convert(seconds): 

    seconds = seconds % (24 * 3600) 

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

@l313l.ar_cmd(pattern="tdata")

async def td(event):
    return await edit_or_reply(event, str(t))

@l313l.ar_cmd(pattern="توب الفلوس(.*)")
   
async def d(message):
    users = des_bank()
    if not users:
        return edit_or_reply(message, "لا يوجد حسابات في المصرف")
    list = '**قائمة اغنى عشرة**\n'
    count = 0
    for i in users:
        count += 1
        list += f'**{count} -** [{i.first_name}](tg://user?id={i.user_id}) {i.balance} 💵\n'
        
    await edit_or_reply(message, list)
    #return await edit_or_reply(message, str(des_bank()))

@l313l.ar_cmd(pattern="مسح حسابي(.*)")
   
async def d(message):
    me = await message.client.get_me()
    acc = get_bank(me.id)
    if acc is None:
        await edit_delete(message, "لا تملك حساب مصرفي لحذفه")
    else:
        row = del_bank(me.id)
        await message.delete()
        await message.client.send_message(message.chat_id, "تم حذف حسابك المصرفي")

@l313l.ar_cmd(
    pattern="انشاء حساب(?:\s|$)([\s\S]*)",
    command=("انشاء حساب", plugin_category),
)
async def start(event):
    me = await event.client.get_me()
    sta = await edit_or_reply(event, f"""</strong>

👋  {me.first_name} مرحبًا
 ━━━━━━━━━━━━━━━━━
- لأنشاء حساب اختر احد المصاريف الاتية

- .انشاء حساب الساحر الاسلامي  

- .انشاء حساب الرافدين
 ━━━━━━━━━━━━━━━━━

</strong>""",parse_mode="html")



@l313l.on(admin_cmd(pattern="(فلوسي|اموالي) ?(.*)"))
async def a(message):
    me = await message.client.get_me()
    if get_bank(me.id) is None:
         noa = await edit_or_reply(message, f"<strong>انت لا تملك حساب في البنك</strong>", parse_mode="html")
    else:
         acc = get_bank(me.id)
         mo = int(acc.balance)
         ba = await edit_or_reply(message,f"<strong>اموالك : {mo}  💵</strong>",parse_mode="html")



@l313l.on(admin_cmd(pattern="(بنكي|مصرفي) ?(.*)"))
async def myb(message):

    me = await message.client.get_me()
    
    if get_bank(me.id) is not None:
         acc = get_bank(me.id)
         nn = acc.first_name
         balance = acc.balance
         ba = acc.bank
         ifn = f"""
- ================= -
• الاسم : {nn} 
• رقم الحساب : {me.id} 
• الاموال : {balance} 💵
• اسم المصرف : {ba} 
- ================= -
          """
         acinfo = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")

    else:
         ca = await edit_or_reply(message,f"<strong>ليس لديك حساب في البنك!</strong>",parse_mode="html")


@l313l.ar_cmd(func=lambda m:"راتب")
async def ga(message):
    mee = await message.client.get_me()
    ms = message.text
    acc = get_bank(mee.id)
 
    if ms == ".المصرف" or ms == ".البنك" or ms == ".مصرف":


        help = """
•| قائمة المساعدة |•
.انشاء حساب (لانشاء حساب مصرفي)
- مثال: .انشاء حساب الرافدين او الساحر الاسلامي
1- .استثمار (مبلغ) 
- مثال : استثمار 18276
2- .حظ (المبلغ)
- مثال : حظ 17267
3- .راتب
4- .كنز
5- .بخشيش
6- .فلوسي | لرؤية فلوسك
7- .بنكي او .مصرفي | لاضهار معلومات حسابك في المصرف
8- .مسح حسابي | لحذف حسابك البنكي
      """


        hr = await edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == ".كنز":
        if "كنز" in t:
              tii = t["كنز"] - time.time()
              return await edit_or_reply(message,"<strong> ليس هنالك كنز لقد اخذته بالفعل انتضر {}</strong>".format(convert(tii)),parse_mode="html")
     
        else:
              rt = randint(50,3000)
              acca = get_bank(mee.id).balance
              ga = int(rt) + int(acca)
              update_bank(mee.id, ga)
              tx = await edit_or_reply(message,f"<strong>💸 لقد حصلت على الكنز!🤩\n- حصلت على {rt} 💵.\n- اموالك الان : {ga} 💵 .</strong>",parse_mode="html")
              t["كنز"] = time.time() + 600 
              await asyncio.sleep(600)
              del t["كنز"]
     
    if ".استثمار" in ms:
        value = message.text.replace(".استثمار","")
        if "استثمار" in t:
            ti2 = t["استثمار"] - time.time()
            return await edit_or_reply(message,"<strong> للاستثمار مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        lss = ["Done","Fail"]
        ls = random.choice(lss)
        ppe = acc.balance
        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الاموال للاستثمار</strong>", parse_mode="html")
        #isv = value.isnumeric()
        #if not isv:
         #    return await edit_delete(message, "<strong>!ادخل رقم صالِح للاستثمار</strong>", parse_mode="html")
        if "Done" in ls:
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            d = ["1%","2%","4%","8%","9%"]
            ra = random.choice(d)
            ma = await edit_or_reply(message,f"""<strong>
===================
• استثمار ناجح  💰
• نسبة الربح  ↢ {ra}
• مبلغ الربح  ↢ ( {ppe} 💵 )
• اموالك الان  ↢ ( {kf}  💵 )
===================
</strong>""",parse_mode="html")
            t["استثمار"] = time.time() + 600
            await asyncio.sleep(600)
            del t["استثمار"]
        if "Fail" in ls:
             await edit_or_reply(message, "استثمار فاشل لم تحصل على اي ارباح")
             t["استثمار"] = time.time() + 600
             await asyncio.sleep(600)
             del t["استثمار"]
             

    if f".حظ"in message.text:
        value = message.text.replace(".حظ","")
        ppe = acc.balance
        if "حظ" in t:
            ti2 = t["حظ"] - time.time()
            return await edit_or_reply(message,"<strong> للعب الحظ مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الاموال للحظ</strong>", parse_mode="html")
        ls = ["Done","Fail"]
        sv = random.choice(ls)
        if "Done" in sv:
        
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            cong = await edit_or_reply(message,f"""<strong>          
======================
• مبارك لقد ربحت بالحظ
• اموالك السابقة  ↢ ( {ppe}  💵 ) .
• اموالك الان  ↢ ( {kf}  💵 ) .
======================
</strong>""",parse_mode="html")
            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
        else:
            pa = acc.balance
            pop = int(pa) - int(value)
            update_bank(mee.id, pop)
            heh = await edit_or_reply(message,f"""<strong>
=======================
• لسوء الحظ , خسرت في الحظ 
• اموالك السابقة  ↢ ( {pa} 💵 ) .
• اموالك الان  ↢ ( {pop} 💵 ) .
========================
</strong>""",parse_mode="html")

            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
    if ms == ".بخشيش":
        ppe = acc.balance
        if "بخشيش" in t:
            ti2 = t["بخشيش"] - time.time()
            return await edit_or_reply(message,"<strong> لقد اخذت بخشيش انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        else:
              rt = randint(70,2000)
              ga = int(rt) + int(ppe)
              tp = await edit_or_reply(message,f"<strong>=================\n- •تم ايداع البخشيش 💸\n- • حصلت على  {rt} 💵.\n- • أموالك الان : {ga} 💵\n=================</strong>",parse_mode="html")
              update_bank(mee.id, ga)
              t["بخشيش"] = time.time() + 600
              await asyncio.sleep(600)
              del t["بخشيش"]
    
    if ms == ".راتب":
        ba = acc.balance
        if "راتب" in t:
            ti2 = t["راتب"] - time.time()
            return await edit_or_reply(message,"<strong> لأخذ راتب مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        else:


              list = ["مبرمج 💻-1000","ملك 🤴-10000","قاضي 👨‍⚖-20000","عامل 🧑‍🔧-1000","روبوت 🤖-2300","سائق 🚓-4000","تاجر مخدرات 🚬-5000","تاجر اسلحة 🔫-9000","طيار ✈️-7000","قبطان 🛳-8000"]

              rt = random.choice(list)
              name = rt.split("-")[0]
              ratb = rt.split("-")[1]
              ga = int(ratb) + int(ba)
              update_bank(mee.id, ga)
              sal = await edit_or_reply(message,f"<strong>==================\n- • تم ايداع راتبك! 💸🤩\n- • حصلت على {ratb} 💵\n- • لأنك {name}.\n- • اموالك الان : {ga} 💵 \n==================</strong>",parse_mode="html")
              t["راتب"] = time.time() + 600
              await asyncio.sleep(600)
              del t["راتب"]

@l313l.ar_cmd(
    pattern="اسرق(?:\s|$)([\s\S]*)",
    command=("اسرق", plugin_category),
)
async def thief(message):
    mee = await message.client.get_me()
    user, custom = await get_user_from_event(message)
    accu = get_bank(user.id)
    acc = get_bank(mee.id)
    if "اسرق" in t:
        ti2 = t["اسرق"] - time.time()
        return await edit_or_reply(message,"<strong> لقد سرقت قبل قليل انتظر {}</strong>".format(convert(ti2)),parse_mode="html")
    else:
        if not user:
            return await edit_or_reply(message,"<strong> يجب عليك الرد على شخص لسرقته </strong>", parse_mode="html")
        if get_bank(user.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك سرقة شخص لا يمتلك حساب مصرفي </strong>", parse_mode="html")
        if get_bank(mee.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك السرقة لانك لا تملك حساب مصرفي </strong>", parse_mode="html")
        if int(accu.balance) < 5000:
            return await edit_or_reply(message,"<strong> لا يمكنك سرقته لان امواله اقل من 5000$ </strong>", parse_mode="html")
    rt = randint(70,2000)
    ppe = int(acc.balance)
    be = int(accu.balance)
    jep = int(be) - int(rt)
    update_bank(user.id, jep)
    SHRU = mee.first_name.replace("\u2060", "") if mee.first_name else mee.username
    ga = int(rt) + int(ppe)
    update_bank(mee.id, ga)
    await l313l.send_file(
                message.chat_id,
                "https://telegra.ph/file/56a3dd726306259beded6.jpg",
                caption=f"سرق [{SHRU}](tg://user?id={mee.id}) من [{user.first_name}](tg://user?id={user.id})\n المبلغ: {rt} 💵",
                )
    t["اسرق"] = time.time() + 600
    await asyncio.sleep(600)
    del t["اسرق"]
    
    
@l313l.ar_cmd(pattern="انشاء حساب (.*)")
async def bankar(message):
    input = message.pattern_match.group(1)
    mee = await message.client.get_me()
    if get_bank(mee.id) is not None:
        return await edit_or_reply(message, f"<strong>لديك حساب مصرفي بالفعل</strong>",parse_mode="html")
    if input == "الساحر الاسلامي":
        bankn = "مصرف الساحر الاسلامي"
    elif input == "الرافدين":
    	bankn = "مصرف الرافدين"
    elif input != "الرافدين" or "الساحر الاسلامي":
         return await edit_or_reply(message, "لا يوجد هكذا مصرِف !")
    add_bank(mee.id, mee.first_name, 50, bankn)
    cbs = await edit_or_reply(message,f"<strong>تم انشاء حساب مصرفي بالمعلومات التالية:\nاسم صاحب الحساب:{mee.first_name}|\nايدي الحساب:{mee.id}|\nاسم المصرف:{bankn}|\nالاموال المودعة:50$</strong>", parse_mode="html")
