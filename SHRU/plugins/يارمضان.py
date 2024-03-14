from SHRU import Qrh9
from ..core.managers import edit_or_reply
from datetime import datetime
import random
from telethon import events
plugin_category = "fun"
#str 122939
quranic_verses = [
    "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ - البقرة 153",
    "وَاصْبِرْ وَمَا صَبْرُكَ إِلَّا بِاللَّهِ - النحل 127",
    "وَلَنَبْلُوَنَّكُم بِشَيْءٍ مِنَ الْخَوْفِ وَالْجُوعِ وَنَقْصٍ مِنَ الْأَمْوَالِ وَالْأَنفُسِ وَالثَّمَرَاتِ - البقرة 155",
    "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا - الطلاق 2",
    "وَمَن يَتَوَكَّلْ عَلَى اللَّهِ فَهُوَ حَسْبُهُ - الطلاق 3",
"إِنَّ اللَّهَ يُحِبُّ الْمُتَوَكِّلِينَ - آل عمران 159",
"فَاذْكُرُونِي أَذْكُرْكُمْ - البقرة 152",
"وَتَوَكَّلْ عَلَى الْعَزِيزِ الرَّحِيمِ - الشعراء 217",
"إِنَّ رَبِّي لَسَمِيعُ الدُّعَاء - إبراهيم 39",
"فَسَبِّحْ بِحَمْدِ رَبِّكَ وَكُن مِّنَ السَّاجِدِينَ - الحجر 98",
"وَاستَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ - البقرة 45",
"وَمَا كَانَ اللَّهُ مُعَذِّبَهُمْ وَهُمْ يَسْتَغْفِرُونَ - الأنفال 33",
"وَأَقِيمُوا الصَّلَاةَ وَآتُوا الزَّكَاةَ - البقرة 43",
"فَإِنَّ مَعَ الْعُسْرِ يُسْرًا - الشرح 6",
"وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ - يوسف 87",
]
hadiths = [
    "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ - الكافي",
    "مَنْ صَلَّى عَلَيَّ وَاحِدَةً صَلَّى اللَّهُ عَلَيْهِ عَشْرًا - الكافي",
    "الصَّدَقَةُ تَدْفَعُ مِيتَةَ السُّوءِ - الكافي",
    "صِلْ مَنْ قَطَعَكَ وَأَعْطِ مَنْ حَرَمَكَ وَاعْفُ عَمَّنْ ظَلَمَكَ - الكافي",
    "العِلْمُ خَيْرٌ مِنَ الْمَالِ - الكافي",
"الْعِلْمُ نُورٌ يَقْذِفُهُ اللَّهُ فِي قَلْبِ مَنْ يَشَاءُ - الكافي",
"مَنْ عَرَفَ نَفْسَهُ فَقَدْ عَرَفَ رَبَّهُ - نهج البلاغة",
"الصَّمْتُ بَابٌ مِنْ أَبْوَابِ الْحِكْمَةِ - نهج البلاغة",
"أَفْضَلُ الْجِهَادِ جِهَادُ النَّفْسِ - الكافي",
"الْعَفْوُ عِنْدَ الْمَقْدِرَةِ زِينَةُ الْأَقْوِيَاءِ - نهج البلاغة",
"أَقْرَبُكُمْ مِنِّي مَجْلِسًا أَحَاسِنُكُمْ أَخْلَاقًا - الكافي",
"الصَّبْرُ مِنَ الْإِيمَانِ كَالرَّأْسِ مِنَ الْجَسَدِ - الكافي",
"مَنْ زَارَ قَبْرَ أَخِيهِ الْمُؤْمِنِ كَتَبَ اللَّهُ لَهُ ثَوَابَ حَاجٍّ وَمُعْتَمِرٍ - الكافي",
"أَفْضَلُ الْعِبَادَةِ انْتِظَارُ الْفَرَجِ - الكافي",
"الْجَنَّةُ تَحْتَ أَقْدَامِ الْأُمَّهَاتِ - الكافي",
]
prayer_times = {
    "الفجر": "04:55",
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
        message = (f"الوقت الحالي: {current_time_str}\nالوقت المتبقي لأذان {next_prayer}: {remaining_time.seconds // 3600} ساعة و {(remaining_time.seconds % 3600) // 60} دقيقة متبقية")
    else:
        message = "لا يوجد صلوات متبقية اليوم."
    await edit_or_reply(event, message)





@Qrh9.ar_cmd(
    pattern="آية$",
    command=("آية", plugin_category),
    info={
        "header": "أمر لجلب آية قرآنية عشوائية.",
        "description": "يُرسل آية قرآنية عشوائية.",
        "usage": "{tr}آية",
    },
)
async def random_quranic_verse(event):
    """ارسال ايات من القران """
    verse = random.choice(quranic_verses)
    await edit_or_reply(event, verse)

@Qrh9.ar_cmd(
    pattern="حديث$",
    command=("حديث", plugin_category),
    info={
        "header": "أمر لجلب حديث عشوائي.",
        "description": "يُرسل حديث عشوائي.",
        "usage": "{tr}حديث",
    },
)
async def random_hadith(event):
    """ارسال احاديث عشوائيه من نهج البلاغه والكافي الشعيه."""
    hadith = random.choice(hadiths)
    await edit_or_reply(event, hadith)
    
    #بوكهن ميخالف لان حتى هاي متدبرها وحدك




@Qrh9.on(events.NewMessage(pattern='.سباق'))
async def emoji_race(event):
    emojis = ["🍉", "🍎", "🍌", "🍇", "🍓", "🍍", "🍊", "🍐", "🍒", "🥝"]
    race_Emoji = random.choice(emojis)
    race_start_time = datetime.now()
    await edit_or_reply(event,f"اول واحد يرسل هذا الايموجي {race_Emoji} يربح نقطة!")

    async with Qrh9.conversation(event.chat_id) as conv:
        while True:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern=race_Emoji))
            if response.sender_id != event.sender_id:
                break

    race_end_time = datetime.now()
    time_taken = (race_end_time - race_start_time).total_seconds()
    winner = await Qrh9.get_entity(response.sender_id)
    await edit_or_reply(event,f"🎉 مبروك {winner.first_name}! لقد فزت بالسباق في {time_taken} ثواني! لقد فزت وحصلت على نقطة!")