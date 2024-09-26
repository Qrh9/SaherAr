import os
from telegraph import Telegraph, upload_file, exceptions
from telethon import events
from SHRU import Qrh9
from ..Config import Config
from ..core.managers import edit_or_reply

telegraph = Telegraph()
telegraph.create_account(short_name=Config.meow)

@Qrh9.ar_cmd(
    pattern="تلجراف ميديا$",
    command=("تلجراف ميديا", "utils"),
    info={
        "header": "رابط تليغراف",
        "usage": "{tr}تلجراف ميديا بالرد على صوره أو فيديو."
    }
)
async def mmes(event):
    reply = await event.get_reply_message()
    
    if not reply or not reply.media:
        return await edit_or_reply(event, "⌔︙يرجى الرد على صورة أو فيديو لاستخدام هذا الأمر.")
    
    jmevent = await edit_or_reply(event, "⌔︙جاري معالجة الوسائط...")
    
    try:
        downloaded_file = await event.client.download_media(reply, Config.TEMP_DIR)
        
        if not downloaded_file:
            return await jmevent.edit("⌔︙حدث خطأ أثناء تحميل الوسائط.")
        
        paths = upload_file(downloaded_file)
        
        os.remove(downloaded_file)
        
        await jmevent.edit(f"⌔︙تم إنشاء الرابط: [اضغط هنا](https://telegra.ph{paths[0]})", link_preview=False)
    
    except exceptions.TelegraphException as e:
        await jmevent.edit(f"⌔︙حدث خطأ: {str(e)}")

    except Exception as e:
        await jmevent.edit(f"⌔︙حدث خطأ غير متوقع: {str(e)}")
