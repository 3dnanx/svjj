from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 23035518
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "038341bd1a28b4cd0c6ca8802d94fb4d"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUJH9C3Qa9Milwur6FDFqa5g-O2QB8vX2rwMkYvqQQr3D3vmgYUvxMIHYP79HPuTTkDZ_d5EDLKUGSPh9VuDdAQklrfsXhnHJGs2uqM6s9KrnM0MCOhrGj3aRCW3rfLKD4qv01bTblPGvz7yLt_SSgL1Hl5ucMcnsTnSr14IyOjS-fT3tM4fgLMsMXCMMTSqUvZUAk8SjEQbhwk4uOgS0VORkKaNvifClUmd_OPKgb-iFRmcRCYWZ3OUebEXNx34v97wkmG3p_sYoKQfhZP9gJRJ7MSK8VRARa-rk0YWrZFyrdn2CEurnNLhRx3_tHJs9prf5pJfFE8pqqWGPZy4j5Ak="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
