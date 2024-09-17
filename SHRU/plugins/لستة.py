from telethon.tl.types import InputPeerChannel
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, GetFullChannelRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from SHRU import Qrh9
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

copied_channels = {}

@Qrh9.on(admin_cmd(pattern=r".تقليد_قناة(?: |$)(.*)"))
async def savatage(event):
    channel_username = event.pattern_match.group(1)
    if not channel_username:
        return await event.edit("⌔∮ يرجى تحديد اسم مستخدم القناة لتقليدها.")
    
    try:
        channel = await event.client(JoinChannelRequest(channel_username))
        full_channel = await event.client(GetFullChannelRequest(channel.channel_id))
        copied_channels[full_channel.chats[0].id] = event.chat_id
        await event.edit(f"⌔∮ تم تقليد القناة: {channel_username}.\nأي منشور جديد سيتم نشره في قناتك.")
    except Exception as e:
        await event.edit(f"⌔∮ حدث خطأ: {str(e)}")

@Qrh9.on(admin_cmd(pattern=r".حذف_التقليد(?: |$)(.*)"))
async def riome(event):
    channel_username = event.pattern_match.group(1)
    if not channel_username:
        return await event.edit("⌔∮ يرجى تحديد اسم مستخدم القناة لحذفها.")
    
    try:
        channel = await event.client(JoinChannelRequest(channel_username))
        full_channel = await event.client(GetFullChannelRequest(channel.channel_id))
        if full_channel.chats[0].id in copied_channels:
            del copied_channels[full_channel.chats[0].id]
            await event.edit(f"⌔∮ تم حذف تقليد القناة: {channel_username}.")
        else:
            await event.edit(f"⌔∮ القناة {channel_username} غير موجودة في قائمة القنوات المقلدة.")
    except Exception as e:
        await event.edit(f"⌔∮ حدث خطأ: {str(e)}")

@Qrh9.on(events.NewMessage())
async def nakl(event):
    if event.chat_id in copied_channels:
        target_chat_id = copied_channels[event.chat_id]
        await event.client(ForwardMessagesRequest(
            from_peer=event.chat_id,
            id=[event.id],
            to_peer=target_chat_id
        ))
