import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
import config

# Логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот активен')

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добрый день!")
    await message.answer("Что вам необходимо найти ?")








# Обработчик при ошибки "Блокировка бота"
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print (f'Пользователь заблокировал бота. \nСообщение: {update}\nОшибка: {exception}')
    return True

# Запуск процесса поллинга новых апдейтов
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
