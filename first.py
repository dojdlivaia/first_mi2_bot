import telebot
bot = telebot.TeleBot('1522150821:AAFON_2LEgvIdsNud9kE7BfnrW3W3yQSiqY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот МИ20. Приятно познакомиться, {message.from_user.first_name}')

bot.polling(none_stop=True)