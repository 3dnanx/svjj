import telethon
from telethon.events import CallbackQuery
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from checktele import *
from state_user import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests

IEX.start()


c = requests.session()
bot_username = '@EEObot'
bot_usernamee = '@A_MAN9300BOT'

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    6121853757,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]

async def join_channel():
    try:
        await IEX(JoinChannelRequest("@r6r6rr"))
        await IEX.send_message("@PP6ZZ", f'''تم بدأالسورس بنجاح
                                  ايها المطور @anxxx''')
    except BaseException:
        pass

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    start = datetime.datetime.now()
    chat_id = event.sender_id
    if event.is_group:  
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
    elif event.is_channel:
        mention = f"المنصب : **المطور [SVJ](tg://user?id={1421814874})**"
    else:
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
        
    await event.edit(f"""ـ               [ SVJ Hunter Source ]
     ـ●━━━━━━━━━━━━━━●
✥┊⌔ **مـرحبـاً عـزيـزي** {mention} 
✥┊⌔  إضغـط على الامـر لـنسخه ©️
     ـ●━━━━━━━━━━━━━━●
✥┊ `.م1`   ➪** إعـــدادات الـــســورس ** ⚙️
✥┊ `.م2`   ➪** أوامــر فحص الحساب** 📟
✥┊ `.م3`   ➪** أوامــر صيـــد اليوزرات** ⛳️
✥┊ `.م4`   ➪** أوامــر تثبيت اليوزرات** 🎯
✥┊ `.م5`   ➪** أوامــر تـجـمـيـع النقاط** 🎰
✥┊ `.م6`   ➪** أوامــر اضافية** 🧩
     ـ●━━━━━━━━━━━━━━●
ـ""", link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    chat_id = event.sender_id
    if event.is_group:  
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
    elif event.is_channel:
        mention = f"المنصب : **المطور (tg://user?id={1421814874})**"
    else:
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
        
    await event.edit(f"""ـ                [ SVJ Hunter Setting SVJ ]
     ـ●━━━━━━━━━━━━━━━━●
✥┊⌔ **مـرحبـاً عـزيـزي** {mention}
✥┊⌔  إضغـط على الامـر لـنسخه ©️
     ـ●━━━━━━━━━━━━━━━━●
✥┊`.فحص`                    ➪ فحص الـــســورس 🔎
✥┊`.سورس`                  ➪ فحص الـــســورس 🔎
✥┊`.اعادة تشغيل`➪ تحديث الـسـورس ♻️
     ـ●━━━━━━━━━━━━━━━━●
ـ""", link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2, link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3, link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4, link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    chat_id = event.sender_id
    if event.is_group:  
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
    elif event.is_channel:
        mention = f"المنصب : **المطور (t.me/@PP6ZZ)"
    else:
        data = await event.get_sender()
        fname = data.first_name   
        uid = data.id 
        mention = f"[{fname}](tg://user?id={uid})"
        
    await event.edit(f"""ـ                      [  Hunter Collector ⎉](t.me/r6r6rr)
     ـ●━━━━━━━━━━━━━━━━━━━━●
✥┊⌔ **مـرحبـاً عـزيـزي** {mention}
✥┊⌔  إضغـط على الامـر لـنسخه ©️
     ـ●━━━━━━━━━━━━━━━━━━━━●
✥┊`.تجميع المليار` :  **تـجميع نقاطـ بوت المليار**   💰
✥┊`.تجميع الجوكر`    :  **تجميع نقاط بوت الجوكر**   💰
     ـ●━━━━━━━━━━━━━━━━━━━━●
ـ""", link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.م6"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec6, link_preview=None)

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ WELCOME TO SVJ **
☆ **VERSION : 6.0**
☆ **PING : `{ms}`**
☆ **DATE : `{m9zpi}`**
☆ **ID : `{event.sender_id}`**
☆ **SOURCE SVJ : @r6r6rr **


-قـم بأرسال `.الاوامر`
''', link_preview=None)

ownerhson_id = 6121853757
@IEX.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply('مرحبا ايها المطور')

@IEX.on(events.NewMessage(outgoing=False, pattern=".المطور"))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply('مرحبا ايها المطور')
@IEX.on(events.NewMessage(outgoing=False, pattern=".بدء"))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply('''مرحبا ايها المطور @anxxx 
                          تم بدء السورس بنجاح للمنصب''')

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتظر 1-2 دقيقة  .")
    await IEX.disconnect()
    await IEX.send_message('me', "`اكتملت اعادة تشغيل السورس !`")

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await IEX.get_entity(bot_username)
        await IEX.send_message('@EEObot', 'جاري التجميع بواسطة | DNG TEAM')
        channel_entity = await IEX.get_entity(bot_username)
        await IEX.send_message('@EEObot', '/start')
        await asyncio.sleep(5)
        msg0 = await IEX.get_messages('@EEObot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await IEX.get_messages('@EEObot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await IEX(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await IEX.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await IEX(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await IEX(ImportChatInviteRequest(bott))
                msg2 = await IEX.get_messages('@EEObot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await IEX.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await IEX.send_message(event.chat_id, "تم الانتهاء من التجميع !")


##########################################################################################

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await IEX.get_entity(bot_usernamee)
        await IEX.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | DNG TEAM')
        channel_entity = await IEX.get_entity(bot_usernamee)
        await IEX.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await IEX.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await IEX.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await IEX(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await IEX.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await IEX(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await IEX(ImportChatInviteRequest(bott))
                msg2 = await IEX.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await IEX.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await IEX.send_message(event.chat_id, "تم الانتهاء من التجميع !")

LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await IEX(JoinChannelRequest("@r6r6rr"))
        await IEX.send_message("@PP6ZZ", f'''تم بدأالسورس بنجاح
                                  ايها المطور @PP6ZZ''')
       
    except BaseException:
        pass
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    6121853757,
]

def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"

@IEX.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')

@IEX.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    IEX = event.pattern_match.group(1)
    if IEX:
        msg = IEX
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@IEX.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    IEX = event.pattern_match.group(1)
    if IEX:
        msg = IEX
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@IEX.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)

async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass

@IEX.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)

@IEX.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
      await event.edit("""السـورس يعمـل | SVJ
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

- المطور :  عدنان |

- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها

قناة السورس : @r6r6rr
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍"""
)

@IEX.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.edit("""SY OWNER : @PP6ZZ"""
)

@IEX.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@IEX.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@IEX.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🔟")
    animation_chars = [
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",

    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
        
@IEX.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@IEX.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


print(" SVJ Hunter is Running ..")
LOGS.info(" SVJ Hunter is Running ")

IEX.run_until_disconnected()
