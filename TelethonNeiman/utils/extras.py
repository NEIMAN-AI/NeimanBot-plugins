import asyncio
import os
import re

from NeimanConfig import Config
from TelethonNeiman.helpers.pasters import pasty



async def edit_or_reply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    deflink=False,
    noformat=False,
    linktext=None,
    caption=None,
):
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096 and not deflink:
        parse_mode = parse_mode or "md"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    if not noformat:
        asciich = ["**", "`", "__"]
        for i in asciich:
            text = re.sub(rf"\{i}", "", text)
    if aslink or deflink:
        linktext = linktext or "Message was to big so pasted to bin"
        response = await pasty(event, text)
        text = linktext + f"[BIN]({response['url']}) •• [RAW]({response['raw']})"
        if event.sender_id in Config.SUDO_USERS:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        await event.edit(text, link_preview=link_preview)
        return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in Config.SUDO_USERS:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)



async def delete_neiman(event, text, time=None, parse_mode=None, link_preview=None):
    parse_mode = parse_mode or "md"
    link_preview = link_preview or False
    time = time or 10
    if event.sender_id in Config.SUDO_USERS:
        reply_to = await event.get_reply_message()
        neimanevent = (
            await reply_to.reply(text, link_preview=link_preview, parse_mode=parse_mode)
            if reply_to
            else await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        )
    else:
        neimanevent = await event.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
    await asyncio.sleep(time)
    return await neimanevent.delete()


async def parse_error(event, error, auto_parse=True, delete=True, time=10):
    if delete:
        if auto_parse:
            await delete_hell(event, f"**ERROR !!** \n\n`{error}`", time)
        else:
            await delete_hell(event, f"**ERROR !!** \n\n{error}", time)
    else:
        if auto_parse:
            await edit_or_reply(event, f"**ERROR !!** \n\n`{error}`")
        else:
            await edit_or_reply(event, f"**ERROR !!** \n\n{error}")

