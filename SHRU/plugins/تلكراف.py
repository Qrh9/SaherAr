import os
import random
import string
from datetime import datetime
from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from telethon.utils import get_display_name
from SHRU import Qrh9
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_or_reply
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "utils"

telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")

@Qrh9.ar_cmd(
    pattern="(ت(ل)?ك(راف)?) ?(m|t|ميديا|نص)(?:\s|$)([\s\S]*)",
    command=("تلكراف", plugin_category),
    info={
        "header": "To get telegraph link.",
        "description": "Reply to text message to paste that text on telegraph you can also pass input along with command.",
        "usage": [
            "{tr}tgm",
            "{tr}tgt <title(optional)>",
        ],
    },
)
async def _(event):
    jmevent = await edit_or_reply(event, "`⌔︙جـار انشـاء رابـط تلكـراف...`")

    optional_title = event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await jmevent.edit("⌔︙قـم بالـرد على الرسالة للحـصول على رابط تلكراف.")

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()

    if input_str in ["ميديا", "m"]:
        downloaded_file_name = await event.client.download_media(r_message, Config.TEMP_DIR)
        await jmevent.edit(f"⌔︙تـم التحـميل الـى {downloaded_file_name}")

        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)

        try:
            media_urls = upload_file(downloaded_file_name)
            
            if isinstance(media_urls, list) and len(media_urls) > 0:
                media_url = media_urls[0]
            else:
                raise ValueError(f"الاستجابة غير صحيحة من Telegraph: {media_urls}")
        except exceptions.TelegraphException as exc:
            await jmevent.edit(f"⌔︙خـطأ : \n`{exc}`")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await jmevent.edit(
                f"⌔︙الـرابـط : [اضغط هنا](https://telegra.ph{media_url})\n⌔︙الوقـت المستغرق : `{ms} ثـواني.`",
                link_preview=False,
            )