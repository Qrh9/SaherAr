import asyncio
import math

import heroku3
import requests
import urllib3

from SHRU import l313l

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@l313l.ar_cmd(pattern="وضع (.*)")
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            var,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            var,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    rep = await var.get_reply_message()
    vra = None
    if rep:
        vra = rep.text
    if vra is None:
        return await edit_delete(
            var, "**⌔∮ يجب عليك الرد على النص او الرابط حسب الفار الذي تضيفه **"
        )
    exe = var.pattern_match.group(1)
    await edit_or_reply(var, "**⌔∮ جارِ وضع الفار انتظر قليلا**")
    heroku_var = app.config()
    if exe == "توقيت":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير الوقت الخاص بك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير الوقت الخاص بك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "لون وقتي" or exe == "لون الوقتي":
        variable = "DIGITAL_PIC_COLOR"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار لون الوقتي\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار لون الوقتي \n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "رمز الاسم":
        variable = "TIME_JEP"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار رمز الاسم\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار رمز الاسم \n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "البايو" or exe == "النبذة" or exe == "بايو":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار البايو\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار البايو\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "امر نشر" or exe == "امر النشر" or exe == "مكرر":
        variable = "MUKRR_ET"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير امر النشر التلقائي\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير امر النشر التلقائي\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "القروب" or exe == "الكروب" or exe == "كروب":
        variable = "DEFAULT_GROUP"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الكروب\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الكروب\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra 
    if exe == "الصورة" or exe == "الصوره" or exe == "صورة":
        variable = "DIGITAL_PIC"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "صورة القروب" or exe == "صورة الكروب":
        variable = "DIGITAL_GROUP_PIC"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار صورة المجموعة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار المجموعة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "لون" or exe == "اللون":
        variable = "DIGITAL_PIC_COLOR"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "زخرفة الارقام" or exe == "زخرفه الارقام":
        variable = "JP_FN"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار زخرفه الارقام\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار زخرفه الارقام\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "اسم" or exe == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار اسم المستخدم\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار اسم المستخدم\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "كروب التخزين":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار كروب التخزين\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار كروب التخزين\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra
    if exe == "كروب الحفظ":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1)
        if variable in heroku_var:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار كروب الحفظ\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                var,
                "**⌔∮ تم بنجاح تغيير فار كروب الحفظ\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = vra


@l313l.ar_cmd(pattern="محو (.*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            event,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            event,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    exe = event.text[5:]
    heroku_var = app.config()
    await edit_or_reply(event, "**⌔∮ جارِ حذف الفار انتظر قليلا**")
    if exe == "رمز الاسم":
        variable = "TIME_JEP"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(
                event, "**⌔∮ لم تتم اضافه فار رمز الاسم بالاصل.**"
            )
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار رمز الاسم\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "البايو" or exe == "النبذة":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(event, "**⌔∮ لم تتم اضافه فار البايو بالاصل.**")
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار البايو\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "القروب" or exe == "الكروب":
        variable = "DEFAULT_GROUP"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(event, "**⌔∮ لم تتم اضافه فار الكروب بالاصل.**")
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار الكروب\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "اللون الوقتي" or exe == "لون وقتي":
        variable = "DIGITAL_PIC_COLOR"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(event, "**⌔∮ لم تتم اضافه فار لون الوقتي بالاصل.**")
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار لون الوقتي\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "الصورة" or exe == "الصوره":
        variable = "DIGITAL_PIC"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(event, "**⌔∮ لم تتم اضافه فار الصورة بالاصل.**")
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "الاسم" or exe == "اسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(event, "**⌔∮ لم تتم اضافه فار الاسم بالاصل.**")
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار الاسم\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "زخرفة الارقام" or exe == "زخرفه الارقام":
        variable = "JP_FN"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(
                event, "**⌔∮ لم تتم اضافه فار زخرفه الارقام بالاصل.**"
            )
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار زخرفه الارقام\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "كروب التخزين":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(
                event, "**⌔∮ لم تتم اضافه فار كروب التخزين بالاصل.**"
            )
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار كروب التخزين\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "كروب الحفظ":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(
                event, "**⌔∮ لم تتم اضافه فار كروب الحفظ بالاصل.**"
            )
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار كروب الحفظ\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]
    if exe == "زخرفة الصورة":
        variable = "DEFAULT_PIC"
        await asyncio.sleep(1)
        if variable not in heroku_var:
            return await edit_or_reply(
                event, "**⌔∮ لم تتم اضافه فار زخرفة الصورة بالاصل.**"
            )
        await edit_or_reply(
            event,
            "**⌔∮ تم بنجاح حذف فار زخرفة الصورة\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
        )
        del heroku_var[variable]


