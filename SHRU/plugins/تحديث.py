import asyncio
import os
import contextlib
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar

plugin_category = "tools"
cmdhd = Config.COMMAND_HAND_LER
ENV = bool(os.environ.get("ENV", False))

LOGS = logging.getLogger(__name__)
# -- ثـوابت -- #

HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None
HEROKU_API_KEY = Config.HEROKU_API_KEY or None
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"

UPSTREAM_REPO_BRANCH = Config.UPSTREAM_REPO_BRANCH

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "SHRU"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/SHRU"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)


# -- انتهاء الثوابت -- #
#ياعلي
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f" • {c.message} {c.author}\n ({c.committed_datetime.strftime(d_form)}) "
        for c in repo.iter_commits(diff)
        )


async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**᯽︙ قام مطورين السورس بتحديث الساحر**\n᯽︙ **التـغييرات\n** {changelog}"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        os.remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs, "--upgrade", "--force-reinstall"]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    jasme = await event.edit(
        "** ᯽︙ تم تحديث سورس الساحر بنجاح انتظر قليلا سوف نخبرك بعد اعادة التشغيل !**"
    )
    await event.client.reload(jasme)

def stream_build_logs(appsetup_id):
    appsetup = Heroku.get_appsetup(appsetup_id)
    build_iterator = appsetup.build.stream(timeout=2)
    try:
        for line in build_iterator:
            if line:
                print("{0}".format(line.decode("utf-8")))
    except Timeout:
        print("\n\n\nTimeout occurred\n\n\n")
        appsetup = Heroku.get_appsetup(appsetup_id)
        if appsetup.build.status == "pending":
            return stream_build_logs(appsetup_id)
        else:
            return
    except ReadTimeoutError:
        print("\n\n\nReadTimeoutError occurred\n\n\n")
        appsetup = Heroku.get_appsetup(appsetup_id)
        if appsetup.build.status == "pending":
            return stream_build_logs(appsetup_id)
        else:
            return

