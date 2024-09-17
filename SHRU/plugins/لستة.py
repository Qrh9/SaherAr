from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from SHRU import Qrh9
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from SHRU.utils import admin_cmd

riochannel = {}

@Qrh9.on(admin_cmd(pattern=r".تقليد_قناة(?: |$)(.*)"))
async def clone_channel(event):
    channel_username = event.pattern_match.group(1)
    if not channel_username:
        return await event.edit("⌔∮ يرجى تحديد اسم مستخدم القناة لتقليدها.")
    
    try:
        await event.client(JoinChannelRequest(channel_username))
    except Exception as e:
        return await event.edit(f"⌔∮ حدث خطأ أثناء الانضمام للقناة: {str(e)}")
    
    riochannel[channel_username] = event.chat_id
    await event.edit(f"⌔∮ تم تقليد القناة: {channel_username}.\nأي منشور جديد سيتم نشره في قناتك.")

@Qrh9.on(admin_cmd(pattern=r".حذف_التقليد(?: |$)(.*)"))
async def remove_cloning(event):
    channel_username = event.pattern_match.group(1)
    if not channel_username or channel_username not in riochannel:
        return await event.edit("⌔∮ يرجى تحديد قناة قمت بتقليدها لحذف التقليد.")
    
    del riochannel[channel_username]
    await event.edit(f"⌔∮ تم حذف تقليد القناة: {channel_username}.")

@Qrh9.on(events.NewMessage(chats=riochannel.keys()))
async def forward_to_channel(event):
    target_channel_id = riochannel.get(event.chat.username)
    if target_channel_id:
        try:
            await Qrh9(ForwardMessagesRequest(
                from_peer=event.chat_id,
                id=[event.id],
                to_peer=target_channel_id
            ))
        except Exception as e:
            await event.client.send_message(target_channel_id, f"⌔∮ خطأ أثناء تقليد المنشور: {str(e)}")
