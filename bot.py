import telebot

# حط التوكن تبعك هنا 👇
TOKEN = "8420983682:AAGZSY7UorXFxi0RIwSYPDt8ThH1Hmlv6VY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك! 🤖 البوت شغال تمام ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"انت قلت: {message.text}")

print("البوت شغال...")

bot.infinity_polling()