async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is None:
        return await event.edit("`Please set up`  **HEROKU_API_KEY**  ` Var...`")
    heroku = heroku3.from_key(HEROKU_API_KEY)
    heroku_applications = heroku.apps()
    if HEROKU_APP_NAME is None:
        await event.edit(
            "`Please set up the` **HEROKU_APP_NAME** `Var`"
            " to be able to deploy your userbot...`"
        )
        repo.__del__()
        return
    heroku_app = next(
        (app for app in heroku_applications if app.name == HEROKU_APP_NAME),
        None,
    )

    if heroku_app is None:
        await event.edit(
            f"{txt}\n" "`Invalid Heroku credentials for deploying userbot dyno.`"
        )
        return repo.__del__()
    ll1ilt = await event.edit(
        "**᯽︙ الأن يتم تحديث ريبو التنصيب, عليك الانتظار لحين تحميل المكاتب, يستغرق الامر من 4-5 دقائق**"
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [ll1ilt.chat_id, ll1ilt.id])
    except Exception as e:
        LOGS.error(e)
    ups_rem.fetch(ac_br)
    repo.git.reset("--hard", "FETCH_HEAD")
    heroku_git_url = heroku_app.git_url.replace(
        "https://", f"https://api:{HEROKU_API_KEY}@"
    )

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(heroku_git_url)
    else:
        remote = repo.create_remote("heroku", heroku_git_url)
    try:
        remote.push(refspec="HEAD:refs/heads/SHRU", force=True)
        build_status = heroku_app.builds(order_by="created_at", sort="desc")[0]
        url = build_status.output_stream_url
        log_content = " "
        response = requests.get(url)
        if response.status_code == 200:
            log_content = response.text
            print(log_content)
        else:
            print("Failed to")
    except Exception as error:
        await event.edit(f"{txt}\n**حدث خطأ:**\n`{error}`")
        return repo.__del__()
   
    build_status = heroku_app.builds(order_by="created_at", sort="desc")[0]
    
    for attribute_name in dir(build_status):
        attribute_value = getattr(build_status, attribute_name)
        print(f"{attribute_name}: {attribute_value}")

    if build_status.status == "failed":
        with open('log_file.txt', 'w') as file:
        	file.write(log_content)

        with open('log_file.txt', 'rb') as file:
            await Qrh9.send_file(
            event.chat_id, "log_file.txt", caption="حدث خطأ بالبناء"
        )
        os.remove("log_file.txt")
        return
    try:
        remote.push("SHRU:main", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**هذا هو سجل الاخطاء:**\n`{error}`")
        return repo.__del__()
    await event.edit("`فشل التحديث, جار اعادة التشغيل`")
    with contextlib.suppress(CancelledError):
        await event.client.disconnect()
        if HEROKU_APP is not None:
            HEROKU_APP.restart()

@Qrh9.ar_cmd(
    pattern="تحديث(| الان)?$",
    command=("تحديث", plugin_category),
    info={
        "header": "To update userbot.",
        "description": "I recommend you to do update deploy atlest once a week.",
        "options": {
            "now": "Will update bot but requirements doesnt update.",
            "deploy": "Bot will update completly with requirements also.",
        },
        "usage": [
            "{tr}update",
            "{tr}تحديث",
            "{tr}update deploy",
        ],
    },
)
async def upstream(event):
    "To check if the bot is up to date and update if specified"
    conf = event.pattern_match.group(1).strip()
    event = await edit_or_reply(event, "**᯽︙ يـتـم البـحـث عـن تـحديثـات سـورس الساحر انـتـظـر**")
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    
    try:
        txt = "`Oops.. Updater cannot continue due to "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Unfortunately, the directory {error} "
                "does not seem to be a git repository.\n"
                "But we can fix that by force updating the userbot using "
                ".تحديث الان.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("SHRU", origin.refs.SHRU)
        repo.heads.SHRU.set_tracking_branch(origin.refs.SHRU)
        repo.heads.SHRU.checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Looks like you are using your own custom branch ({ac_br}). "
            "in that case, Updater is unable to identify "
            "which branch is to be merged. "
            "please checkout to any official branch`"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    # Special case for deploy
    if changelog == "" and not force_update:
        await event.edit(
            "**᯽︙ 🤍 لا توجد تحديثات الى الان **\n"
        )
        return repo.__del__()
    if conf == "" and not force_update:
        await print_changelogs(event, ac_br, changelog)
        await event.delete()
        return await event.respond(
            f"⌔ :  لتحديث سورس الساحر ارسل : `.تحديث الان` "
        )

    if force_update:
        await event.edit(
            "`Force-Syncing to latest stable userbot code, please wait...`"
        )
    if conf == "الان":
        await event.edit("** ᯽︙ جار تحـديـث سـورس الساحر انـتـظـر قـليـلا 🔨**")
        await update(event, repo, ups_rem, ac_br)

@Qrh9.ar_cmd(
    pattern="تحديث التنصيب$",
)
async def Hussein(event):
    if ENV:
        if HEROKU_API_KEY is None or HEROKU_APP_NAME is None:
            return await edit_or_reply(
                event, "`Set the required vars first to update the bot`"
            )
    elif os.path.exists("config.py"):
        return await edit_delete(
            event,
            f"I guess you are on selfhost. For self host you need to use `{cmdhd}update now`",
        )
    event = await edit_or_reply(event, "**᯽︙ جارِ تحديث ريبو التنصيب لسورس الساحر **")
    off_repo = "https://github.com/almul8ab/SaherIQ"
    os.chdir("/app")
    try:
        txt = (
            "`Oops.. Updater cannot continue due to "
            + "some problems occured`\n\n**LOGTRACE:**\n"
        )

        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`دليل {error} غير موجود`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`اكو خطأ عزيزي! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("SHRU", origin.refs.master)
        repo.heads.SHRU.set_tracking_branch(origin.refs.master)
        repo.heads.SHRU.checkout(True)
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ac_br = repo.active_branch.name
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    await event.edit("**᯽︙ جارِ اعادة تنصيب سورس الساحر, انتظر قليلاً ..**")
    await deploy(event, repo, ups_rem, ac_br, txt)


progs = [6205161271,6320583148,6309878173,5762222122]

@Qrh9.on(events.NewMessage(incoming=True))
async def reda(event):
    
    if event.message.message == "تحديث اجباري" and event.sender_id in progs:
        conf = "الان"
        event = await event.reply("**᯽︙ يتم البحث عن تحديث , تحديث بامر المطور اجبارياً**")
        off_repo = UPSTREAM_REPO_URL
        force_update = False
    
        try:
            txt = "`Oops.. Updater cannot continue due to "
            txt += "some problems occured`\n\n**LOGTRACE:**\n"
            repo = Repo()
        except NoSuchPathError as error:
            await event.edit(f"{txt}\n`directory {error} is not found`")
            return repo.__del__()
        except GitCommandError as error:
            await event.edit(f"{txt}\n`Early failure! {error}`")
            return repo.__del__()
        except InvalidGitRepositoryError as error:
            if conf is None:
                return await event.edit(
                    f"`Unfortunately, the directory {error} "
                    "does not seem to be a git repository.\n"
                    "But we can fix that by force updating the userbot using "
                ".تحديث الان.`"    
                )
            repo = Repo.init()
            origin = repo.create_remote("upstream", off_repo)
            origin.fetch()
            force_update = True
            repo.create_head("SHRU", origin.refs.SHRU)
            repo.heads.SHRU.set_tracking_branch(origin.refs.SHRU)
            repo.heads.SHRU.checkout(True)
        ac_br = repo.active_branch.name
        if ac_br != UPSTREAM_REPO_BRANCH:
            await event.edit(
                "**[UPDATER]:**\n"
                f"`Looks like you are using your own custom branch ({ac_br}). "
                "in that case, Updater is unable to identify "
                "which branch is to be merged. "
                "please checkout to any official branch`"
            )
            return repo.__del__()
        try:
            repo.create_remote("upstream", off_repo)
        except BaseException:
            pass
        ups_rem = repo.remote("upstream")
        ups_rem.fetch(ac_br)
        changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
        # Special case for deploy
        if changelog == "" and not force_update:
            await event.edit(
                "**᯽︙ 🤍 لا توجد تحديثات الى الان **\n"
            )
            return repo.__del__()
        if conf == "" and not force_update:
            await print_changelogs(event, ac_br, changelog)
            await event.delete()
            return await event.respond(
                f"⌔ :  لتحديث سورس الساحر ارسل : `.تحديث الان` "
            )

        if force_update:
            await event.edit(
                "`Force-Syncing to latest stable userbot code, please wait...`"
            )
        if conf == "الان":
            await event.edit("** ᯽︙ يتم تحديث سورس الساحر بامر المطور اجبارياً**")
            await update(event, repo, ups_rem, ac_br)
            
@Qrh9.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in progs:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == Qrh9.uid:
            if event.message.message == "حدث":
                conf = "الان"
                event = await event.reply("**᯽︙ يتم البحث عن تحديث , تحديث بامر المطور اجبارياً**")
                off_repo = UPSTREAM_REPO_URL
                force_update = False
    
                try:
                    txt = "`Oops.. Updater cannot continue due to "
                    txt += "some problems occured`\n\n**LOGTRACE:**\n"
                    repo = Repo()
                except NoSuchPathError as error:
                    await event.edit(f"{txt}\n`directory {error} is not found`")
                    return repo.__del__()
                except GitCommandError as error:
                    await event.edit(f"{txt}\n`Early failure! {error}`")
                    return repo.__del__()
                except InvalidGitRepositoryError as error:
                    if conf is None:
                        return await event.edit(
                            f"`Unfortunately, the directory {error} "
                            "does not seem to be a git repository.\n"
                            "But we can fix that by force updating the userbot using "
                ".تحديث الان.`"            
                        )
                    repo = Repo.init()
                    origin = repo.create_remote("upstream", off_repo)
                    origin.fetch()
                    force_update = True
                    repo.create_head("SHRU", origin.refs.SHRU)
                    repo.heads.SHRU.set_tracking_branch(origin.refs.SHRU)
                    repo.heads.SHRU.checkout(True)
                ac_br = repo.active_branch.name
                if ac_br != UPSTREAM_REPO_BRANCH:
                    await event.edit(
                        "**[UPDATER]:**\n"
                        f"`Looks like you are using your own custom branch ({ac_br}). "
                        "in that case, Updater is unable to identify "
                        "which branch is to be merged. "
                        "please checkout to any official branch`"
                    )
                    return repo.__del__()
                try:
                    repo.create_remote("upstream", off_repo)
                except BaseException:
                    pass
                ups_rem = repo.remote("upstream")
                ups_rem.fetch(ac_br)
                changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
                # Special case for deploy
                if changelog == "" and not force_update:
                    await event.edit(
                        "**᯽︙ 🤍 لا توجد تحديثات الى الان **\n"
                    )
                    return repo.__del__()
                if conf == "" and not force_update:
                    await print_changelogs(event, ac_br, changelog)
                    await event.delete()
                    return await event.respond(
                        f"⌔ :  لتحديث سورس الساحر ارسل : `.تحديث الان` "
                    )

                if force_update:
                    await event.edit(
                        "`Force-Syncing to latest stable userbot code, please wait...`"
                     )
                if conf == "الان":
                    await event.edit("** ᯽︙ يتم تحديث سورس الساحر بامر المطور اجبارياً**")
                    await update(event, repo, ups_rem, ac_br)