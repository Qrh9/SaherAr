import importlib
import sys
from pathlib import Path

from SHRU import CMD_HELP, LOAD_PLUG

from ..Config import Config
from ..core import LOADED_CMDS, PLG_INFO
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..core.session import Qrh9
from ..helpers.tools import media_type
from ..helpers.utils import _cattools, _catutils, _format, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("SHRU")


def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"SHRU/plugins/{shortname}.py")
        checkplugins(path)
        name = "SHRU.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("᯽︙تم بنجاح تحميل ملف " + shortname)
    else:
        if plugin_path is None:
            path = Path(f"SHRU/plugins/{shortname}.py")
            name = f"SHRU.plugins.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Qrh9
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = Qrh9.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._catutils = _catutils
        mod._cattools = _cattools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        mod.borg = Qrh9
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["SHRU.plugins." + shortname] = mod
        LOGS.info("᯽︙تم بنجاح تحميل ملف ✓" + shortname)


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    Qrh9.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    try:
        for i in LOAD_PLUG[shortname]:
            Qrh9.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    except BaseException:
        pass
    try:
        name = f"SHRU.plugins.{shortname}"
        for i in reversed(range(len(Qrh9._event_builders))):
            ev, cb = Qrh9._event_builders[i]
            if cb.__module__ == name:
                del Qrh9._event_builders[i]
    except BaseException:
        raise ValueError


def checkplugins(filename):
    with open(filename, "r") as f:
        filedata = f.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as f:
        f.write(filedata)


# استدعاء ملفات البوت المساعد
def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"SHRU/plugins/assistant/{shortname}.py")
        name = "SHRU.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("يتم تشغيل البوت المساعد.")
        print("بنجاح تم استدعاء " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"SHRU/plugins/assistant/{shortname}.py")
        name = "SHRU.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["SHRU.plugins.assistant" + shortname] = mod
        print("بنجاح يتم تحميل " + shortname)
