from telethon import events
from telethon.tl.functions.messages import DeleteMessagesRequest
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import TLObject

class ReactionEmoji(TLObject):
    CONSTRUCTOR_ID = 0x1b2286b8
    SUBCLASS_OF_ID = 0x5da165a1

    def __init__(self, emoticon: str):
        """
        Constructor for Reaction: Instance of either ReactionEmpty, ReactionEmoji, ReactionCustomEmoji.
        """
        self.emoticon = emoticon

    def to_dict(self):
        return {
            '_': 'ReactionEmoji',
            'emoticon': self.emoticon
        }

    def _bytes(self):
        return b''.join((
            b'\xb8\x86"\x1b',
            self.serialize_bytes(self.emoticon),
        ))

    @classmethod
    def from_reader(cls, reader):
        _emoticon = reader.tgread_string()
        return cls(emoticon=_emoticon)

from SHRU import Qrh9
import random 
from SHRU.utils import admin_cmd

iz3aj_active = {}
emoje = ["😂", "🤯", "👍", "😅"]

@Qrh9.on(admin_cmd(pattern=r".ازعاج (.*)"))
async def start_iz3aj(event):
    emoji = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not reply:
        return await event.respond("⌔∮ يرجى الرد على رسالة الشخص.")
    
    user_id = reply.sender_id
    iz3aj_active[user_id] = emoji or random.choice(emoje)  
    await event.respond(f"⌔∮ تم تفعيل الإزعاج بهذا الإيموجي {emoji} للشخص.")

@Qrh9.on(admin_cmd(pattern=r".حذف_ازعاج"))
async def stop_iz3aj(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.respond("⌔∮ يرجى الرد على رسالة الشخص.")
    
    user_id = reply.sender_id
    if user_id in iz3aj_active:
        del iz3aj_active[user_id]
        await event.respond("⌔∮ تم إلغاء الإزعاج للشخص.")
    else:
        await event.respond("⌔∮ لا يوجد إزعاج مفعّل لهذا الشخص.")

@Qrh9.on(events.NewMessage())
async def iz3a(event):
    if event.sender_id in iz3aj_active:
        emoji = iz3aj_active.get(event.sender_id)
        if not emoji:
            emoji = random.choice(emoje)

        try:
            await Qrh9(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=emoji)]
            ))
        except Exception as e:
            await event.respond(f"خطأ: {str(e)}")