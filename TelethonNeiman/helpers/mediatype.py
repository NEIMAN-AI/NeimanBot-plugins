from TelethonNeiman.clients.logger import LOGGER as LOGS
from TelethonNeiman.helpers.formats import yaml_format
from TelethonNeiman.helpers.progress import humanbytes


async def mediadata(e_media):
    neiman = ""
    if e_media.file.name:
        neiman += f"📍 NAME :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        neiman += f"📍 MIME TYPE :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        neiman += f"📍 SIZE :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        neiman += f"📍 DATE :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        neiman += f"📍 ID :  {e_media.file.id}<br>"
    if e_media.file.ext:
        neiman += f"📍 EXTENSION :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        neiman += f"📍 EMOJI :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        neiman += f"📍 TITLE :  {e_media.file.title}<br>"
    if e_media.file.performer:
        neiman += f"📍 PERFORMER :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        neiman += f"📍 DURATION :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        neiman += f"📍 HEIGHT :  {e_media.file.height}<br>"
    if e_media.file.width:
        neiman += f"📍 WIDTH :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        neiman += f"📍 STICKER SET :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            neiman += f"📍 Thumb  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return neiman


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None
