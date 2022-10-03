import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добрый день!")

# Запуск процесса поллинга новых апдейтов
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
