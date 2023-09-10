import asyncio
import os
from pathlib import Path

from TelethonNeiman.plugins import *


@neiman_cmd(pattern="cmds$")
async def kk(event):
    event.message.id
    if event.reply_to_msg_id:
        event.reply_to_msg_id
    cids = await client_id(event)
    fuck_uff_XD, NEIMAN_USER, neiman_mention = cids[0], cids[1], cids[2]
    cmd = "ls TelethonNeiman/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"""
<h1>List of Plugins in NeimanBot:</h1>

<code>{o}</code>

<b><i>HELP:</b></i> <i>ιf уσυ ωαит тσ киσω тнє ¢σммαи∂ѕ fσя α ρℓυgιи, ∂σ “ .ρℓιиfσ <ρℓυgιи иαмє> ”

<b><a href='https://t.me/TeamNeimanν>@TeamNeiman</a></b>
"""
    neiman = await telegraph_paste("αℓℓ αναιℓαвℓє ρℓυgιиѕ ιи иєιмαиẞø†", OUTPUT)
    await eor(event, f"[αℓℓ αναιℓαвℓє ρℓυgιиѕ ιи ẞø†]({hell})", link_preview=False)


@neiman_cmd(pattern="send ([\s\S]*)")
async def send(event):
    cids = await client_id(event)
    fuck_uff_XD, NEIMAN_USER, neiman_mention = cids[0], cids[1], cids[2]
    message_id = event.reply_to_msg_id or event.message.id
    thumb = neiman_logo
    input_str = event.pattern_match.group(1)
    omk = f"**• Plugin name ≈** `{input_str}`\n**• Uploaded by ≈** {neimna_mention}\n\n⚡ **[Team Neiman]({chnl_link})** ⚡"
    the_plugin_file = "./TelethonNeiman/plugins/{}.py".format(input_str.lower())
    if os.path.exists(the_plugin_file):
        await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await parse_error(event, f"No plugin named {input_str.lower()}")


@neiman_cmd(pattern="install(?:\s|$)([\s\S]*)")
async def install(event):
    cids = await client_id(event)
    fuck_uff_XD, NEIMAN_USER, neiman_mention = cids[0], cids[1], cids[2]
    b = 1
    owo = event.text[9:]
    neiman = await eor(event, "__ιиѕтαℓℓιиg.__")
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "./TelethonNeiman/plugins/",  # pylint:disable=E0602
                )
            )
            if owo != "-f":
                op = open(downloaded_file_name, "r")
                rd = op.read()
                op.close()
                try:
                    for harm in HARMFUL:
                        if harm in rd:
                            os.remove(downloaded_file_name)
                            return await neiman.edit(
                                f"**⚠️ ωαяиιиg !!** \n\n__яєρℓιє∂ ρℓυgιи fιℓє ¢σитαιиѕ ѕσмє нαямfυℓ ¢σ∂єѕ. ρℓєαѕє ¢σиѕι∂єя ¢нє¢кιиg тнє fιℓє. ιf уσυ ѕтιℓℓ ωαит тσ ιиѕтαℓℓ тнєи υѕє__ `{hl}install -f`. \n\n**¢σ∂єѕ ∂єтє¢тє∂ :** \n• {harm}"
                            )
                except BaseException:
                    pass
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**¢σммαи∂ѕ fσυи∂ ιи** `{}`\n".format(
                        (os.path.basename(downloaded_file_name))
                    )
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i
                        string += "`\n"
                        if b == 1:
                            a = "__ιиѕтαℓℓιиg..__"
                            b = 2
                        else:
                            a = "__ιиѕтαℓℓιиg...__"
                            b = 1
                        await neiman.edit(a)
                    return await neiman.edit(
                        f"✅ **ιиѕтαℓℓє∂ мσ∂υℓє** :- `{shortname}` \n✨ BY :- {neiman_mention}\n\n{string}\n\n        ⚡ **[ Team Neiman]({chnl_link})** ⚡",
                        link_preview=False,
                    )
                return await neiman.edit(
                    f"ιиѕтαℓℓє∂ мσ∂υℓє `{os.path.basename(downloaded_file_name)}`"
                )
            else:
                os.remove(downloaded_file_name)
                return await parse_error(hell, f"мσ∂υℓє αℓяєα∂у ιиѕтαℓℓє∂ σя υикиσωи fσямαт.")
        except Exception as e:
            await parse_error(neiman, e)
            return os.remove(downloaded_file_name)


@neiman_cmd(pattern="uninstall ([\s\S]*)")
async def uninstall(event):
    shortname = event.text[11:]
    if ".py" in shortname:
        shortname = shortname.replace(".py", "")
    neiman = await eor(event, f"__тяуιиg тσ υиιиѕтαℓℓ ρℓυgιи__ `{shortname}` ...")
    dir_path = f"./TelethonNeiman/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await eod(neiman, f"**υиιиѕтαℓℓє∂ ρℓυgιи** `{shortname}` **successfully.**")
    except OSError as e:
        await parse_error(neiman, f"`{dir_path}` : __{e.strerror}__", False)


@neiman_cmd(pattern="unload ([\s\S]*)")
async def unload(event):
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await eod(event, f"ѕυ¢¢єѕѕfυℓℓу υиℓσα∂є∂ `{shortname}`")
    except Exception as e:
        await parse_error(event, e)


@neiman_cmd(pattern="load ([\s\S]*)")
async def load(event):
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await eod(event, f"ѕυ¢¢єѕѕfυℓℓу ℓσα∂є∂ `{shortname}`")
    except Exception as e:
        await parse_error(event, e)


CmdHelp("core").add_command(
    "install", "<reply to a .py file>", "ιиѕтαℓℓѕ тнє яєρℓιє∂ ρутнσи fιℓє ιf ѕυιтαвℓє иєιмαивσт.`\n** fℓαgѕ :** `-f"
).add_command(
    "uninstall", "<plugin name>", "υиιиѕтαℓℓѕ тнє gινєи ρℓυgιи fяσм иєιмαиẞø†. тσ gєт тнαт αgαιи ∂σ .restart", "uninstall alive"
).add_command(
    "load", "<plugin name>", "ℓσα∂єѕ тнє υиℓσα∂є∂ ρℓυgιи тσ уσυя вσт", "load alive"
).add_command(
    "unload", "<plugin name>", "υиℓσα∂ѕ тнє ρℓυgιи fяσм уσυя bot", "unload alive"
).add_command(
    "send", "<file name>", "ѕєи∂ѕ тнє gινєи fιℓє fяσм уσυя υѕєявσт ѕєяνєя, ιf αиу.", "send alive"
).add_command(
    "cmds", None, "gινєѕ συт тнє ℓιѕт σf мσ∂υℓєѕ ιи Bot."
).add_command(
    "repo", None, "gινєѕ вσт'ѕ gιтнυв яєρσ ℓιик."
).add_command(
    "help", None, "ѕнσωѕ ιиℓιиє нєℓρ мєиυ."
).add_command(
    "plinfo", "<plugin name>", "ѕнσωѕ тнє ∂єтαιℓє∂ ιиfσямαтισи σf gινєи ρℓυgιи."
).add_command(
    "cmdinfo", "<cmd name>", "ѕнσωѕ тнє ιиfσямαтισи σf gινєи ¢σммαи∂."
).add_warning(
    "⚡ιиѕтαℓℓ єχтєяиαℓ ρℓυgιиѕ σи уσυяσωи яιѕк."
).add()
