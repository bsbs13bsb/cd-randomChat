"""
عبر هذا الملف يتم ملئ المعلومات الاساسية
https://t.me/BotFather يمكنك جلب التوكن الخاص بالبوت عبر هذا البوت
"""

VERSION = "v2.2.1"

# ضع توكن البوت هنا
TOKEN = str("5358874912:AAH-FwXogXSsEEIHCCR9tMQkUjMi1RcVz-s")

# وضع الفرق بين كل رسالة ورسالة اخرى
delay = 1 # 1s

# اختيار عدد البلاغات الازمة لحظر العضو
max_reports = 10 # 10

# اختار اقصى مدة للجلسة
session_time = 60*20 # 20m

# لسهولة استعمال المتغيرات بين الملفات
import telebot
bot = telebot.TeleBot(TOKEN)
botName = bot.get_me().first_name
