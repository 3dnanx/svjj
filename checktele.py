import random
import string
import asyncio
import logging
from asyncio import sleep
from user_agent import *
from help import *
from config import *
from Formater import *
import telethon
from telethon import events, Button
import requests
from telethon.sync import functions
from telethon.tl import types
from telethon.tl.types import InputChatUploadedPhoto
from telethon.errors import FloodError, FloodWaitError
from user_agent import generate_user_agent
import requests
import re
from queue import Queue
import threading
from threading import Thread
try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
except ModuleNotFoundError:
    os.system("pip3 install nltk")
    import nltk
    from nltk.corpus import words
    nltk.download('words')

LOGS = logging.getLogger(__name__)




english_words = set(words.words())

a = 'qwertyuiopassdfghjklzxcvbnm'
bbb = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
aa = 'ertuiowaszxcvnm'
ee = 'mnvcxzaswertuio'
bb = 'wertuioaszxcvnm'
eee = '8'
aaa = 'x'








import random

def generate_similar_pattern(input_pattern):
    # تعريف المتغيرات للرموز الثابتة
    global fixed_char, fixed_digit
    if 'fixed_char' not in globals():
        fixed_char = None
    if 'fixed_digit' not in globals():
        fixed_digit = None
    
    result = []
    i = 0
    
    while i < len(input_pattern):
        char = input_pattern[i]
        
        if char == '*':
            # حرف أو رقم عشوائي (a-z, 0-9)
            if random.choice([True, False]):
                result.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
            else:
                result.append(random.choice('0123456789'))
            i += 1
            
        elif char == '#':
            # حرف إنجليزي فقط (a-z)
            result.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
            i += 1
            
        elif char == '%':
            # 3 أرقام متسلسلة (فقط 123, 456, 789)
            allowed_patterns = ['123', '456', '789']
            result.append(random.choice(allowed_patterns))
            i += 1
            
        elif char == '$':
            # حرف عشوائي ثابت (يثبت مرة واحدة لكل عملية صيد)
            if fixed_char is None:
                fixed_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            result.append(fixed_char)
            i += 1
            
        elif char == '&':
            # رقم عشوائي ثابت (يثبت مرة واحدة لكل عملية صيد)
            if fixed_digit is None:
                fixed_digit = random.choice('0123456789')
            result.append(fixed_digit)
            i += 1
            
        elif char == '+':
            # رقم عشوائي غير ثابت (يتغير في كل مرة)
            result.append(random.choice('0123456789'))
            i += 1
            
        elif char in ['_', '-']:
            # الشرطة السفلية والشرطة العادية تبقى كما هي
            result.append(char)
            i += 1
            
        else:
            # أي حرف آخر يبقى ثابتاً
            result.append(char)
            i += 1
    
    # إعادة تعيين الرموز الثابتة بعد الانتهاء
    fixed_char = None
    fixed_digit = None
    
    return ''.join(result)
#############################################################################
# أضف هنا الدالة الجديدة:
def check_choice_valid(choice):
    """
    دالة للتحقق من صحة choice وتحمي من الأخطاء
    """
    # تحقق إذا كانت القيمة تحتوي على نقطة أو فاصلة
    if '.' in str(choice):
        choice = str(choice).split('.')[0]  # خذ الجزء الصحيح فقط
    if ',' in str(choice):
        choice = str(choice).split(',')[0]  # خذ الجزء الصحيح فقط
    
    # تحقق إذا كانت رقمية
    if not str(choice).isdigit():
        return False, "غير رقم"
    
    choice_num = int(choice)
    if choice_num < 1 or choice_num > 55:
        return False, "خارج النطاق"
    
    return True, choice_num
banned = []
isclaim = ["off"]
isfiltering = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()

# def check_user(username):
#     url = "https://t.me/"+str(username)
#     headers = {
#         "User-Agent": generate_user_agent(),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

#     response = requests.get(url, headers=headers)
#     if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
#         return "Available"
#     else:
#         return "Unavailable"
def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return "Available"
        else:
            return "Unavailable"
    except Exception:
        return "error"


