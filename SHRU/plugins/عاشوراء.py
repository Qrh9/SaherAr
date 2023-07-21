import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
plugin_category = "utils"
ashour = [
    "أَقِيمُوا الْعَزَاء اُذْكُرُوا سِّيِّد الشَّبَاب قتييل كَرْبَلا ءاِبْن عَلِيّ والزهراء",
    "سأمضي وما بالموت عارٌ على الفتى * إذا ما نوى حقاً وجاهد مسلمًا.",
    "فهل إلاّ الموت ؟ فمرحباً به",
    "أيّها الناس نافِسوا في المكارم وسارعوا في المغانِم.",
    "نَفْسِ مَنْ بَعْدِ الْحُسَيْن هَوِّنِي وَبَعْدَهُ لَا كُنْتِ أَوْ تَكُونِي",
    "هَذَا الْحُسَيْن شَارِب الْمَنُون وتشربين بَارِد الْمُعَيَّن",
    "هَيْهَاتَ مَا هَذَا فَعَّال دِينِي وَلَا فِعَالَ صَادِقٌ الْيَقِين",
    "وَاَللَّه لو قطعـتموا يمـيني",
    "يَا نَفْسُ لَا تخـشي مِن الكفار",
    "نَفْسِ مَنْ بَعْدِ الْحُسَيْن هَوِّنِي وَبَعْدَهُ لَا كُنْتِ أَوْ تَكُونِي",
    "هذا حسينٌ واردُ المَنونِ وتَشْربينَ بارِدَ المَعينِ\n تاللهِ ما هذا فِعالُ دِيني ولا فِعَالُ صَادِقِ اليقينِ",
    ""
]

@l313l.ar_cmd(
    pattern="عاشوراء$",
    command=("عاشوراء", plugin_category),
    info={
        "header": "Get random qusts about عاشوراء (Ashura).",
        "usage": "{tr}عاشوراء",
    },
)
async def ashura_info(event):
    ahsouralshen = random.choice(ashour)
    await edit_or_reply(event, ahsouralshen)