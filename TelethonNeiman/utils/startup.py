from NeimanConfig import Config
from telethon import Button
from telethon.tl import functions
from telethon.tl.types import ChatAdminRights
from TelethonNeiman.clients.logger import LOGGER as LOGS
from TelethonNeiman.DB.gvar_sql import addgvar, gvarstat
from TelethonNeiman.helpers.int_str import make_int
from TelethonNeiman.version import __telever__



async def logger_id(client):
    desc = "α вσт ℓσggєя gяσυρ fσя иєιмαивσт. ∂σ иσт ℓєανє тнιѕ gяσυρ !!"
    try:
        grp = await client(
            functions.channels.CreateChannelRequest(
                title="𝗡𝗲𝗶𝗺𝗮𝗻𝗕𝗼𝘁 𝗟𝗼𝗴𝗴𝗲𝗿 ", about=desc, megagroup=True
            )
        )
        grp_id = grp.chats[0].id
    except Exception as e:
        LOGS.error(f"{str(e)}")
        return
    
    if not str(grp_id).startswith("-100"):
        grp_id = int("-100" + str(grp_id))
    
    try:
        new_rights = ChatAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            manage_call=True,
        )
        grp = await client(functions.messages.ExportChatInviteRequest(peer=grp_id))
        await client(
            functions.channels.InviteToChannelRequest(
                channel=grp_id, users=[Config.BOT_USERNAME]
            )
        )
        await client(
            functions.channels.EditAdminRequest(
                grp_id, Config.BOT_USERNAME, new_rights, "Helper"
            )
        )
    except Exception as e:
        LOGS.error(f"{str(e)}")

    return grp_id



async def update_sudo():
    Sudo = Config.SUDO_USERS
    sudo = gvarstat("SUDO_USERS")
    if sudo:
        int_list = await make_int(gvarstat("SUDO_USERS"))
        for x in int_list:
            Sudo.append(x)



async def logger_check(bot):
    if Config.LOGGER_ID == 0:
        if gvarstat("LOGGER_ID") is None:
            grp_id = await logger_id(bot)
            addgvar("LOGGER_ID", grp_id)
            Config.LOGGER_ID = grp_id
        Config.LOGGER_ID = int(gvarstat("LOGGER_ID"))


async def start_msg(client, pic, version, total):
    is_sudo = "True" if Config.SUDO_USERS else "False"
    text = f"""
ɴᴇɪᴍᴀɴʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛᴇᴀᴍ ɴᴇɪᴍᴀɴ

<b><i>νєяѕισи:</b></i> <code>{version}</code>
<b><i>ѕυ∂σ:</b></i> <code>{is_sudo}</code>
<b><i>ƈℓιєитѕ:</b></i> <code>{str(total)}</code>
<b><i>ℓιвяαяу:</b></i> <code>ᴛᴇʟᴇᴛʜᴏɴ - {__telever__}</code>

<b><i>⚡ <u><a href='https://t.me/TeamNeiman'>иღιмαив♡т</a></u> ⚡⚡</i></b>
"""
    await client.send_file(
        Config.LOGGER_ID,
        pic,
        caption=text,
        parse_mode="HTML",
        buttons=[[Button.url("ᴛᴇᴀᴍ ɴᴇɪᴍᴀɴ ", "https://t.me/TeamNeiman")]],
    )


async def join_it(client):
    if client:
        try:
            await client(functions.channels.JoinChannelRequest("@TeamNeiman"))
            await client(functions.messages.ImportChatInviteRequest("@Neiman_X_Support"))
        except BaseException:
            pass

