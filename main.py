
import telebot
from flask import Flask, request

API_TOKEN = '7567723543:AAGNjg42d9DfEj3-rRRtWT56SdGFsyh6TCo'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return '', 403

@app.route('/')
def index():
    return 'Bot is running!', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلًا بك في بوت رحلة المليار 🚀")

@bot.message_handler(commands=['تشغيل', 'إيقاف'])
def control_recommendations(message):
    if message.text == '/تشغيل':
        bot.reply_to(message, "✅ تم تشغيل التوصيات.")
    elif message.text == '/إيقاف':
        bot.reply_to(message, "⛔ تم إيقاف التوصيات.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
