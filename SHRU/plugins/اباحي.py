# ها حبيبي تره بعدني ممسوي لما اكمل اخمطه
import os

import requests

from SHRU import Qrh9

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"

@Qrh9.Rio_cmd(
    pattern="اباحي$",
    command=("اباحي", plugin_category),
    info={
        "header": "للكشف عن العري في الصورة المرتدة.",
        "description": "أمر الكشف عن العري في أي صورة أو ملصق غير متحرك للكشف عن العري فيها",
        "usage": "{tr}كشف",
    },
)
async def detect(event):
    "اكو استنياج لو لا؟."
    if Config.DEEP_AI is None:
        return await edit_delete(
            event, "لازم تعين المتغير `DEEP_AI`تكدر تحصله منا    https://deepai.org/", 5
        )
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "`رد على أي صورة أو ملصق  !`", 5
        )
    catevent = await edit_or_reply(event, "`ثواني حبيبي  ...`")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):#اذا شسمه وذا مو شسمه شسمه
        return await edit_delete(
            event, "`رد على ملصق او صوره !`", 5
        )
    catevent = await edit_or_reply(event, "`الكشف عن الاباحي ...`")
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",#كسمه
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Config.DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await edit_delete(catevent, r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b>تم اكتشاف الاباحي غطيها يمعود:</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"
    if detections := r_json["detections"]:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"<b>• {name}:</b>\n   <code>{confidence} %</code>\n"
    await edit_or_reply(
        catevent,
        result,
        link_preview=False,
        parse_mode="HTML",
     
)