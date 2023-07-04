import io
import json
from datetime import datetime

import aiohttp
import requests
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, gvarstatus
from . import l313l, edit_or_reply, logging, reply_id

plugin_category = "utils"

LOGS = logging.getLogger(__name__)
# Get time zone of the given country. Credits: @aragon12 and @zakaryan2004.
async def get_tz(con):
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


def fahrenheit(f):
    temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
    return temp[0]


def celsius(c):
    temp = str((c - 273.15)).split(".")
    return temp[0]


def sun(unix, ctimezone):
    return datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")

SHRU = "36980ed85a0d7008872784656e7ff2c8"
@l313l.ar_cmd(
    pattern="الطقس(?:\s|$)([\s\S]*)",
    command=("الطقس", plugin_category),
    info={
        "header": "للحصول على معلومات الطقس ",
        "description": "يظهر لك تقرير الطقس لمدينة. بشكل افتراضي هي بغداد .",
        "note": "يجب وضع فار الـ OPEN_WEATHER_MAP_APPID يمكنك الحصول على قيمته من هذا الرابط https://openweathermap.org/",
        "usage": [
            "{tr}الطقس",
            "{tr}الطقس <اسم المدينه>",
        ],
    },
)
async def get_weather(event):  # sourcery no-metrics
    "لعرض معلومات الطقس."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    CITY = gvarstatus("DEFCITY") or "Baghdad" if not input_str else input_str
    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }
    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(event, "- اسم هذه المدينه خطأ تاكد بشكل صحيح")
            CITY = newcity[0].strip() + "," + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={SHRU}"
    async with aiohttp.ClientSession() as _session:
        async with _session.get(url) as request:
            requeststatus = request.status
            requesttext = await request.text()
    result = json.loads(requesttext)
    if requeststatus != 200:
        return await edit_or_reply(event, "- هذا الاسم غير صحيح")
    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    feel = result["main"]["feels_like"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    cloud = result["clouds"]["all"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")
    await edit_or_reply(
        event,
        f"🌡**درجة الحرارة:** `{celsius(curtemp)}°C | {fahrenheit(curtemp)}°F`\n"
        + f"🥰**الشعور الانساني** `{celsius(feel)}°C | {fahrenheit(feel)}°F`\n"
        + f"🥶**درجه الحرارة الصغرى.:** `{celsius(min_temp)}°C | {fahrenheit(min_temp)}°F`\n"
        + f"🥵**درجه الحرارة العظمى.:** `{celsius(max_temp)}°C | {fahrenheit(max_temp)}°F`\n"
        + f"☁️**رطوبة:** `{humidity}%`\n"
        + f"🧧**الضغط** `{pressure} hPa`\n"
        + f"🌬**الرياح:** `{kmph[0]} kmh | {mph[0]} mph, {findir}`\n"
        + f"⛈**سحاب:** `{cloud} %`\n"
        + f"🌄**شروق الشمس:** `{sun(sunrise,ctimezone)}`\n"
        + f"🌅**غروب:** `{sun(sunset,ctimezone)}`\n\n\n"
        + f"**{desc}**\n"
        + f"`{cityname}, {fullc_n}`\n"
        + f"`{time}`\n",
    )
