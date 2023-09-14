from asyncio import sleep

from SHRU import Qrh9
from SHRU.core.logger import logging

plugin_category = "tools"
LOGS = logging.getLogger(__name__)


@Qrh9.ar_cmd(
    pattern="مؤقت (\d*) ([\s\S]*)",
    command=("مؤقت", plugin_category),
    info={
        "شـرح": "لأرسـال رسـالة موقوتة وحـذفها بعـد وقت معيـن انت تضعـه",
        "⌔︙أسـتخدام": "{tr}مؤقت [الوقت] [النص]",
        "᯽︙ امثـلة": "{tr}مؤقت 10 ههلا",
    },
)
async def selfdestruct(destroy):
    "᯽︙ لأرسـال رسـالة مـوقوتة"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()
