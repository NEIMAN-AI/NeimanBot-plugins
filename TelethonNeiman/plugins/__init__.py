from NeimanConfig import Config, db_config, os_config
from TelethonNeiman.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from TelethonNeiman.clients.decs import neiman_cmd, neiman_handler
from TelethonNeiman.clients.instaAPI import InstaGram
from TelethonNeiman.clients.logger import LOGGER
from TelethonNeiman.clients.session import (H2, H3, H4, H5, Neiman, NeimanBot,
                                          validate_session)

from TelethonNeiman.utils.startup import *
from TelethonNeiman.version import __hellver__, __telever__


neiman_logo = "./NeimanConfig/resources/pics/neimanbot_logo.jpg"



neiman_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
neimanbot_version = __hellver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "TeamNeiman"
my_group = Config.MY_GROUP or "Neiman_X_Support"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/TeamNeiman"
grp_link = "https://t.me/Neiman_X_Support"
neiman_channel = f"[иєιмαивσт]({chnl_link})"
neiman_grp = f"[тєαм иєιмαи]({grp_link})"

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