def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], c[0] ,d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+'_'+d+c+d
        f2 = c+d+c+'_'+d
        f3 = c+d+'_'+d+c
        f4 = c+'_'+d+d+c
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+'_'+d+c+d
            f2 = c+c+d+'_'+d
            f3 = c+d+'_'+c+d
            f4 = c+'_'+d+d+c
            f = f1,f2,f3,f4
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "5":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], s[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], s[0], s[0], d[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "7":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "8":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], '_' , d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], '_' , d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
    else:
            pass
    if choice == "10":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], c[0] , '_' , d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0] , '_' , d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "11":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0], c[0] , c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(a)
            f = [c[0], c[0], d[0], c[0], d[0] ,d[0]]
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], c[0] , c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
             pass
    if choice == "12":
        c = d = random.choices(a)
        d = random.choices(a)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "13":
        c = d = random.choices(a)
        d = random.choices(a)
        f =  [c[0], d[0],  '_' , c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f =  [c[0], d[0],  '_' , c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "14":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], c[0], c[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], c[0], c[0], d[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "15":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [c[0], c[0], d[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [c[0], c[0], d[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "16":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "17":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(aaa)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(aaa)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "18":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(aaa)
        f = [s[0], s[0], s[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(aaa)
            f = [s[0], s[0], s[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "19":
        c = random.choices(aa)
        d = random.choices(aaa)
        s = random.choices(ee)
        f = [s[0], c[0], c[0], c[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(aaa)
            s = random.choices(ee)
            f = [s[0], c[0], c[0], c[0], d[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "20":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [s[0], d[0], d[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [s[0], d[0], d[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "21":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "22":
        c = random.choices(aa)
        d = random.choices(ee)
        s = random.choices(bb)
        f = [s[0], s[0], s[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(ee)
            s = random.choices(bb)
            f = [s[0], s[0], s[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "23":
        c = random.choices(aa)
        d = random.choices(bb)
        s = random.choices(ee)
        f = [s[0], d[0], d[0], d[0], c[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(aa)
            d = random.choices(bb)
            s = random.choices(ee)
            f = [s[0], d[0], d[0], d[0], c[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "24":
        c = random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "25":
        c = random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "26":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "27":
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        d3 = str(''.join((random.choice(b) for i in range(1))))
        f1 = 'vip'+d1+d2+d1+d2
        f2= 'vip'+d1+d1+d2+d2
        f3 = 'vip'+d1+d2+d2+d2
        f4 = 'vip'+d1+d1+d1+d2
        f5 = 'id'+d1+d2+d3
        f = f1,f2,f3,f4,f5
        f = random.choice(f)
        username =f
        if username in banned[0]:
            d1 = str(''.join((random.choice(b) for i in range(1))))
            d2 = str(''.join((random.choice(b) for i in range(1))))
            f1 = 'vip'+d1+d2+d1+d2
            f2= 'vip'+d1+d1+d2+d2
            f3 = 'vip'+d1+d1+d1+d2
            f4 = 'vip'+d1+d1+d1+d1
            f5 = 'id'+d1+d2+d3
            f6 = 'USER'+d1+d2+d3
            f = f1,f2,f3,f4,f5,f6
            f = random.choice(f)
            username =f
        else:
            pass
    if choice == "28":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        k = random.choices(b)
        f = [c[0], d[0], s[0],k[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            k = random.choices(b)
            f = [c[0], c[0], c[0],k[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    if choice == "29":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0] , d[0], c[0] ,d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0] , d[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "30":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], d[0] , c[0], c[0] ,c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], d[0] , c[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "31":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0] , c[0], d[0] ,d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], d[0], c[0] , c[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "32":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0] , c[0], c[0] ,c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], d[0], c[0] , c[0], c[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "33":
        c = random.choices(a)
        d = random.choices(bbb)
        s = random.choices(b)
        f = [c[0], c[0], s[0], s[0] , s[0], s[0] ,s[0]]
        random.shuffle(f)
        username = ''.join(f)
    else:
            pass
    if choice == "34":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0] , d[0], c[0] ,c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], c[0], d[0] , c[0], d[0] ,d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "35":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+c+d+c+c+d+c
        f2 = c+d+d+c+c+c+c
        f3 = c+d+c+d+c+c+c
        f4 = c+c+c+d+c+c+d
        f5 = c+c+d+c+d+c+c
        f6 = c+c+c+d+c+d+c
        f7 = c+d+d+c+c+c+c
        f8 = c+c+d+d+c+c+c 
        f9 = c+c+c+d+d+c+c
        f10 = c+c+c+c+d+d+c
        f11 = c+c+c+c+c+d+d
        f12 = c+c+c+c+d+c+d
        f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+c+d+c+c+d+c
            f2 = c+d+d+c+c+c+c
            f3 = c+d+c+d+c+c+c
            f4 = c+d+c+c+d+c+c
            f5 = c+d+c+c+c+c+d
            f6 = c+c+c+d+c+d+c
            f7 = c+d+d+c+c+c+c
            f8 = c+c+d+d+c+c+c 
            f9 = c+c+c+d+d+c+c
            f10 = c+c+c+c+d+d+c
            f11 = c+c+c+c+c+d+d
            f12 = c+c+c+c+d+c+d
            f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f10,f11,f12
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "36":
        c = random.choices(a)
        d = random.choices(bbb)
        s = random.choices(eee)
        f = [c[0], c[0], s[0], s[0] , s[0], s[0] ,s[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(bbb)
            s = random.choices(eee)
            f = [c[0], c[0], s[0], s[0] , s[0], s[0] ,s[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "37":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+d+c+c+c
        f2 = c+c+d+d+c+c
        f3 = c+c+c+d+d+c
        f4 = c+c+c+c+d+d
        f5 = c+d+c+d+c+c
        f6 = c+c+d+c+d+c
        f7 = c+c+c+d+c+d
        f8 = c+c+c+c+d+d
        f9 = c+d+d+d+d+c
        f10 = c+d+d+d+c+d
        f11 = c+c+d+d+d+d
        f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(b) for i in range(1))))
            f1 = c+d+d+c+c+c
            f2 = c+c+d+d+c+c
            f3 = c+c+c+d+d+c
            f4 = c+c+c+c+d+d
            f5 = c+d+c+d+c+c
            f6 = c+c+d+c+d+c
            f7 = c+c+c+d+c+d
            f8 = c+c+c+c+d+d
            f9 = c+d+d+d+d+c
            f10 = c+d+d+d+c+d
            f11 = c+c+d+d+d+d
            f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11 
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "38":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+c+c+c+c+c
        f2 = c+c+d+c+c+c+c
        f3 = c+c+c+d+c+c+c
        f4 = c+c+c+c+d+c+c
        f5 = c+c+c+c+c+d+c
        f6 = c+c+c+c+c+c+d
        f = f1,f2,f3,f4,f5,f6
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+d+c+c+c+c+c
            f2 = c+c+d+c+c+c+c
            f3 = c+c+c+d+c+c+c
            f4 = c+c+c+c+d+c+c
            f5 = c+c+c+c+c+d+c
            f6 = c+c+c+c+c+c+d 
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "39":
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        d3 = str(''.join((random.choice(b) for i in range(1))))
        f1 = 'trx'+d1+d2
        f2= 'top'+d1+d2
        f3 = 'ton'+d1+d2
        f4 = 'tg'+d1+d2+d3
        f = f1,f2,f3,f4
        f = random.choice(f)
        username =f
        if username in banned[0]:
            d1 = str(''.join((random.choice(b) for i in range(1))))
            d2 = str(''.join((random.choice(b) for i in range(1))))
            f1 = 'trx'+d1+d2
            f2= 'top'+d1+d2+d2
            f3 = 'ton'+d1+d2+d2
            f4 = 'tg'+d1+d2+d3
            f = f1,f2,f3,f4
            f = random.choice(f)
            username =f
        else:
            pass
    if choice == "40":
        c = str(''.join((random.choice(a) for i in range(1))))
        s = str(''.join((random.choice(bbb) for i in range(1))))
        n = str(''.join((random.choice(eee) for i in range(1))))
        k = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+s+n+n+n+n+n
        f2 = c+k+n+n+n+n+n
        f = f1,f2
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "41":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], '_' , d[0], d[0] , d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], '_' , d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
        if choice == "42":
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(bbb) for i in range(1))))
            f1 = c+d+c+c+c+c+c+c
            f2 = c+c+d+c+c+c+c+c
            f3 = c+c+c+d+c+c+c+c
            f4 = c+c+c+c+d+c+c+c
            f5 = c+c+c+c+c+d+c+c
            f6 = c+c+c+c+c+c+d+c
            f7 = c+c+c+c+c+c+c+d
            f = f1,f2,f3,f4,f5,f6,f7
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "43":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(bbb) for i in range(1))))
        f1 = c+s+s+s+s+s+d
        f2 = c+s+s+s+s+s+n
        f = f1,f2
        f = random.choice(f)
        username = f
    else: 
        pass
    if choice == "44":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(bbb)
            f = [c[0], d[0], d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a)
                d = random.choices(b)
            f = [c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a) 
                d = random.choices(b)
            f = [c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
            if username in banned[0]:
                c = random.choices(a) 
                d = random.choices(e)
            f = [c[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "45":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+d+d+c+c
        f2 = c+c+d+d+c
        f3 = c+c+c+d+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "46":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+'_'+d+d+d
        f2 = c+c+c+'_'+d
        f = f1,f2
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "47":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+c+d+d+d+d+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "48":
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        d3 = str(''.join((random.choice(b) for i in range(1))))
        f1 = 'tg'+d1+d2+d3
        f2 = 'tg'+d1+d2+d2
        f3 = 'tg' +d1+d1+d2
        f = f1,f2,f3
        f = random.choice(f)
        username =f
    else:
        pass
    if choice == "49":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        bbb = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+d+d+d+c+c+c
        f2 = c+d+d+d+d+c+c
        f3 = c+c+d+d+d+c+c
        f4 = c+c+c+d+d+d+c
        f5 = c+c+c+d+d+d+d
        f6 = c+c+c+c+d+d+d
        f7 = c+c+c+d+d+d+c
        f = f1,f2,f3,f4,f5,f6,f7
        f = random.choice(f)
        username =f
    else:
        pass
    if choice == "50":
        c = str(''.join((random.choice(aaa) for i in range(1))))
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+d1+d2+d1+d1
        f2 = c+d1+d1+d2+d1
        f = f1,f2
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "51":
        c = str(''.join((random.choice(a) for i in range(1))))
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+d1+d2+d1+d1
        f2 = c+d1+d1+d2+d1
        f = f1,f2
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "52":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        s = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+d+s+s
        f2 = c+s+s+d+d
        f3 = c+c+d+d+s
        f4 = c+c+s+s+d
        f5 = c+c+d+s+s
        f6 = c+c+s+d+d
        f = f1,f2,f3,f4,f5,f6
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "53":
        d1 = str(''.join((random.choice(b) for i in range(1))))
        d2 = str(''.join((random.choice(b) for i in range(1))))
        d3 = str(''.join((random.choice(b) for i in range(1))))
        f1 = 'vip'+d1+d1+d1+d2+d2+d2
        f2 = 'vip'+d2+d2+d2+d1+d1+d1
        f3 = 'vip' +d1+d2+d2+d2+d2
        f4 = 'vip' +d1+d1+d1+d1+d2
        f = f1,f2,f3, f4
        f = random.choice(f)
        username =f
    else:
        pass
    if choice == "54":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        s = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+'_'+d+c+d
        f2 = c+d+c+'_'+d
        f3 = c+d+'_'+d+c
        f4 = c+'_'+d+d+c
        f5 = c+d+'_'+c+d
        f6 = 'bot'+c+d+s
        f7 = 'vip'+d1+d1+d1+d2+d2+d2
        f8 = 'vip'+d2+d2+d2+d1+d1+d1
        f9 = 'vip' +d1+d2+d2+d2+d2
        f10 = 'vip' +d1+d1+d1+d1+d2
        f = f1,f2,f3,f4,f5,f7,f8,f9,f10
        f = random.choice(f)
        username = f
    else:
        pass
    if choice == "55":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        s = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+s+s+s
        f2 = c+d+d+d+s
        f3 = c+c+c+d+s
        f = f1,f2,f3
        f = random.choice(f)
        username = f
    else:
        pass
    return username 
      
        
    
#############################################################################
#الصيد العادى 
# صيد عدد نوع قناة  
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        choice = str(msg[1])
        replly = await event.get_reply_message()

        try:
            ch = str(msg[2])
        except Exception as ee:
            ch = None

        is_valid, result = check_choice_valid(choice)
        if not is_valid:
            await event.edit(f"هذا النوع غير موجود: {result}")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            return await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        else:
            await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")
            await asyncio.sleep(1)

        if ch == None:
            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title=" SVJ Hunting Channal ",
                    about=f"This channel to hunt usernames by - @PP6ZZ,  {IEX_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass
                    
                    invite = await IEX(functions.messages.ExportChatInviteRequest(
                        peer=ch
                    ))

                    invite_link = invite.link

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** [اضغط هنا]({invite_link}) \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
            
    for i in range(int(msg[0])):
        if ispay[0] == 'no':
            break
        username = ""

        username = gen_user(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(1)
            try:
                await IEX(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                
                break
            
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys = int(trys)
        trys += 3
        
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    await event.client.send_message(event.chat_id, "! انتهى الصيد " )
#############################################################################
#صيد متعدد
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد_متعدد (.*)"))
async def multi_hunt(event):
    if ispay[0] == "yes":
        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        
        # معالجة الأمر: .صيد متعدد نوع1.نوع2.نوع3...
        types_str = event.pattern_match.group(1)
        
        # تحليل الأنواع المطلوبة باستخدام النقطة (.)
        multi_hunt_types = []
        for t in types_str.split("."):
            t = t.strip()
            is_valid, result = check_choice_valid(t)
            if is_valid:
                multi_hunt_types.append(str(result))
        
        if not multi_hunt_types:
            await event.edit("**لم يتم تحديد أنواع صحيحة (1-55)**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # إنشاء قناة واحدة للصيد
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""
        
        try:
            ch = await IEX(functions.channels.CreateChannelRequest(
                title=f"SVJ Hunting Channal",
                about=f"This channel to hunt usernames by - @PP6ZZ, {IEX_USER}",
            ))
            ch = ch.updates[1].channel_id
            
            photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
            try:
                await IEX(functions.channels.EditPhotoRequest(channel=ch, photo=photo))
            except Exception:
                pass
                
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في إنشاء القناة: {str(e)}")
            isclaim.clear()
            isclaim.append("off")
            return
            
        await event.edit(f"**✥┊ تم بدء الصيد المتعدد .. بنجاح ☑️**\n**✥┊ الأنواع: {' . '.join(multi_hunt_types)}**\n**✥┊ سيصيد يوزر واحد من بين هذه الأنواع**\n**✥┊ لمعرفة تقدم عملية الصيد (** `.حالة الصيد` **)**\n**✥┊ لإيقاف عملية الصيد (** `.ايقاف الصيد` **)**")
        
        # بدء الصيد - يختار نوع عشوائي من الأنواع المحددة في كل محاولة
        Checking = True
        while Checking:
            if ispay[0] == 'no' or "off" in isclaim:
                break
                
            # اختيار نوع عشوائي من الأنواع المحددة
            random_type = random.choice(multi_hunt_types)
            username = gen_user(random_type)
            
            t = Thread(target=lambda q, arg1: q.put(check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            
            if "error" in isav:
                await IEX.send_message(event.chat_id, f""" **حدث خطأ فى الفحص** \n قم بارسالها الى مطور السورس @PP6ZZ""")

            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await IEX(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))

                    await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                    await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')

                    break  
                
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    if "too many public channels" in str(eee):
                        await IEX.send_message(event.chat_id, f"""- خطأ بصيد اليوزر @{username}، لديك الكثير من القنوات""")
                        break
                    elif "USERNAME_OCCUPIED" in str(eee):
                        # اليوزر محجوز، استمر في المحاولة
                        pass
            else:
                pass
            trys += 1
            
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        await event.client.send_message(event.chat_id, "! انتهى الصيد المتعدد")

#############################################################################

    # الصيد التلقائى بالرد على قناة او انشائها تلقائيا صياد + نوع تلقائى + عدد اليوزرات المطلوب 

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صياد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        choice = str(msg[0])
        tr = int(msg[1]) if len(msg) > 1 and msg[1].isdigit() else 1
        
        if choice not in (""):
            is_valid, result = check_choice_valid(choice)  
            if not is_valid:                                                                                               
                await event.edit(f"هذا النوع غير موجود: {result}")
                isclaim.clear()
                isclaim.append("off")
                trys = 0
                await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        replly = await event.get_reply_message()

        if tr > 1:

            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶 ▬▭▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟸𝟶 ▬▬▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟹𝟶 ▬▬▬▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟺𝟶 ▬▬▬▬▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟻𝟶 ▬▬▬▬▬▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟼𝟶 ▬▬▬▬▬▬▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟽𝟶 ▬▬▬▬▬▬▬▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟾𝟶 ▬▬▬▬▬▬▬▬▭▭", link_preview=None) 
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟿𝟶 ▬▬▬▬▬▬▬▬▬▭", link_preview=None) 
            await asyncio.sleep(1)
            dl =  await event.edit(f"ᯓ **[SVJ Multi HUNTER](t.me/r6r6rr)**\n**•─────────────────•**\n\n**⇜ انتهي تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶𝟶 ▬▬▬▬▬▬▬▬▬▬💯", link_preview=None)
            await sleep(1)
            await dl.delete()

            for current_cycle in range(tr):
                    try:

                        ch = await IEX(functions.channels.CreateChannelRequest(
                        title="SVJ Hunting Channal ",
                        about=f"This channel to hunt usernames by - @PP6ZZ,  {IEX_USER}",
                        ))
            
                        ch = ch.updates[1].channel_id

                        photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                        try:
                            await IEX(functions.channels.EditPhotoRequest(
                                channel=ch,
                                photo=photo
                            ))
                        except Exception:
                            pass

                        await event.client.send_message(event.chat_id, f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊عدد اليوزرات المطلوبة** {tr} \n**✥┊المحاولة الحالية رقم :- ** {current_cycle + 1} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                    except Exception as e:

                        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                        Checking = False
        
        
                    Checking = True
                    while Checking:
                        if ispay[0] == 'no':
                            break
                        username = ""

                        username = gen_user(choice)
                        t = Thread(target=lambda q, arg1: q.put(
                            check_user(arg1)), args=(que, username))
                        t.start()
                        t.join()
                        isav = que.get()
                        
                        if "error" in isav:
                            await IEX.send_message(event.chat_id, f""" **حدث خطأ فى الفحص** \n قم بارسالها الى مطور السورس @PP6ZZ""")

                        if "Available" in isav:
                            await asyncio.sleep(1)
                            try:
                                await IEX(functions.channels.UpdateUsernameRequest(
                                    channel=ch, username=username))

                                await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                                await event.client.send_file(channel, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                                
                                await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')

                                break  
                            except Chack_UserName_Flood as e:
                                hours = e.seconds // 3600
                                minutes = (e.seconds % 3600) // 60
                                seconds = (e.seconds % 3600) % 60

                                message = f"""**تم كشف فلود عند فحص اليوزر** {username}
** خاصية روح ثبت عليه **  

ـ          **[ SVJ FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                                await IEX.send_message(event.chat_id, message)
                                await IEX.send_message("@PP6ZZ", message)
                                await IEX.send_message(channel , message)
                                await sleep(e.seconds + 5)
                                pass
                            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                                with open("banned.txt", "a") as f:
                                    f.write(f"\n{username}")
                            except Exception as eee:
                                if "too many public channels" in str(eee):
                                    await IEX.send_message(
                                        event.chat_id,
                                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                                    )
                                    break
                                else:
                                    pass
                        else:
                            pass
                        trys = int(trys)
                        trys += 3
            pass
        else:

            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ النـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title=" SVJ Hunting Channal ",
                    about=f"This channel to hunt usernames by - @PP6ZZ,  {IEX_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
        
        
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break
                username = ""

                username = gen_user(choice)
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))

                        await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                        await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')

                        break
                    
                        pass
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        with open("banned.txt", "a") as f:
                            f.write(f"\n{username}")
                    except Exception as eee:
                        if "too many public channels" in str(eee):
                            await IEX.send_message(
                                event.chat_id,
                                f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                            )
                            break
                        else:
                            pass
                else:
                    pass
                trys = int(trys)
                trys += 3
            pass
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    Checking = False
    if tr > 1:
        await event.client.send_message(event.chat_id, "! انتهى الصيد المتعدد بنجاح")
    else:
        await event.client.send_message(event.chat_id, " مبروك ") 
#############################################################################
# التحكم بالصيد
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف الصيد(.*)")) 
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        await event.edit("**- تم إيقـاف عمليـة الصيد .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية صـيد جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
            
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if ispay[0] == "yes":
        if "on" in isclaim:
            await event.edit(f"الصيد وصل لـ({trys}) من المحاولات")
        elif "off" in isclaim:
            await event.edit("لايوجد صيد شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
#############################################################################
    #تثبيت البوتات
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_بوتات (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""
        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])

        if username.startswith('@'): 
            username = username.replace("@", "")  
        else:
            username = username

        if not username.lower().endswith("bot"):
            await event.edit("**● عـذرًا عـزيـزي اليوزر خطـأ ❌**\n**● استخـدم الامـر كالتالـي**\n**● أرسـل (**`..تثبيت_بوتات`** + يوزر البوت نهايته(bot))**")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            Checking = False
        elif username.lower().endswith("bot"):
            await event.edit(f"**⎉╎تم بـدء التثبيت .. بنجـاح ☑️**\n**⎉╎اليـوزر المثبت ( {username} )**\n**⎉╎لمعرفـة تقـدم عمليـة التثبيت (**`.حالة التثبيت`**)**\n**⎉╎لـ ايقـاف عمليـة التثبيت (**`.ايقاف التثبيت`**)**")
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break

                t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX.send_message("@BotFather", "/newbot")
                        await asyncio.sleep(1)
                        async for message in IEX.iter_messages("@BotFather", limit=1):
                            if message.message.startswith("Sorry, you can't add more than"):
                                await IEX.send_message(event.chat_id, "لا يمكنك إضافة المزيد من البوتات.")
                                isclaim.clear()
                                isclaim.append("off")
                                trys = 0
                                Checking = False
                                break
                            elif message.message.startswith("Sorry"):
                                match = re.search(r"(\d+) seconds", message.message)
                                if match:
                                    s = int(match.group(1))
                                    hours = s // 3600
                                    minutes = (s % 3600) // 60
                                    seconds = (s % 3600) % 60
                                    message = (
                                        f"\"للاسف تبندت\n مدة الباند.\n"
                                        f"الساعات: {hours}\n"
                                        f"الدقائق: {minutes}\n"
                                        f"الثواني: {seconds}\""
                                    )
                                    await IEX.send_message(event.chat_id, message)
                                    await sleep(s)
                                    await sleep(10)
                            else:
                                await IEX.send_message("@BotFather", "● SVJ Bot Hunter ●")
                                await asyncio.sleep(2)
                                await IEX.send_message("@BotFather", f"@{username}")
                                await asyncio.sleep(3)
                                async for message in IEX.iter_messages("@BotFather", limit=1):
                                    if message.message.startswith("Done! Congratulations on your new bot."):
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"The user was Hunted by @PP6ZZ")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setuserpic")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_file("@BotFather", "IEX_HUNTER.jpg")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"SVJ Bot Hunted By - @PP6ZZ , ")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setdescription")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"SVJ Bot Hunted By - @PP6ZZ, \n owner :- {IEX_USER}")
                                        
                                        await event.client.send_file(event.chat_id,"https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( @BotFather )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                                        await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( @BotFather )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                                        Checking = False
                                        break
                                    elif message.message.startswith("Sorry, this username is invalid."):
                                        await event.client.send_message(event.chat_id, f"**المعرف @{username} غير صالح !!❌❌**")
                                        isclaim.clear()
                                        isclaim.append("off")
                                        trys = 0
                                        Checking = False
                                        break
                                    else:
                                        pass
                    except Exception as e:
                        print(e)
                else:
                    pass
            trys = int(trys)
            trys += 1
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        Checking = False
        await event.client.send_message(event.chat_id, f"\n- لـ التأكـد قـم بالذهـاب الـى @BotFather\nـ! انتهت عملية تثبيت البوت بنجاح ")
#############################################################################################
# التثبيت التلقائى بالرد على قناة او انشائها تلقائيا 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_قناة (.*)"))
async def _(event):
    global trys
    trys = 0
    isclaim.clear()
    isclaim.append("on")

    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    username = str(msg[0])

    replly = await event.get_reply_message()
    try:
        
        if replly and replly.text.startswith('@'): 
            
            ch = replly.text
            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ على القناة ( {ch} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
        else:
            user = await event.get_sender()
            uss = user.username   
            IEX_USER = f"@{uss}" if uss else ""
            
            ch = await IEX(functions.channels.CreateChannelRequest(
            title=" SVJ Hunting Channal ",
            about=f"This channel to hunt usernames by - @PP6ZZ,  | {IEX_USER}",
            ))
                
            ch = ch.updates[1].channel_id
                
            photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
            try:
                await IEX(functions.channels.EditPhotoRequest(
                    channel=ch,
                    photo=photo
                ))
            except Exception:
                pass

            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    except Exception as e:
        
        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        cmodels = False
        
    if username.startswith('@'): 
        username = username.replace("@", "")  
    else:
        username = username


    isclaim.clear()
    isclaim.append("on")
    cmodels = True
    while cmodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isch = que.get()
        if "Available" in isch:
            try:
                await IEX(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                
                break
            except Chack_UserName_Flood as e: 
                        hours = e.seconds // 3600
                        minutes = (e.seconds % 3600) // 60
                        seconds = (e.seconds % 3600) % 60
                        message = f"""**تم كشف فلود عند فحص اليوزر** {username}
** خاصية روح ثبت عليه ** 

ـ          **[ SVJ FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                        await IEX.send_message(event.chat_id, message)
                        await IEX.send_message("@PP6ZZ", message)
                        await sleep(e.seconds + 5)
 
            except FloodWaitError as zed:
                wait_time = zed.seconds
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = (wait_time % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too any public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 1

        await asyncio.sleep(2)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    
    return await IEX.send_message(event.chat_id, "**- تم الانتهاء من التثبيت على القناة .. بنجـاح ✅**")

#############################################################################################
# التثبيت على حساب المستخدم

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_حساب (.*)"))
async def _(event):
    global trys
    trys = 0

    zelzal = str(event.pattern_match.group(1))
    if not zelzal.startswith('@'):
        return await edit_or_reply(event, "**⎉╎عـذراً عـزيـزي المدخـل خطـأ ❌**\n**⎉╎استخـدم الامـر كالتالـي**\n**⎉╎ارسـل (**`.تثبيت_حساب`** + اليـوزر)**")
    await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {zelzal} )**\n**✥┊ نوع التثبيت :- حساب **\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
    
    isclaim.clear()
    isclaim.append("on")

    username = zelzal.replace("@", "")
    amodels = True
    while amodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isac = que.get()
        if "Available" in isac:
            try:
                await IEX(functions.account.UpdateUsernameRequest(username=username))
                await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Account )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Account )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                amodels = False
                break
            except Chack_UserName_Flood as zed:
                wait_time = zed.seconds
                
                hours = e.seconds // 3600
                minutes = (e.seconds % 3600) // 60
                seconds = (e.seconds % 3600) % 60
                                
                message = f"""**تم كشف فلود على اليوزر** {username}
**عليك الانتظار سيقوم السورس بالمحاولة للسحب بعد انتهاء المدة **
ـ          **[ SVJ FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                await IEX.send_message(event.chat_id, message)
                await IEX.send_message("@PP6ZZ", message)
                await sleep(wait_time + 5)
                
            except FloodWaitError as zed:
                wait_time = zed.seconds
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = (wait_time % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 1

        await asyncio.sleep(5)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    return await IEX.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")


LOGS.info(" SVJ Hunter is Running ")


Threads=[] 
if "on" in isclaim:
    for t in range(200):
        x = threading.Thread(target=_)
        le = threading.Thread(target=gen_user)
        x.start()
        le.start()
        Threads.append(x)
        Threads.append(le)
    for Th in Threads:
        Th.join()
else:
    Threads.clear()
    pass

#############################################################################################
    #التحكم بالتثبيت 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التثبيت"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys1 = 0
        await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
############################################################################################
        
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay[0] == "yes":
        await IEX.send_file(event.chat_id, 'banned.txt')


#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
ftrys = 0 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تصفية المبند"))
async def filter_banned_users(event):
    global ftrys
    if ispay[0] == "yes":
        isfiltering.clear()
        isfiltering.append("on")
        replly = await event.get_reply_message()
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
            else:
                user = await event.get_sender()
                uss = user.username   
                IEX_USER = f"@{uss}" if uss else ""
        
                ch = await IEX(functions.channels.CreateChannelRequest(
                title=" SVJ Hunting Channal ",
                about=f"This channel to Flood usernames by - @PP6ZZ ,  | {IEX_USER}",
                ))
            
                ch = ch.updates[1].channel_id
                
                photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                try:
                    await IEX(functions.channels.EditPhotoRequest(
                        channel=ch,
                        photo=photo
                    ))
                except Exception:
                    pass

                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

    try:
        if replly and replly.text.startswith('@'):
            channel_username = replly.text
        else:
            channel_username = ch

        with open("banned.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                username = line.strip()
                try:
                    await IEX(
                        functions.channels.UpdateUsernameRequest(
                            channel=channel_username,
                            username=username
                        )
                    )
                    await event.client.send_message(
                        event.chat_id,
                        f"- Done : @{username} ✅",
                    )
                    await event.client.send_message(
                        "@PP6ZZ", f"- Done : @{username} ✅",
                    )
                except telethon.errors.FloodWaitError as e:
                    hours = e.seconds // 3600
                    minutes = (e.seconds % 3600) // 60
                    seconds = (e.seconds % 3600) % 60
                    message = (
                        f"\"للاسف تبندت\n مدة الباند.\n"
                        f"الساعات: {hours}\n"
                        f"الدقائق: {minutes}\n"
                        f"الثواني: {seconds}\""
                    )
                    await IEX.send_message(event.chat_id, message)
                    await sleep(e.seconds)
                    await sleep(20)
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    pass
                except Exception as eee:
                    if "The username is already taken" in str(eee) or "USERNAME_PURCHASE_AVAILABLE" in str(eee) or "(caused by UpdateUsernameRequest)" in str(eee):
                        with open("banned.txt", "r+") as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if line.strip() != username:
                                    f.write(line)
                            f.truncate()
                    else:
                        await IEX.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        break
                ftrys += 1
        ftrys = 0
        isfiltering.clear()
        isfiltering.append("off")
        await IEX.send_file(event.chat_id, 'banned.txt')  # بعد الانتهاء
    except Exception as e:
        await IEX.send_message(event.chat_id, f"خطأ في التصفية , الخطأ**-  : {str(e)}**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التصفية"))
async def check_filter_status(event):
    if ispay[0] == "yes":
        if "on" in isfiltering:
            await event.edit(f"التصفية وصلت لـ({ftrys}) من المحاولات")
        elif "off" in isfiltering:
            await event.edit("لاتوجد تصفية شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
################################################################
    #الانواع التقليدية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.edit(Types["Types1"])
#             elif type_number == 2:
#                 await event.edit(Types["Types2"])
#             elif type_number == 3:
#                 await event.edit(Types["Types3"])
#         else:
#             await event.edit(Types["Types1"])

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.edit(Main_Types, link_preview=None)    

################################################################
    #الانواع التلقائية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.edit(Auto_Checker["Types1"])
#             elif type_number == 2:
#                 await event.edit(Auto_Checker["Types2"])
#             elif type_number == 3:
#                 await event.edit(Auto_Checker["Types3"])
#         else:
#             await event.edit(Auto_Checker["Types1"])
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.edit(Main_Auto_Checker, link_preview=None)
#===================================================================
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ج"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username
        uss1 = user.first_name   
        uss2 = user.last_name   
        uss3 = f"{uss1} {uss2}"
        
        uss4 = user.id   
        mention = f"[{uss1}](tg://user?id={uss4})"
        await IEX.send_message(event.chat_id, f"{str(user)}")
        await IEX.send_message(event.chat_id, f"{str(uss)}")
        await IEX.send_message(event.chat_id, f"{str(uss1)}")
        await IEX.send_message(event.chat_id, f"{str(uss2)}")
        await IEX.send_message(event.chat_id, f"{str(uss3)}")
        await IEX.send_message(event.chat_id, f"{str(uss4)}")
        await event.edit(f"""
[ SVJ Hunter Source ](t.me/r6r6rr)
ـ●━━━━━━━━━━━━━━●
✥┊⌔ مـرحبـاً عـزيـزي {mention}
✥┊⌔  إضغـط على الامـر لـنسخه
ـ    ●╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍●
✥┊ .م1   ➪ إعـــدادات الـــســورس 
✥┊ .م2   ➪ أوامــر صيـــد اليوزرات
✥┊ .م3   ➪ أوامــر تثبيت اليوزرات
✥┊ .م4   ➪ أوامــر تـجـمـيـع النقاط
✥┊ .م5   ➪ أوامــر اضافية
ـ●━━━━━━━━━━━━━━●
""", link_preview=None)
        await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
################################################################
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.لستة"))
async def check_list(event):
    if ispay[0] == "yes":
        # إعداد حالة الصيد
        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        
        # الانتظار حتى يرسل المستخدم الملف
        await event.edit("**📁┊أرسل لي الملف الآن (txt)**\n**⏳┊سأنتظر 60 ثانية...**")
        
        try:
            fut = event.client.loop.create_future()

            @event.client.on(events.NewMessage(from_users=event.sender_id))
            async def handler(new_event):
                if not fut.done():
                    fut.set_result(new_event)

            file_msg = await asyncio.wait_for(fut, timeout=60)

        except asyncio.TimeoutError:
            await event.edit("**❌│ما رسلت ملف خلال 60 ثانية**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # تحميل الملف إذا كان يحتوي على مستند
        if file_msg.document:
            file_path = await file_msg.download_media()
        else:
            await event.edit("**❌┊الرسالة المرسلة لا تحتوي على ملف**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # قراءة الملف
        try:
            with open(file_path, 'r') as f:
                usernames = f.readlines()
        except Exception as e:
            await event.edit(f"**❌┊خطأ في قراءة الملف: {str(e)}**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        if not usernames:
            await event.edit(f"**✥┊ الملف فارغ**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        await event.edit(f"**✥┊ جاري فحص {len(usernames)} يوزر...**\n**✥┊ سيستمر حتى يصيد يوزر**")
        
        # إنشاء قناة للصيد
        try:
            user = await event.get_sender()
            uss = user.username   
            IEX_USER = f"| @{uss}" if uss else ""
            
            ch = await IEX(functions.channels.CreateChannelRequest(
                title="SVJ Hunting Channal",
                about=f"This channel to hunt usernames by - @PP6ZZ, {IEX_USER}",
            ))
            ch = ch.updates[1].channel_id
            
            photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
            try:
                await IEX(functions.channels.EditPhotoRequest(channel=ch, photo=photo))
            except Exception:
                pass
                
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في إنشاء القناة: {str(e)}")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # بدء عملية الفحص
        caught = False
        trys = 0
        
        while not caught:
            if ispay[0] == 'no' or "off" in isclaim:
                break
                
            for username in usernames:
                if caught or ispay[0] == 'no' or "off" in isclaim:
                    break
                    
                username = username.strip()
                if not username:
                    continue
                    
                if username.startswith('@'):
                    username = username[1:]
                
                # فحص اليوزر
                t = Thread(target=lambda q, arg1: q.put(check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                
                if "error" in isav:
                    await IEX.send_message(event.chat_id, f"**حدث خطأ في فحص اليوزر: @{username}**")
                    continue
                
                if "Available" in isav:
                    await asyncio.sleep(0.8)
                    try:
                        # محاولة أخذ اليوزر
                        await IEX(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                        
                        # إرسال رسالة النجاح
                        await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                        await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                        
                        caught = True
                        break
                        
                    except Exception as eee:
                        if "too many public channels" in str(eee):
                            await IEX.send_message(
                                event.chat_id,
                                f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                            )
                            # ✅ الإصلاح هنا
                            caught = True
                            isclaim.clear()
                            isclaim.append("off")
                            break
                trys += 1
            
            # إذا تم كسر الحلقة بسبب كثرة القنوات، نخرج
            if caught and "off" not in isclaim:
                break
            
        isclaim.clear()
        isclaim.append("off")
        
        if caught:
            await event.edit(f"**✅ تم الصيد بنجاح! @{username}**\n**⏹️ توقف الفحص بعد {trys} محاولة**")
        else:
            await event.edit(f"**⏹️ توقف الفحص بعد {trys} محاولة**\n**❌ لم يتم صيد أي يوزر**")
        
        # تنظيف الملف المؤقت
        try:
            os.remove(file_path)
        except:
            pass
################################################################
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد_نمط (.*)"))
async def pattern_hunt(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        
        # الحصول على الأنماط وعدد المحاولات
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        patterns_input = str(msg[0])
        num_tries = int(msg[1]) if len(msg) > 1 and msg[1].isdigit() else 0
        
        # فصل الأنماط
        patterns = []
        if '.' in patterns_input:
            patterns = patterns_input.split('.')
        elif '،' in patterns_input:
            patterns = patterns_input.split('،')
        else:
            patterns = [patterns_input]
        
        # تنظيف الأنماط
        patterns = [pattern.strip() for pattern in patterns if pattern.strip()]
        
        if not patterns:
            await event.edit("**❌┊لم يتم تحديد أي نمط صحيح**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # ✅ التحقق: يجب أن يكون النمط 5 أحرف على الأقل
        short_patterns = []
        for pattern in patterns:
            if len(pattern) < 5:
                short_patterns.append(pattern)
        
        if short_patterns:
            error_message = f"**❌┊ الأنماط التالية قصيرة جداً:**\n"
            for short in short_patterns:
                error_message += f"• `{short}` ({len(short)} أحرف)\n"
            error_message += "\n**⛔┊ يجب أن يحتوي النمط على 5 أحرف على الأقل**"
            error_message += "\n**⏹️┊ تم إيقاف العملية**"
            
            await event.edit(error_message)
            isclaim.clear()
            isclaim.append("off")
            return
        
        # ✅ التحقق من الأنماط التي تبدأ برموز ممنوعة ($ + &)
        invalid_start_patterns = []
        forbidden_starts = ['%', '+', '&']
        
        for pattern in patterns:
            # إذا كان النمط يبدأ برمز ممنوع
            if pattern and pattern[0] in forbidden_starts:
                invalid_start_patterns.append(pattern)
        
        # إذا وجد أنماط تبدأ برموز ممنوعة
        if invalid_start_patterns:
            error_message = f"**❌┊ الأنماط التالية غير صالحة (تبدأ برموز ممنوعة):**\n"
            for invalid in invalid_start_patterns:
                error_message += f"• `{invalid}`\n"
            error_message += "\n**⛔┊ الرموز التالية ممنوعة في بداية النمط: $ + &**"
            error_message += "\n**⏹️┊ تم إيقاف العملية**"
            
            await event.edit(error_message)
            isclaim.clear()
            isclaim.append("off")
            return
        
        # ✅ التحقق: يرفض أي نمط يبدأ برقم (حتى بدون رموز)
        invalid_digit_patterns = []
        
        for pattern in patterns:
            # إذا كان النمط يبدأ برقم (أي رقم)
            if pattern and pattern[0].isdigit():
                invalid_digit_patterns.append(pattern)
        
        # إذا وجد أنماط تبدأ برقم
        if invalid_digit_patterns:
            error_message = f"**❌┊ الأنماط التالية غير صالحة (تبدأ برقم):**\n"
            for invalid in invalid_digit_patterns:
                error_message += f"• `{invalid}`\n"
            error_message += "\n**⛔┊ ممنوع بدء النمط بأي رقم**"
            error_message += "\n**⏹️┊ تم إيقاف العملية**"
            
            await event.edit(error_message)
            isclaim.clear()
            isclaim.append("off")
            return
        
        replly = await event.get_reply_message()
        
        # إنشاء القناة أو استخدام القناة المردودة
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                if num_tries > 0:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالأنماط .. بنجـاح ☑️**\n**✥┊ الأنماط:** `{' . '.join(patterns)}`\n**✥┊ على القنـاة:** {ch}\n**✥┊ عدد المحاولات:** {num_tries}\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                else:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالأنماط .. بنجـاح ☑️**\n**✥┊ الأنماط:** `{' . '.join(patterns)}`\n**✥┊ على القنـاة:** {ch}\n**✥┊ عدد المحاولات:** لا نهائي\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
            else:
                ch = await IEX(functions.channels.CreateChannelRequest(
                    title="SVJ Pattern Hunting Channel",
                    about=f"This channel to hunt usernames by - @PP6ZZ, {IEX_USER}",
                ))
                ch = ch.updates[1].channel_id
                
                photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
                try:
                    await IEX(functions.channels.EditPhotoRequest(channel=ch, photo=photo))
                except Exception:
                    pass
                
                invite = await IEX(functions.messages.ExportChatInviteRequest(peer=ch))
                invite_link = invite.link
                
                if num_tries > 0:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالأنماط .. بنجـاح ☑️**\n**✥┊ الأنماط:** `{' . '.join(patterns)}`\n**✥┊ على القنـاة:** [اضغط هنا]({invite_link})\n**✥┊ عدد المحاولات:** {num_tries}\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                else:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالأنماط .. بنجـاح ☑️**\n**✥┊ الأنماط:** `{' . '.join(patterns)}`\n**✥┊ على القنـاة:** [اضغط هنا]({invite_link})\n**✥┊ عدد المحاولات:** لا نهائي\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة: {str(e)}")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # بدء عملية الصيد
        Checking = True
        caught = False
        current_try = 0
        
        while True:
            if ispay[0] == 'no' or "off" in isclaim:
                break
                
            if num_tries > 0 and current_try >= num_tries:
                await event.client.send_message(event.chat_id, "! انتهت المحاولات دون صيد يوزر")
                break
                
            current_pattern = random.choice(patterns)
            username = generate_similar_pattern(current_pattern)
            
            if username is None:
                continue
                
            t = Thread(target=lambda q, arg1: q.put(check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            
            if "Available" in isav:
                await asyncio.sleep(0.8)
                try:
                    # ✅ الخطوة 1: تغيير يوزر القناة
                    await IEX(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                    
                    # ✅ الخطوة 2: تغيير اسم القناة إلى اسم اليوزر
                    await IEX(functions.channels.EditTitleRequest(
                        channel=ch,
                        title=username
                    ))
                    
                    
                    await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Pattern : {current_pattern}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                    await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Pattern : {current_pattern}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                    
                    caught = True
                    break
                    
                except Exception as eee:
                    if "too many public channels" in str(eee):
                        await IEX.send_message(event.chat_id, f"""- خطأ بصيـد اليـوزر تملك الكثير من القنوات @{username}""")
                        break
            else:
                pass
                
            trys += 1
            current_try += 1
             
        isclaim.clear()
        isclaim.append("off")
        if caught:
            await event.client.send_message(event.chat_id, f"! تم صيد اليوزر بنجاح: @{username} (النمط: {current_pattern})")

################################################################
def generate_unified_pattern(pattern, avoid_sequences=None):
    """
    دالة موحدة لتوليد الأنماط مع دعم جميع الرموز
    - * : حرف أو رقم عشوائي (a-z, 0-9)
    - # : حرف إنجليزي فقط (a-z)
    - % : 3 أرقام متسلسلة (فقط 123, 456, 789)
    - $ : حرف عشوائي ثابت (a-z) - يثبت مرة واحدة لكل عملية صيد
    - & : رقم عشوائي ثابت (0-9) - يثبت مرة واحدة لكل عملية صيد
    - أي حرف آخر: يبقى ثابتاً
    """
    if avoid_sequences is None:
        avoid_sequences = []
    
    result = []
    i = 0
    length = len(pattern)
    
    # إنشاء حرف ثابت للرمز $ (يولد مرة واحدة ويستخدم لنفس العملية)
    fixed_char = None
    if '$' in pattern:
        fixed_char = random.choice(string.ascii_lowercase)
    
    # إنشاء رقم ثابت للرمز &
    fixed_digit = None
    if '&' in pattern:
        fixed_digit = str(random.randint(0, 9))
    
    while i < length:
        char = pattern[i]
        
        if char == '*':
            # حرف أو رقم عشوائي (a-z, 0-9)
            result.append(random.choice(string.ascii_lowercase + string.digits))
        elif char == '#':
            # حرف إنجليزي فقط (a-z)
            result.append(random.choice(string.ascii_lowercase))
        elif char == '%':
            # 3 أرقام متسلسلة (فقط 123, 456, 789)
            allowed_patterns = ['123', '456', '789']
            numbers = random.choice(allowed_patterns)
            result.append(numbers)
            i += 2  # تخطي الموضعين الإضافيين
        elif char == '$':
            # حرف صغير عشوائي ثابت (نفس الحرف لكل العملية)
            if fixed_char is not None:
                result.append(fixed_char)
            else:
                result.append(random.choice(string.ascii_lowercase))
        elif char == '&':
            # رقم عشوائي ثابت (نفس الرقم لكل العملية)
            if fixed_digit is not None:
                result.append(fixed_digit)
            else:
                result.append(str(random.randint(0, 9)))
        else:
            # أي حرف آخر يضاف كما هو
            result.append(char)
        i += 1
    
    # تحويل القائمة إلى سلسلة نصية
    result = ''.join(result)
    
    # التأكد من أن الطول بين 5-32 حرف ولا يبدأ برقم
    if len(result) < 5:
        needed = 5 - len(result)
        result += ''.join(str(random.randint(0, 9)) for _ in range(needed))
    elif len(result) > 32:
        result = result[:32]
    
    # إذا بدأ برقم، نضيف حرف في البداية
    if result and result[0].isdigit():
        result = random.choice(string.ascii_lowercase) + result[1:]
    
    # تجنب المتواليات غير المرغوبة
    for seq in avoid_sequences:
        if seq in result:
            # إذا وجدنا متوالية غير مرغوبة، نعيد توليد النمط
            return generate_unified_pattern(pattern, avoid_sequences)
    
    return result

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد_مخصص (.*)"))
async def unified_pattern_hunt(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        
        # الحصول على النمط وعدد المحاولات والخيارات
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        pattern = str(msg[0])
        
        # إذا لم يتم تحديد عدد المحاولات أو كان 0، يصبح لا نهائي
        if len(msg) > 1 and msg[1].isdigit():
            num_tries = int(msg[1])
            unlimited = False
        else:
            num_tries = 0
            unlimited = True  # وضع لا نهائي
        
        # التحقق من وجود خيارات إضافية
        avoid_sequences = []
        if len(msg) > 2:
            options = msg[2].lower()
            if 'no123' in options:
                avoid_sequences.extend(['123', '456', '789'])
        
        # التحقق من صحة النمط الأساسي
        if len(pattern.replace('*', '').replace('#', '').replace('%', '').replace('$', '').replace('&', '')) < 2:
            await event.edit("**❌┊النمط قصير جداً! يجب أن يحتوي على الأقل على حرفين**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # التحقق المبدئي إذا النمط يمكن أن ينتج اسم صالح
        test_username = generate_unified_pattern(pattern, avoid_sequences)
        if test_username is None or (test_username and test_username[0].isdigit()):
            await event.edit("**❌┊النمط غير صالح! لا يمكن توليد اسم يلبي الشروط:**\n**• 5 أحرف على الأقل**\n**• لا يبدأ برقم**\n**• لا يزيد عن 32 حرف**")
            isclaim.clear()
            isclaim.append("off")
            return
        
        replly = await event.get_reply_message()
        
        # إنشاء القناة أو استخدام القناة المردودة
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                if not unlimited:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالنمط .. بنجـاح ☑️**\n**✥┊ النمط:** `{pattern}`\n**✥┊ على القنـاة:** {ch}\n**✥┊ عدد المحاولات:** {num_tries}\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                else:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالنمط .. بنجـاح ☑️**\n**✥┊ النمط:** `{pattern}`\n**✥┊ على القنـاة:** {ch}\n**✥┊ عدد المحاولات:** لا نهائي\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
            else:
                ch = await IEX(functions.channels.CreateChannelRequest(
                    title="SVJ Unified Pattern Hunting Channel",
                    about=f"This channel to hunt usernames by - @PP6ZZ, {IEX_USER}",
                ))
                ch = ch.updates[1].channel_id
                
                try:
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
                    await IEX(functions.channels.EditPhotoRequest(channel=ch, photo=photo))
                except Exception:
                    pass
                
                invite = await IEX(functions.messages.ExportChatInviteRequest(peer=ch))
                invite_link = invite.link
                
                if not unlimited:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالنمط .. بنجـاح ☑️**\n**✥┊ النمط:** `{pattern}`\n**✥┊ على القنـاة:** [اضغط هنا]({invite_link})\n**✥┊ عدد المحاولات:** {num_tries}\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                else:
                    await event.edit(f"**✥┊ تم بـدء الصيد بالنمط .. بنجـاح ☑️**\n**✥┊ النمط:** `{pattern}`\n**✥┊ على القنـاة:** [اضغط هنا]({invite_link})\n**✥┊ عدد المحاولات:** لا نهائي\n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**")
                
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة: {str(e)}")
            isclaim.clear()
            isclaim.append("off")
            return
        
        # بدء عملية الصيد
        caught = False
        current_try = 0
        
        while True:
            if ispay[0] == 'no' or "off" in isclaim:
                break
                
            # إذا كان هناك حد للمحاولات وتحقق (وليس لا نهائي)
            if not unlimited and current_try >= num_tries:
                await event.client.send_message(event.chat_id, "! انتهت المحاولات دون صيد يوزر")
                break
                
            # توليد اسم مستخدم بناءً على النمط
            username = generate_unified_pattern(pattern, avoid_sequences)
            
            # إذا لم يتم توليد اسم صالح، ننتقل للمحاولة التالية
            if not username:
                trys += 1
                current_try += 1
                continue
                
            t = Thread(target=lambda q, arg1: q.put(check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            
            if "error" in isav:
                await IEX.send_message(event.chat_id, f"**حدث خطأ في فحص اليوزر: @{username}**")
                continue
            
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await IEX(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                    
                    await event.client.send_file(event.chat_id, "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Pattern : {pattern}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr 
    ''')
                    await event.client.send_file("@PP6ZZ", "https://t.me/vgyhjhh/5", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Pattern : {pattern}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @PP6ZZ ) @r6r6rr ''')
                    
                    caught = True
                    break
                    
                except Exception as eee:
                    if "too many public channels" in str(eee):
                        await IEX.send_message(event.chat_id, f"""- خطأ بصيـد اليـوزر @{username}""")
                        break
            else:
                pass
                
            trys += 1
            current_try += 1
            
        isclaim.clear()
        isclaim.append("off")
        if caught:
            await event.client.send_message(event.chat_id, f"! تم صيد اليوزر بنجاح: @{username}")
##################################################################################
#def generate_navigation_buttons(current_type, max_index):
#    buttons = []
#    if current_type != "Types1":
#        buttons.append(Button.inline("Next", data="next"))
#    if current_type != "Types3":
#        buttons.append(Button.inline("Previous", data="previous"))
#    return buttons

#current_type = "Types1"
#by  @PP6ZZ
#@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
#async def show_types(event):
#    types_text = Types[current_type]
#    buttons = generate_navigation_buttons(current_type, len(Types))
#    await event.respond(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="next"))
#async def show_next_types(event):
#    global current_type
#    if current_type != "Types1":
#        current_type = f"Types{int(current_type[-1]) + 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="previous"))
#async def show_previous_types(event):
#    global current_type
#    if current_type != "Types3":
#        current_type = f"Types{int(current_type[-1]) - 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)ttons)))
