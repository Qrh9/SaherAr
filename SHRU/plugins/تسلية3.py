
import asyncio
from collections import deque

from . import l313l, edit_delete, edit_or_reply, mention

plugin_category = "fun"


@l313l.ar_cmd(
    pattern="نجمه$",
    command=("نجمه", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}نجمه",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "`نجمه.....`")
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@l313l.ar_cmd(
    pattern="مكعبات$",
    command=("مكعبات", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}مكعبات",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "`مكعبات...`")
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@l313l.ar_cmd(
    pattern="مطر$",
    command=("مطر", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}مطر",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "`مطر.......`")
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@l313l.ar_cmd(
    pattern="deploy$",
    command=("deploy", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}deploy",
    },
)
async def _(event):
    "animation command"
    animation_interval = 3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "`Deploying...`")
    animation_chars = [
        "**Heroku Connecting To Latest Github Build **",
        f"**Build started by user** {mention}",
        f"**Deploy** `535a74f0` **by user** {mention}",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m SHRU`",
        "**State changed from starting to up**",
        "__INFO:SHRU:Logged in as 557667062__",
        "__INFO:SHRU:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@l313l.ar_cmd(
    pattern="تفريغ(?: |$)(.*)",
    command=("تفريغ", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}تفريغ <ثلاث سمايلات>",
        "examples": ["{tr}تفريغ", "{tr}تفريغ 🍰🍎🐓"],
    },
)
async def _(event):
    "Animation Command"
    try:
        obj = event.pattern_match.group(1)
        if len(obj) != 3:
            return await edit_delete(event, "`Input length must be 3 or empty`")
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    event = await edit_or_reply(event, "`تفريغ....`")
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            await event.edit(something_else)


@l313l.ar_cmd(
    pattern="فليم$",
    command=("فليم", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}فليم",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    event = await edit_or_reply(event, "فليم....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@l313l.ar_cmd(
    pattern="احبك$",
    command=("احبك", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}احبك",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "احبك")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
        "❤",
        "احبك ❤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@l313l.ar_cmd(
    pattern="طائره$",
    command=("طائره", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}طائره",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "انتظر الطائره...")
    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)


@l313l.ar_cmd(
    pattern="شرطه$",
    command=("شرطه", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}شرطه",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "شرطه")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        f"{mention} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@l313l.ar_cmd(
    pattern="jio$",
    command=("jio", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}jio",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(19)
    event = await edit_or_reply(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Optimising JIO NETWORK...*",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ █`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@l313l.ar_cmd(
    pattern="النضام الشمسي$",
    command=("النضام الشمسي", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}النضام الشمسي",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await edit_or_reply(event, "النضام الشمسي")
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
