import importlib
import logging
import os
import sys
from pathlib import Path

from NeimanConfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from TelethonNeiman.clients.client_list import client_id
from TelethonNeiman.clients.decs import neiman_cmd
from TelethonNeiman.clients.logger import LOGGER as LOGS
from TelethonNeiman.clients.session import H2, H3, H4, H5, Neiman, NeimanBot
from TelethonNeiman.utils.cmds import CmdHelp
from TelethonNeiman.utils.decorators import admin_cmd, command, sudo_cmd
from TelethonNeiman.utils.extras import delete_neiman, edit_or_reply
from TelethonNeiman.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import TelethonNeiman.utils

        path = Path(f"TelethonNeiman/plugins/{shortname}.py")
        name = "TelethonNeiman.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("NeimanBot - Successfully imported " + shortname)
    else:
        import TelethonNeiman.utils

        path = Path(f"TelethonNeiman/plugins/{shortname}.py")
        name = "TelethonNeiman.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Neiman
        mod.H1 = Neiman
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Neiman = Neiman
        mod.NeimanBot = NeimanBot
        mod.tbot = NeimanBot
        mod.tgbot = Neiman.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Neiman
        mod.neimanbot = Neiman
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_neiman = delete_neiman
        mod.eod = delete_neiman
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.neiman_cmd = neiman_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = TelethonNeiman
        sys.modules["userbot"] = TelethonNeiman
        sys.modules["userbot.events"] = TelethonNeiman
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["TelethonNeiman.plugins." + shortname] = mod
        LOGS.info("🔥 иღιмαив♡т 🔥 - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Neiman.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"TelethonNeiman.plugins.{shortname}"

            for i in reversed(range(len(Neiman._event_builders))):
                ev, cb = Neiman._event_builders[i]
                if cb.__module__ == name:
                    del Neiman._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("🔥 иღιмαив♡т 🔥 - PLUGIN CHANNEL DETECTED.")
        LOGS.info("🔥 иღιмαив♡т 🔥 - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"TelethonNeiman/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "TelethonNeiman/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))
