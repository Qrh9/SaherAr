from SHRU import Qrh9
from ..core.managers import edit_or_reply
from datetime import datetime
import random
import asyncio
import akinator
from telethon import events
plugin_category = "fun"
#str 122939#المليون

    
#تكدر تضيف بعد وره ال plus
A_qq = [
    {"aW": "ما هو الحيوان الذي يمتلك أكبر عدد من الأسنان؟", "choices": ["التمساح", "القرش", "الفيل"], "Wa": "القرش"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'Au'؟", "choices": ["الذهب", "الفضة", "النحاس"], "Wa": "الذهب"},
    {"aW": "ما هي أكبر قارة في العالم؟", "choices": ["آسيا", "أفريقيا", "أوروبا"], "Wa": "آسيا"},
    {"aW": "من هو مؤلف رواية 'البؤساء'؟", "choices": ["فيكتور هوغو", "شارلز ديكنز", "ليو تولستوي"], "Wa": "فيكتور هوغو"},
    {"aW": "ما هي اللغة الرسمية للبرازيل؟", "choices": ["البرتغالية", "الإسبانية", "الإنجليزية"], "Wa": "البرتغالية"},
    {"aW": "ما هو أعمق محيط في العالم؟", "choices": ["المحيط الهادئ", "المحيط الأطلسي", "المحيط الهندي"], "Wa": "المحيط الهادئ"},
    {"aW": "من هو مخترع المصباح الكهربائي؟", "choices": ["توماس إديسون", "ألكسندر جراهام بيل", "نيكولا تسلا"], "Wa": "توماس إديسون"},
    {"aW": "ما هي عاصمة اليابان؟", "choices": ["طوكيو", "أوساكا", "كيوتو"], "Wa": "طوكيو"},
    {"aW": "من هو مؤلف كتاب 'الإخوان كارامازوف'؟", "choices": ["فيودور دوستويفسكي", "ليو تولستوي", "أنطون تشيخوف"], "Wa": "فيودور دوستويفسكي"},
    {"aW": "ما هو الطائر الذي يمكنه الطيران للخلف؟", "choices": ["الطنان", "النسر", "البومة"], "Wa": "الطنان"},
    {"aW": "ما هي أصغر دولة في العالم؟", "choices": ["الفاتيكان", "موناكو", "ناورو"], "Wa": "الفاتيكان"},
    {"aW": "ما هو أطول نهر في العالم؟", "choices": ["نهر النيل", "نهر الأمازون", "نهر يانغتسي"], "Wa": "نهر النيل"},
    {"aW": "من هو مؤلف مسرحية 'هاملت'؟", "choices": ["ويليام شكسبير", "سوفوكليس", "موليير"], "Wa": "ويليام شكسبير"},
    {"aW": "ما هو الكوكب الأصغر في المجموعة الشمسية؟", "choices": ["عطارد", "بلوتو", "المريخ"], "Wa": "عطارد"},
    {"aW": "من هو مؤلف رواية 'الحرب والسلام'؟", "choices": ["ليو تولستوي", "فيودور دوستويفسكي", "أنطون تشيخوف"], "Wa": "ليو تولستوي"},
    {"aW": "ما هو أقدم جامعة في العالم؟", "choices": ["جامعة القرويين", "جامعة بولونيا", "جامعة أكسفورد"], "Wa": "جامعة القرويين"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'O'؟", "choices": ["أكسجين", "أوزون", "أوسميوم"], "Wa": "أكسجين"},
    {"aW": "ما هي عملة اليابان؟", "choices": ["الين", "الوون", "اليوان"], "Wa": "الين"},
    {"aW": "من هو مؤلف مسرحية 'مكبث'؟", "choices": ["ويليام شكسبير", "كريستوفر مارلو", "بن جونسون"], "Wa": "ويليام شكسبير"},
    {"aW": "ما هو الحيوان الوطني لأستراليا؟", "choices": ["الكنغر", "الكوالا", "الإيمو"], "Wa": "الكنغر"},
    {"aW": "ما هي أكبر دولة في أفريقيا من حيث المساحة؟", "choices": ["الجزائر", "السودان", "ليبيا"], "Wa": "الجزائر"},
    {"aW": "ما هو أطول نفق في العالم؟", "choices": ["نفق سانت غوتارد", "نفق سيكان", "نفق لوشبرغ"], "Wa": "نفق سانت غوتارد"},
    {"aW": "ما هي أكبر جزيرة في العالم؟", "choices": ["غرينلاند", "نيو غينيا", "بورنيو"], "Wa": "غرينلاند"},
    {"aW": "من هو مؤلف كتاب 'الأمير'؟", "choices": ["نيكولو مكيافيلي", "توماس هوبز", "جون لوك"], "Wa": "نيكولو مكيافيلي"},
    {"aW": "ما هي الدولة التي تضم مدينة البندقية؟", "choices": ["إيطاليا", "فرنسا", "إسبانيا"], "Wa": "إيطاليا"},
    {"aW": "من هو مخترع الراديو؟", "choices": ["غوليلمو ماركوني", "نيكولا تسلا", "ألكسندر جراهام بيل"], "Wa": "غوليلمو ماركوني"},
    {"aW": "ما هي عاصمة كندا؟", "choices": ["أوتاوا", "تورونتو", "مونتريال"], "Wa": "أوتاوا"},
    {"aW": "ما هو أقدم علم في العالم؟", "choices": ["علم الرياضيات", "علم الفلك", "علم الكيمياء"], "Wa": "علم الفلك"},
    {"aW": "ما هي أصغر دولة في أفريقيا؟", "choices": ["سيشيل", "غامبيا", "موريشيوس"], "Wa": "سيشيل"},
    {"aW": "ما هو البركان الأكثر نشاطاً في العالم؟", "choices": ["كيلاويا", "إتنا", "فيزوف"], "Wa": "كيلاويا"},
    {"aW": "ما هي اللغة الرسمية للأرجنتين؟", "choices": ["الإسبانية", "البرتغالية", "الإنجليزية"], "Wa": "الإسبانية"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'Fe'؟", "choices": ["الحديد", "الفلور", "الفرانسيوم"], "Wa": "الحديد"},
    {"aW": "ما هي عاصمة جنوب أفريقيا؟", "choices": ["بريتوريا", "كيب تاون", "جوهانسبرغ"], "Wa": "بريتوريا"},
    {"aW": "من هو مؤلف كتاب 'الأخوة كارامازوف'؟", "choices": ["فيودور دوستويفسكي", "ليو تولستوي", "أنطون تشيخوف"], "Wa": "فيودور دوستويفسكي"},
    {"aW": "ما هو الحيوان الذي يعيش أطول عمراً؟", "choices": ["السلحفاة", "الفيل", "الببغاء"], "Wa": "السلحفاة"},
    {"aW": "ما هو أصغر كوكب في المجموعة الشمسية؟", "choices": ["عطارد", "بلوتو", "المريخ"], "Wa": "عطارد"},
    {"aW": "ما هي اللغة الرسمية لمصر؟", "choices": ["العربية", "الإنجليزية", "الفرنسية"], "Wa": "العربية"},
    {"aW": "من هو مؤلف كتاب 'الجمهورية'؟", "choices": ["أفلاطون", "أرسطو", "سقراط"], "Wa": "أفلاطون"},
    {"aW": "ما هي عاصمة الهند؟", "choices": ["نيودلهي", "مومباي", "بنغالور"], "Wa": "نيودلهي"}
]

qq = [
    {"aW": "ما هو أطول نهر في العالم؟", "choices": ["النيل", "الأمازون", "المسيسيبي"], "Wa": "الأمازون"},
    {"aW": "من هو مؤلف رواية 'البؤساء'؟", "choices": ["فيكتور هوغو", "تشارلز ديكنز", "ليو تولستوي"], "Wa": "فيكتور هوغو"},
    {"aW": "كم عدد الكواكب في نظامنا الشمسي؟", "choices": ["8", "9", "10"], "Wa": "8"},
]
Io = [
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
    verse = random.choice(Io)
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


@Qrh9.ar_cmd(
    pattern="المارد$",
    command=("المارد", plugin_category),
    info={
        "header": "امر المارد السحري الازرك.",
        "description": "مكتبة المارد الازرق ا .",
        "usage": "{tr}المارد",
    },
)
async def akinator_game(event):
    aki = akinator.Akinator()
    q = aki.start_game(language='ar')

    async with Qrh9.conversation(event.chat_id) as conv:
        question_msg = await edit_or_reply(event,
            f"{q}\n\n"
            "اجب ب:\n"
            "`y` = نعم\n"
            "`n` = لا\n"
            "`idk` = لا اعلم\n"
            "`p` = من الممكن\n"
            "`c` = انهاء اللعبة\n"
            "`b` = رجوع"
        )
        while aki.progression <= 80:
            response = await conv.wait_event(events.NewMessage(from_users=event.sender_id))
            a = response.text
            await response.delete()
            if a.lower() == "c":
                await question_msg.edit("لقد ألغيت اللعبة.")
                return
            elif a.lower() == "b":
                try:
                    q = aki.back()
                except akinator.CantGoBackAnyFurther:
                    pass
            else:
                q = aki.answer(a)
            await question_msg.edit(
                f"{q}\n\n"
                "اجب ب:\n"
                "`y` = نعم\n"
                "`n` = لا\n"
                "`idk` = لا اعلم\n"
                "`p` = من الممكن\n"
                "`c` = انهاء اللعبة\n"
                "`b` = رجوع"
            )
        aki.win()

        correct = await edit_or_reply(event, f"هل هو [{aki.first_guess['name']}]({aki.first_guess['absolute_picture_path']}) ({aki.first_guess['description']})؟ هل كنت محقًا؟")
        response = await conv.wait_event(events.NewMessage(from_users=event.sender_id))
        if response.text.lower() in ["yes", "y", "نعم", "أجل"]:
            await correct.reply("ياي\n")
        else:
            await correct.reply("أوف\n")

@Qrh9.on(events.NewMessage(pattern='.سباق'))
async def emoji_race(event):
    emojis = ["🍉", "🍎", "🍌", "🍇", "🍓", "🍍", "🍊", "🍐", "🍒", "🥝"]
    race_Emoji = random.choice(emojis)
    Po = datetime.now()
    await edit_or_reply(event,f"اول واحد يرسل هذا الايموجي {race_Emoji} يربح نقطة!")

    async with Qrh9.conversation(event.chat_id) as conv:
        while True:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern=race_Emoji))
            if response.sender_id != event.sender_id:
                break

    race_end_time = datetime.now()
    time_taken = (race_end_time - Po).total_seconds()
    Wi = await Qrh9.get_entity(response.sender_id)
    await response.reply(f"🎉 مبروك [{Wi.first_name}](tg://user?id={Wi.id}) \n- ثواني: {int(time_taken)} !!", parse_mode="md")
    

@Qrh9.on(events.NewMessage(pattern='.اصابع'))
async def rock_paper_scissors(event):
    choices = {
        "حجرة": "ورقة",
        "ورقة": "مقص",
        "مقص": "حجرة"
    }
    user_choice = event.text.split()[-1]

    if user_choice not in choices:
        await edit_or_reply(event, "يرجى اختيار واحد من الخيارات التالية: حجرة، ورقة، أو مقص.")
        return

    bot_choice = random.choice(list(choices.keys()))
    if user_choice == bot_choice:
        result = "تعادل!"
    elif choices[bot_choice] == user_choice:
        result = "🎉 مبروك! لقد فزت."
    else:
        result = "😢 لقد خسرت. حاول مرة أخرى."

    await edit_or_reply(event, f"اختيارك: {user_choice}\nاختيار الساحر: {bot_choice}\nنتيجة اللعبة: {result}")




@Qrh9.on(events.NewMessage(pattern='.سيارات'))
async def car_race(event):
    racers = []
    Kk = None
    await edit_or_reply(event, "التسجيل بدأ ارسل 1 للانضمام")

    async with Qrh9.conversation(event.chat_id) as conv:
        while len(racers) < 5:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern="1"))
            if response.sender_id not in [r[0] for r in racers]:
                racer_entity = await Qrh9.get_entity(response.sender_id)
                racers.append((response.sender_id, racer_entity.username or racer_entity.first_name))
                Kk = await response.reply("تم التسجيل بنجاح")

    track = ["🏎️" for _ in range(5)]
    await Kk.edit(
        "السباق يبدأ الآن!\n" +
        "\n".join([f"{i+1}- {track[i]} [{racers[i][1]}](https://t.me/{racers[i][1]})" for i in range(5)])
    )

    for _ in range(10):
        await asyncio.sleep(1)
        moving_car = random.randint(0, 4)
        track[moving_car] = "-" + track[moving_car]
        await Kk.edit(
            "السباق يبدأ الآن!\n" + "\n".join([f"{i+1}- {track[i]} [{racers[i][1]}](https://t.me/{racers[i][1]})" for i in range(5)])
        )

    winner = racers[moving_car]
    await Kk.edit(
        f"🎉 مبروك [{winner[1]}](https://t.me/{winner[1]})! لقد فزت بالسباق!"
    )
    
