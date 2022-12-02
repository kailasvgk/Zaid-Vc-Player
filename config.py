## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "1AZWarzUBu5KkSBO6U3RNHDhP3NGozIgwy5jIfr5tBuw1sv95E7kiRlJtB_NbemdecSqICcrv9ak5gALbt6CjtQJH-wTihvAqVokPpQVgl8JXsLIp0l9ESR_8RafFrknHYr0DCd9QDm-QooQG9bSDmizwCbEF2VpTyvusHketHW_EOAMEjs75J9ZwLmV3-fWW7o3IFYB8-YsEEojg1cDprQY6AXTDCkvgUKI29ls8pQkK6HwJg_etR9TiniUrtKVjs73XlIqh9uuZM_61G6zSaUR21fpr2RIgHHgozeAC-57HC3vQYu6MXi2Fy_DLOBojEyFeHok0aHgDMuZ7DvHkCfHopJjlz3Y=":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "1AZWarzUBu5KkSBO6U3RNHDhP3NGozIgwy5jIfr5tBuw1sv95E7kiRlJtB_NbemdecSqICcrv9ak5gALbt6CjtQJH-wTihvAqVokPpQVgl8JXsLIp0l9ESR_8RafFrknHYr0DCd9QDm-QooQG9bSDmizwCbEF2VpTyvusHketHW_EOAMEjs75J9ZwLmV3-fWW7o3IFYB8-YsEEojg1cDprQY6AXTDCkvgUKI29ls8pQkK6HwJg_etR9TiniUrtKVjs73XlIqh9uuZM_61G6zSaUR21fpr2RIgHHgozeAC-57HC3vQYu6MXi2Fy_DLOBojEyFeHok0aHgDMuZ7DvHkCfHopJjlz3Y=":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "1AZWarzUBu5KkSBO6U3RNHDhP3NGozIgwy5jIfr5tBuw1sv95E7kiRlJtB_NbemdecSqICcrv9ak5gALbt6CjtQJH-wTihvAqVokPpQVgl8JXsLIp0l9ESR_8RafFrknHYr0DCd9QDm-QooQG9bSDmizwCbEF2VpTyvusHketHW_EOAMEjs75J9ZwLmV3-fWW7o3IFYB8-YsEEojg1cDprQY6AXTDCkvgUKI29ls8pQkK6HwJg_etR9TiniUrtKVjs73XlIqh9uuZM_61G6zSaUR21fpr2RIgHHgozeAC-57HC3vQYu6MXi2Fy_DLOBojEyFeHok0aHgDMuZ7DvHkCfHopJjlz3Y=":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "1AZWarzUBu5KkSBO6U3RNHDhP3NGozIgwy5jIfr5tBuw1sv95E7kiRlJtB_NbemdecSqICcrv9ak5gALbt6CjtQJH-wTihvAqVokPpQVgl8JXsLIp0l9ESR_8RafFrknHYr0DCd9QDm-QooQG9bSDmizwCbEF2VpTyvusHketHW_EOAMEjs75J9ZwLmV3-fWW7o3IFYB8-YsEEojg1cDprQY6AXTDCkvgUKI29ls8pQkK6HwJg_etR9TiniUrtKVjs73XlIqh9uuZM_61G6zSaUR21fpr2RIgHHgozeAC-57HC3vQYu6MXi2Fy_DLOBojEyFeHok0aHgDMuZ7DvHkCfHopJjlz3Y=":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5477168104:AAHg-FLWEbvGWI09T92De37u_RaDQL3Cxx4")
BOT_NAME = getenv("BOT_NAME", "DarshanaXMusic")

API_ID = int(getenv("API_ID", "22029156"))
API_HASH = getenv("API_HASH", "7c7d75736193b71d40b00dc0b0981725")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://kailasvg:kailasvg@cluster04.gvju7bn.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Kailas")
OWNER_USERNAME = getenv("OWNER_USERNAME", "kailas_vg")
ALIVE_NAME = getenv("ALIVE_NAME", "Kailas")
BOT_USERNAME = getenv("BOT_USERNAME", "Darshana_music_bot")
OWNER_ID = getenv("OWNER_ID", "5530347700")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Darshana_Singer")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Darshana_music_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "About_kailas")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5530347700 5775058591").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
