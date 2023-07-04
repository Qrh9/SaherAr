import pyfiglet
from SHRU import l313l
from SHRU.helpers.utils import _format
from SHRU.core.managers import edit_delete, edit_or_reply
from SHRU.plugins import _format, l313l, deEmojify

plugin_category = "utils"

CMD_FIG = {

    "slant": "slant",

    "3D": "3-d",

    "5line": "5lineoblique",

    "alpha": "alphabet",

    "banner": "banner3-D",

    "doh": "doh",

    "basic": "basic",

    "binary": "binary",

    "iso": "isometric1",

    "letter": "letters",

    "allig": "alligator",

    "dotm": "dotmatrix",

    "bubble": "bubble",

    "bulb": "bulbhead",

    "digi": "digital",

}

@l313l.ar_cmd(
    pattern="تشكيل(?:\s|$)([\s\S]*)",
    command=("تشكيل", plugin_category),
    info={
        "header": "للترفيه",
        "description": "تشكيل النص",
        "styles": [
            "slant",
            "3D",
            "5line",
            "alpha",
            "banner",
            "doh",
            "iso",
            "letter",
            "allig",
            "dotm",
            "bubble",
            "bulb",
            "digi",
            "binary",
            "basic",
        ],
    },
)




async def figlet(event):

    "تغيير ستايل النص للستايل المُختار"

    input_str = event.pattern_match.group(1)

    if ";" in input_str:

        cmd, text = input_str.split(";", maxsplit=1)

    elif input_str:

        cmd = None

        text = input_str

    else:

        await edit_or_reply(event, "`ضع نص للتشكيل`")

        return

    style = cmd

    text = text.strip()

    if style is not None:

        try:

            font = CMD_FIG[style.strip()]

        except KeyError:

            return await edit_delete(

                event, "**لا يوجد هكذا ستايل**, __Check__ `.info figlet`."

            )

        result = pyfiglet.figlet_format(deEmojify(text), font=font)

    else:

        result = pyfiglet.figlet_format(deEmojify(text))

    await edit_or_reply(event, result, parse_mode=_format.parse_pre)
