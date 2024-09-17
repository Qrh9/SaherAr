import os
from telethon import events
from telethon.tl.functions.messages import GetStoriesRequest, DownloadMediaRequest
from SHRU import Qrh9
from ..core.managers import edit_or_reply

@Qrh9.on(events.NewMessage(pattern=r".ستوري (.*)"))
async def onichan(event):
    user_input = event.pattern_match.group(1)
    
    if not user_input:
        return await event.respond("⌔∮ يرجى إدخال معرف المستخدم أو آيدي المستخدم")
    
    try:
        entity = await Qrh9.get_entity(user_input)
        stories = await Qrh9(GetStoriesRequest(entity))
        
        if not stories.items:
            return await event.respond("⌔∮ لا توجد ستوريات متاحة لهذا المستخدم")
        
        download_folder = f"./downloads/{entity.id}/stories/"
        os.makedirs(download_folder, exist_ok=True)
        
        for story in stories.items:
            file_path = os.path.join(download_folder, f"{story.id}.jpg")
            
            await Qrh9.download_media(story.media, file_path)
            await event.client.send_file(event.chat_id, file_path, caption=f"⌔∮ ستوري من {entity.first_name}")
        
        await event.respond(f"⌔∮ تم تنزيل جميع ستوريات المستخدم: {entity.first_name}")
        
    except Exception as e:
        await event.respond(f"⌔∮ حدث خطأ: {str(e)}")

