from SHRU import Qrh9
from ..core.managers import edit_or_reply
from datetime import datetime


prayer_times = {
    "الامساك": "04:45",
    "الفجر": "04:55",
    "الشروق": "06:17",
    "الظهر": "12:13",
    "العصر": "15:36",
    "المغرب (الفطور)": "18:09",
    "العشاء": "19:27"
}

@Qrh9.ar_cmd(
    pattern="كم باقي$",
    command=("كم باقي", plugin_category),
    info={
        "header": "الوقت المتبقي للصلاة او الافطار",
        "description": "يعرض الوقت الحالي والوقت المتبقي للصلاة التالية.",
        "usage": "{tr}كم باقي",
    },
)
async def countdown_next_prayer(event):
    """عد تنازلي للصلاة."""
    now = datetime.now()
    current_time_str = now.strftime("%H:%M")
    remaining_time = None
    next_prayer = None
    for prayer, time_str in prayer_times.items():
        prayer_time = datetime.strptime(time_str, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
        if prayer_time > now:
            remaining_time = prayer_time - now
            next_prayer = prayer
            break
    if remaining_time and next_prayer:
        message = f"الوقت الحالي: {current_time_str}\nالوقت المتبقي لصلاة {next_prayer}: {remaining_time}"
    else:
        message = "لا يوجد صلوات متبقية اليوم."
    await edit_or_reply(event, message)