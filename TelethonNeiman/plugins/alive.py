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
<b><i>🔥🔥иღιмαив♡т ɨs օռʟɨռɛ🔥🔥</i></b>
<b><i>↼ Øwñêr ⇀</i></b> : 『 {neiman_mention} 』
╭──────────────
┣─ <b>» Telethon:</b> <i>{telethon_version}</i>
┣─ <b>» иღιмαив♡т:</b> <i>{neimanbot_version}</i>
┣─ <b>» Sudo:</b> <i>{is_sudo}</i>
┣─ <b>» Uptime:</b> <i>{uptime}</i>
┣─ <b>» Ping:</b> <i>{ping}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/TeamNeiman'>[иღιмαив♡т]</a> «««</i></b>
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>иღιмαив♡т ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
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
    uptime = await get_time((time.time() - StartTime))
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
        PIC = "https://te.legra.ph/file/8338a235da86c7456b92d.mp4"
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


@neiman_cmd(pattern="hell$")
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
