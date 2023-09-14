import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from SHRU import Qrh9

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply

LOGS = logging.getLogger(__name__)
plugin_category = "utils"


# ====================== CONSTANT ===============================
INVALID_MEDIA = "᯽︙ امتدا هذه الصورة غير صالح.```"
PP_CHANGED = "⌔︙**  تم تغير صورة حسابك بنجاح ⌁،**"
PP_TOO_SMOL = "** ᯽︙ هذه الصوره صغيره جدا قم بختيار صوره اخرى  ⌁،**"
PP_ERROR = "** ᯽︙ حدث خطا اثناء معالجه الصوره  ⌁**"
BIO_SUCCESS = "** ᯽︙ تم تغير بايو حسابك بنجاح ⌁،**"
NAME_OK = "** ᯽︙ تم تغير اسم حسابك بنجاح ⌁**"
USERNAME_SUCCESS = "**᯽︙ تم تغير معرف حسابك بنجاح ⌁،**"
USERNAME_TAKEN = "**᯽︙  هذا المعرف مستخدم ⌁ ،**"
# ===============================================================
#ياعلي مدد

@Qrh9.ar_cmd(
    pattern="وضع بايو (.*)",
    command=("وضع بايو", plugin_category),
    info={
        "header": "To set bio for this account.",
        "usage": "{tr}pbio <your bio>",
    },
)
async def _(event):
    "To set bio for this account."
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "᯽︙ تـم تغـيير البـايو بنـجاح ✅")
    except Exception as e:
        await edit_or_reply(event, f"**خطأ:**\n`{str(e)}`")


@Qrh9.ar_cmd(
    pattern="وضع اسم (.*)",
    command=("وضع اسم", plugin_category),
    info={
        "header": "To set/change name for this account.",
        "usage": ["{tr}pname firstname ; last name", "{tr}pname firstname"],
    },
)
async def _(event):
    "To set/change name for this account."
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await edit_delete(event, "᯽︙ تـم تغيير الاسـم بـنجاح ✅")
    except Exception as e:
        await edit_or_reply(event, f"**خطأ:**\n`{str(e)}`")


@Qrh9.ar_cmd(
    pattern="وضع صورة$",
    command=("وضع صورة", plugin_category),
    info={
        "header": "To set profile pic for this account.",
        "usage": "{tr}ppic <reply to image or gif>",
    },
)
async def _(event):
    "To set profile pic for this account."
    reply_message = await event.get_reply_message()
    catevent = await edit_or_reply(
        event, "**...**"
    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e:
        await catevent.edit(str(e))
    else:
        if photo:
            await catevent.edit("᯽︙ أنتـظر قلـيلا ")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await catevent.edit("᯽︙ يجب ان يكون الحجم اقل من 2 ميغا ✅")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(
                        file=catpic, video=catvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:
                await catevent.edit(f"**خطأ:**\n`{str(e)}`")
            else:
                await edit_or_reply(
                    catevent, "᯽︙ تم تغيير الصـورة بنـجاح ✅"
                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))


@Qrh9.ar_cmd(
    pattern="وضع معرف (.*)",
    command=("وضع معرف", plugin_category),
    info={
        "header": "To set/update username for this account.",
        "usage": "{tr}pusername <new username>",
    },
)
async def update_username(username):
    """For .username command, set a new username in Telegram."""
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await edit_or_reply(event, USERNAME_TAKEN)
    except Exception as e:
        await edit_or_reply(event, f"**خطأ:**\n`{str(e)}`")


@Qrh9.ar_cmd(
    pattern="الحساب$",
    command=("الحساب", plugin_category),
    info={
        "header": "To get your profile stats for this account.",
        "usage": "{tr}count",
    },
)
async def count(event):
    """For .count command, get profile stats."""
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    catevent = await edit_or_reply(event, "᯽︙ يتم الحساب انتـظر ")
    dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            LOGS.info(d)

    result += f"**᯽︙ الأشخاص:**\t**{u}**\n"
    result += f"**᯽︙ الـمجموعات:**\t**{g}**\n"
    result += f"**᯽︙ المجموعات الخارقه:**\t**{c}**\n"
    result += f"**᯽︙ القنوات:**\t**{bc}**\n"
    result += f"**᯽︙ البوتات:**\t**{b}**"

    await catevent.edit(result)


@Qrh9.ar_cmd(
    pattern="حذف صوره ?(.*)",
    command=("حذف صوره", plugin_category),
    info={
        "header": "To delete profile pic for this account.",
        "description": "If you havent mentioned no of profile pics then only 1 will be deleted.",
        "usage": ["{tr}delpfp <no of pics to be deleted>", "{tr}delpfp"],
    },
)
async def remove_profilepic(delpfp):
    """For .delpfp command, delete your current profile picture in Telegram."""
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await edit_delete(
        delpfp, f"᯽︙ تـم الحذف {len(input_photos)} من صور حسابك بنجاح ✅"
    )


@Qrh9.ar_cmd(
    pattern="انشائي$",
    command=("انشائي", plugin_category),
    info={
        "header": "To list public channels or groups created by this account.",
        "usage": "{tr}myusernames",
    },
)
async def _(event):
    "To list all public channels and groups."
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "᯽︙ جميع القنوات والمجموعات التي قمت بأنشائها :\n"
    output_str += "".join(
        f" - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats
    )
    await edit_or_reply(event, output_str)

#ملف البروفايل خاص بقناة الساحر
