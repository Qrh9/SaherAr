from instaloader import Instaloader, Profile
from SHRU import Qrh9
from ..core.managers import edit_or_reply

@Qrh9.ar_cmd(
    pattern="كشانستا(?: |$)(.*)",
    command=("كشانستا", "tools"),
    info={
        "header": "حساب .",
        "description": "ص.",
        "usage": "{tr}كشانستا < >",
    }
)
async def _int(event):
    user1 = event.pattern_match.group(1)
    if not user1:
        return await edit_or_reply(event, "⌔∮ يرجى إدخال اسم مستخدم إنستغرام صالح.")
    
    loader = Instaloader()
    profile = None

    try:
        profile = Profile.from_username(loader.context, user1)
    except Exception as e:
        return await edit_or_reply(event, f"⌔∮ خطأ: {str(e)}")

    pr = f"""
⌔∮ معلومات حساب إنستغرام:
- **الاسم**: {profile.full_name}
- **المتابعين**: {profile.followers}
- **يتابع**: {profile.followees}
- **عدد المنشورات**: {profile.mediacount}
- **البايو**: {profile.biography}
- **خاص/عام**: {"خاص" if profile.is_private else "عام"}
"""
    await edit_or_reply(event, pr)
