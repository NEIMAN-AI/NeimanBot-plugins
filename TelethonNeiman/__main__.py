import glob
import os
import sys
from pathlib import Path

from NeimanConfig import Config

from TelethonNeiman.clients.logger import LOGGER as LOGS
from TelethonNeiman.clients.session import H2, H3, H4, H5, Neiman, NeimanBot
from TelethonNeiman.utils.plug import load_module, plug_channel
from TelethonNeiman.utils.startup import (join_it, logger_check, start_msg,
                                        update_sudo)
from TelethonNeiman.version import __hellver__

# Global Variables #
NEIMAN_PIC = "https://te.legra.ph/file/e79e58a483488e23ae815.jpg"


# Client Starter
async def hells(session=None, client=None, session_name="Main"):
    num = 0
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            num = 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
    return num


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as neiman:
            path1 = Path(neiman.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"TelethonNeiman/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))


# Final checks after startup
async def neiman_is_on(total):
    await update_sudo()
    await logger_check(Neiman)
    await start_msg(NeiamnBot, NEIMAN_PIC, __hellver__, total)
    await join_it(Neiman)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# Neimanbot starter...
async def start_Neimanbot():
    try:
        tbot_id = await NeimanBot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        Neiman.tgbot = NeimanBot
        LOGS.info("••• Starting NeimanBot (TELETHON) •••")
        C1 = await hells(Config.NEIMANBOT_SESSION, Hell, "NEIMANBOT_SESSION")
        C2 = await hells(Config.SESSION_2, H2, "SESSION_2")
        C3 = await hells(Config.SESSION_3, H3, "SESSION_3")
        C4 = await hells(Config.SESSION_4, H4, "SESSION_4")
        C5 = await hells(Config.SESSION_5, H5, "SESSION_5")
        await NeimanBot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• NeimanBot Startup Completed •••")
        LOGS.info("••• Starting to load Plugins •••")
        await plug_load("TelethonNeiman/plugins/*.py")
        await plug_channel(Neiman, Config.PLUGIN_CHANNEL)
        LOGS.info("⚡ Your NeimanBot Is Now Working ⚡")
        LOGS.info("Head to @TeamNeiman for Updates. Also join chat group to get help regarding NeimanBot.")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await neiman_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


Neiman.loop.run_until_complete(start_neimanbot())

if len(sys.argv) not in (1, 3, 4):
    Neiman.disconnect()
else:
    try:
        Neiman.run_until_disconnected()
    except ConnectionError:
        pass

