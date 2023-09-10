import datetime
import random
import time
from unicodedata import name

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from TelethonNeiman.DB.gvar_sql import gvarstat, addgvar
from TelethonNeiman.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>⚡ɴᴇɪᴍᴀɴ ɪs ᴏɴʟɪɴᴇ ⚡</i></b>
<b><i>↼ σωиєя ⇀</i></b> : 『 {neiman_mention} 』
╔═══❰𝗡𝗲𝗶𝗺𝗮𝗻𝗕𝗼𝘁❱═══╗
║
┣⪼<b>» υρтιмє:</b> <i>{uptime}</i>
┣⪼<b>» ѕυ∂σ:</b> <i>{is_sudo}</i>
┣⪼<b>» иღιмαив♡т:</b> <i>{neimanbot_version}</i>
┣⪼<b>» тєℓєтнσи:</b> <i>{telethon_version}</i>
║╔═════════╗
║   <b><i>『<a href='https://t.me/TeamNeiman'>[𝗧𝗲𝗮𝗺𝗡𝗲𝗶𝗺𝗮𝗻]</a> 』</i></b>
║╚═════════╝
╚══════════════╝"""
# -------------------------------------------------------------------------------


@neiman_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    neiman = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await neiman.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await neiman.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@neiman_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    userid, neiman_user, neiman_mention = await client_id(event, is_html=True)
    neiman = await eor(event, "`Building Alive....`")
    reply = await event.get_reply_message()
    name = gvarstat("ALIVE_NAME") or neiman_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://te.legra.ph/file/de7d368b013727c198d65.jpg"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        neiman_mention=neiman_mention,
        telethon_version=telethon_version,
        neimanbot_version=neimanbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await neiman.delete()


@neiman_cmd(pattern="neiman$")
async def neiman_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» иღιмαив♡т ιѕ σиℓιиє ««</b>"
    try:
        neiman = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await neiman[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, telethon_version, neimanbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the default Alive message."
).add_command(
    "neiman", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
