import os
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply
from telethon.tl.functions.stories import GetStoriesArchive
from telethon.tl.types import InputPeerUser

@Qrh9.on(events.NewMessage(pattern=r".ستوري (.*)"))
async def fetch_stories(event):
    user_input = event.pattern_match.group(1)
    if not user_input:
        return await event.edit_or_reply("⌔∮ يرجى إدخال معرف المستخدم أو ايدي المستخدم.")
    
    try:
        user = await event.Qrh9.get_entity(user_input)
        stories = await event.Qrh9(GetStoriesArchive(peer=InputPeerUser(user_id=user.id, access_hash=user.access_hash)))
        
        if stories and stories.stories:
            for story in stories.stories:
                media = story.media
                await event.Qrh9.download_media(media)
            await event.edit_or_reply(f"⌔∮ تم تنزيل {len(stories.stories)} ستوريات من حساب {user.username}.")
        else:
            await event.edit_or_reply("⌔∮ لا توجد ستوريات مؤرشفة للمستخدم.")
    except Exception as e:
        await event.edit_or_reply(f"⌔∮ حدث خطأ: {str(e)}")
