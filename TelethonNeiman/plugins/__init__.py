from HellConfig import Config, db_config, os_config
from TelethonHell.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from TelethonHell.clients.decs import hell_cmd, hell_handler
from TelethonHell.clients.instaAPI import InstaGram
from TelethonHell.clients.logger import LOGGER
from TelethonHell.clients.session import (H2, H3, H4, H5, Hell, HellBot,
                                          validate_session)
from TelethonHell.DB import gvar_sql
from TelethonHell.helpers.anime import *
from TelethonHell.helpers.classes import *
from TelethonHell.helpers.convert import *
from TelethonHell.helpers.exceptions import *
from TelethonHell.helpers.formats import *
from TelethonHell.helpers.gdriver import *
from TelethonHell.helpers.google import *
from TelethonHell.helpers.ig_helper import *
from TelethonHell.utils.startup import *
from TelethonHell.version import __hellver__, __telever__


hell_logo = "./HellConfig/resources/pics/hellbot_logo.jpg"



hell_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hellbot_version = __hellver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "Its_HellBot"
my_group = Config.MY_GROUP or "HellBot_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/its_hellbot"
grp_link = "https://t.me/HellBot_Chat"
hell_channel = f"[†hê Hêllẞø†]({chnl_link})"
hell_grp = f"[Hêllẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""
