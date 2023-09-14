from geopy.geocoders import Nominatim
from telethon.tl import types

from SHRU import Qrh9

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "extra"


@Qrh9.ar_cmd(
    pattern="موقع ([\s\S]*)",
    command=("موقع", plugin_category),
    info={
        "header": "⌔︙لإرسـال خارطـة الموقـع المعطـى",
        "usage": "{tr}⌔︙موقع <المڪـان> ",
        "examples": "{tr}⌔︙موقع <المڪـان> ",
    },
)
async def gps(event):
    "᯽︙ لإرسـال خارطـة الموقـع المعطـىٰ 🗺"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "** ᯽︙ جاري العثـور على الموقع  … **")
    geolocator = Nominatim(user_agent="catuserbot")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**᯽︙ الموقـع   : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await catevent.delete()
    else:
        await catevent.edit("᯽︙ عـذراً، لـم أستطـع إيجـاده  ⚠️")
