from SHRU import Qrh9
from telethon import events
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest

@Qrh9.on(events.NewMessage(pattern=r"^.مرر$", outgoing=True))
async def forward_to_channels(event):
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()

        if replied_msg:
            if replied_msg.from_id.bot and replied_msg.text:
                import re
                links = re.findall(r'https?://[^\s]+', replied_msg.text)

                for link in links:
                    try:
                        await Qrh9(JoinChannelRequest(link))
                        await Qrh9.send_message(link, '\start')
                    except Exception as e:
                        print(f"Error: {str(e)}")
                    finally:
                        await asyncio.sleep(2)
    else:
        await event.reply("رد على رسالة اشتراك اجباري.")