#بالحظ
@Qrh9.ar_cmd(
    pattern="تحدي$",
    command=("تحدي", plugin_category),
    info={
        "header": "Challenge another user to a duel.",
        "description": "Randomly selects a Wi between the challenger and the opponent.",
        "usage": "{tr}تحدي",
    },
)
async def challenge(event):
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "يرجى الرد على رسالة المستخدم الذي تريد تحديه.")
        return

    reply_message = await event.get_reply_message()
    opponent = reply_message.sender_id
    challenger = event.sender_id

    Wi = random.choice([challenger, opponent])
    Wi_entity = await Qrh9.get_entity(Wi)

    await edit_or_reply(event, f"🎊 تهانينا [{Wi_entity.first_name}](tg://user?id={Wi})! لقد فزت في التحدي!")
    

@Qrh9.ar_cmd(
    pattern="المليون$",
    command=("المليون", plugin_category),
    info={
        "header": "Play a million game.",
        "description": "لعبه مثل مال من سيربح المليون",
        "usage": "{tr}المليون",
    },
)
async def million(event):
    Bq = qq + A_qq
    aW = random.choice(Bq)
    choices = aW["choices"][:]
    random.shuffle(choices)
    choices_text = "\n".join([f"{i+1}. {choice}" for i, choice in enumerate(choices)])
    await edit_or_reply(event, f"{aW['aW']}\n\n{choices_text}\n\nاكتب رقم الإجابة الصحيحة:")

    async with Qrh9.conversation(event.chat_id) as conv:
        response = await conv.wait_event(events.NewMessage(pattern=r'^[1-3]$', from_users=event.sender_id))
        Wa_index = int(response.text) - 1
        if choices[Wa_index] == aW["Wa"]:
            await response.reply("🎉 صحيح! إجابتك صحيحة.")
        else:
            await response.reply(f"❌ خطأ! الإجابة الصحيحة هي: {aW['Wa']}")