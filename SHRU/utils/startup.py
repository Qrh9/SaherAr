import time
import asyncio
import glob
import os
import sys
from telethon.errors.rpcerrorlist import ChannelPrivateError
import urllib.request
from datetime import timedelta
from pathlib import Path
import requests
from telethon import Button, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from SHRU import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from aiohttp import web
from ..core import web_server
from ..core.logger import logging
from ..core.session import Qrh9
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("SHRU")
##Reda hands here
cmdhr = Config.COMMAND_HAND_LER
bot = Qrh9
ENV = bool(os.environ.get("ENV", False))

if ENV:
    VPS_NOLOAD = ["سيرفر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هيروكو"]

async def check_dyno_type():
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.heroku.com/apps/{Config.HEROKU_APP_NAME}/dynos", headers=headers) as resp:
            if resp.status == 200:
                dynos = await resp.json()
                for dyno in dynos:
                    if dyno["type"] != "standard-1X":
                        return False
            else:
                return False
    return True

async def setup_bot():
    """
    To set up bot for SHRU
    """
    try:
        await Qrh9.connect()
        config = await Qrh9(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == Qrh9.session.server_address:
                if Qrh9.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙معرف ثابت في الجلسة من {Qrh9.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                Qrh9.session.set_dc(option.id, option.ip_address, option.port)
                Qrh9.session.save()
                break
        bot_details = await Qrh9.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        redaport = Config.PORT
        await web.TCPSite(app, bind_address, redaport).start()
        Qrh9.me = await Qrh9.get_me()
        Qrh9.uid = Qrh9.tgbot.uid = utils.get_peer_id(Qrh9.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(Qrh9.me)
        if not check_dyno_type:
            LOGS.error("قد تحدث مشكلة ولن يعمل السورس لان نوع الداينو ليس بيسك قم بتحويله الى basic")
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await Qrh9.tgbot.send_file(
                BOTLOG_CHATID,
                "https://t.me/i1Voices/2139",
                caption="**‏᯽︙ بــوت الساحر يـعـمـل بـنـجـاح ✓ \n᯽︙ أرسل `.الاوامر`لرؤية اوامر السورس \n  ᯽︙ لأستعمال بوت الأختراق عبر كود التيرمكس أرسل`.هاك`**",
                buttons=[(Button.url("سورس الساحر", "https://t.me/SXYO3"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await Qrh9.check_testcases()
            message = await Qrh9.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**تم تشغيل البوت الأن أرسل `.فحص`**"
            await Qrh9.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await Qrh9.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    JEPTH_USER = Qrh9.me.first_name
    The_noon = Qrh9.uid
    jep_ment = f"[{JEPTH_USER}](tg://user?id={The_noon})"
    f"ـ {jep_ment}"
    f"⪼ هذا هو بوت خاص بـ {jep_ment} يمكنك التواصل معه هنا"
    starkbot = await Qrh9.tgbot.get_me()
    perf = "الساحر ✨"
    bot_name = starkbot.first_name
    botname = f"@{starkbot.username}"
    if bot_name.endswith("Assistant"):
        if not starkbot.inline_query_enabled:
            print(" (inline) معطل للبوت")
            return
        print("تم تشغيل البوت")
    else:
        try:
            await Qrh9.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await Qrh9.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await Qrh9.send_message("@BotFather", perf)
            await asyncio.sleep(2)
        except Exception as e:
            print(e)

async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = requests.get("https://ipv4.jsonip.com/").json()["ip"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await Qrh9.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await Qrh9.tgbot.get_me()
    try:
        await Qrh9(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await Qrh9(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))
#by @SXYO3 بس اشوفك خامطه للكود اهينك وافضحك
SHRU = {"@SXYO3", "@Qrh9X", "@SXYO4"}
async def saves():
   for SX9OO in SHRU:
        try:
             await Qrh9(JoinChannelRequest(channel=SX9OO))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue
        except ChannelPrivateError:
            continue
                
async def load_plugins(folder, extfolder=None):
    """
    تحميل ملفات السورس
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"SHRU/{folder}/*.py"
        plugin_path = f"SHRU/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لم يتم تحميل {shortname} بسبب خطأ {e}\nمسار الملف {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await Qrh9.tgbot.send_message(
            BOTLOG_CHATID,
            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`',
        )

async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await Qrh9.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
        except ValueError:
            LOGS.error("᯽︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")
        except TypeError:
            LOGS.error(
                "᯽︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."
            )
        except Exception as e:
            LOGS.error(
                "᯽︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "- عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها  - @SXYO3"
        photobt = await Qrh9.upload_file(file="Qrh9/razan/resources/start/ALSAHER.JPEG")
        _, groupid = await create_supergroup(
            "مجموعة أشعارات الساحر ", Qrh9, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("᯽︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await Qrh9.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙الأذونات مفقودة لإرسال رسائل لـ PM_LOGGER_GROUP_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙الأذونات مفقودة للمستخدمين الإضافيين لـ PM_LOGGER_GROUP_ID المحدد."
                    )
        except ValueError:
            LOGS.error("᯽︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. تأكد من صحتها.")
        except TypeError:
            LOGS.error("᯽︙PM_LOGGER_GROUP_ID غير مدعوم. تأكد من صحتها.")
        except Exception as e:
            LOGS.error(
                "⌯︙حدث استثناء عند محاولة التحقق من PM_LOGGER_GROUP_ID.\n" + str(e)
            )
    else:
        descript = "᯽︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي \n  - @SXYO3"
        photobt = await Qrh9.upload_file(file="Qrh9/razan/resources/start/ALSAHER2.JPEG")
        _, groupid = await create_supergroup(
            "مجموعة التخزين", Qrh9, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "SHRU"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)

async def install_externalrepo(repo, branch, cfolder):
    jokerREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if jokerBRANCH := branch:
        repourl = os.path.join(jokerREPO, f"tree/{jokerBRANCH}")
        gcmd = f"git clone -b {jokerBRANCH} {jokerREPO} {cfolder}"
        errtext = f"لا يوحد فرع بأسم `{jokerBRANCH}` في الريبو الخارجي {jokerREPO}. تاكد من اسم الفرع عبر فار (`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = jokerREPO
        gcmd = f"git clone {jokerREPO} {cfolder}"
        errtext = f"الرابط ({jokerREPO}) الذي وضعته لفار `EXTERNAL_REPO` غير صحيح عليك وضع رابط صحيح"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await Qrh9.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا "
        )
        return await Qrh9.tgbot.send_message(
            BOTLOG_CHATID,
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا ",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="SHRU", extfolder=cfolder)