@l313l.ar_cmd(pattern="وقت(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            event,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            event,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    exe = event.text[5:]
    iraq = "Asia/Baghdad"
    cairo = "Africa/Cairo"
    jordan = "Asia/Amman"
    yman = "Asia/Aden"
    Syria = "Asia/Damascus"
    heroku_var = app.config()
    await edit_or_reply(event, "⌔∮ يتم جلب معلومات هذا الفار")
    if exe == "العراق" or exe == "عراق":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى العراق\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى العراق\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = iraq
    if exe == "السعودية" or exe == "السعوديه":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى السعودية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى السعودية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = iraq
    if exe == "مصر":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى مصر\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى مصر\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = cairo
    if exe == "الاردن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى الاردن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى الاردن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = jordan
    if exe == "اليمن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى اليمن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى اليمن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = yman
    if exe == "سوريا":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى اليمن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        else:
            await edit_or_reply(
                event,
                "**⌔∮ تم بنجاح تغيير الوقت الى اليمن\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**",
            )
        heroku_var[variable] = Syria
        
@l313l.ar_cmd(pattern="زخرفة الصورة(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    heroku_var = app.config()
    jep = await edit_or_reply(event, "**جـاري اضـافة زخـرفـة الوقتيـه لـ حسابك ✅ . . .**")
    if input_str == "1":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/SXYO3.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "2":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Starjedi.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "3":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Papernotes.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "4":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Terserah.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "5":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Photography Signature.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "6":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Austein.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "7":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Dream MMA.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "8":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/EASPORTS15.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "9":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/KGMissKindergarten.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "10":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/212 Orion Sans PERSONAL USE.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "11":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/PEPSI_pl.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "12":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Paskowy.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "13":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Cream Cake.otf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "14":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Hello Valentina.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "15":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Alien-Encounters-Regular.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "16":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/Linebeam.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "17":
        variable = "DEFAULT_PIC"
        zinfo = "SHRU/helpers/styles/EASPORTS15.ttf"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير زخرفة الصورة الوقتية\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo

@l313l.ar_cmd(pattern="ميوزك(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    heroku_var = app.config()
    jep = await edit_or_reply(event, "** جارِ تغير وضع الميوزك ✅ . . .**")
    if input_str == "تفعيل":
        variable = "VCMODE"
        zinfo = "True"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo
    elif input_str == "تعطيل":
        variable = "VCMODE"
        zinfo = "False"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jep.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        else:
            await jep.edit("**⌔∮ تم بنجاح تغيير وضع الميوزك\n\n❃ جار اعادة تشغيل السورس انتظر من 2-5 دقائق ليتشغل مره اخرى**".format(input_str))
        heroku_var[variable] = zinfo


@l313l.ar_cmd(pattern="استخدامي$")
async def dyno_usage(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    dyno = await edit_or_reply(dyno, "**- يتم جلب المعلومات انتظر قليلا**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("**خطا: يوجد شي غير صحيح حدث**\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**استخدام الدينو**:\n\n"
        f" -> `استخدام الدينو لتطبيق`  **{Config.HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**ساعات**  `{AppMinutes}`**دقائق**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> الساعات المتبقية لهذا الشهر :\n"
        f"     •  `{hours}`**ساعات**  `{minutes}`**دقائق**  "
        f"**|**  [`{percentage}`**%**]"
    )


@l313l.ar_cmd(pattern="لوك$")
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "عزيزي المستخدم يجب ان تعين معلومات الفارات التالية لاستخدام اوامر الفارات\n `HEROKU_API_KEY`\n `HEROKU_APP_NAME`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " يجب التذكر من ان قيمه الفارات التاليه ان تكون بشكل صحيح \nHEROKU_APP_NAME\n HEROKU_API_KEY"
        )
    data = app.get_log()
    await edit_or_reply(
        dyno, data, deflink=True, linktext="**اخر 200 سطر في لوك هيروكو: **"
    )


def prettyjson(obj, indent=4, maxlinelength=80):
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
