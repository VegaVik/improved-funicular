
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


#функция обработки команды start
def start (update, context):
    update.message.reply_text('Добрый день!')

#функция обработки команды help
def help (update, context):
    update.message.reply_text('Какая помощь необходима')

def error(update, context):
    update.message.reply_text('Ошибка!')

#функция обработки текста
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'Did you said "{text_received}" ?')

def main():
    TOKEN = '5655755461:AAGKVQLPhUwZjuHcASlAbpKIZbsdOI25Pdg'
    
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #обработчик команд start/help
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    #обработчик текста
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    #обработчик ошибок
    dispatcher.add_error_handler(error)

    #запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


