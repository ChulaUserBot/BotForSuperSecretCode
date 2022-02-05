import logging,math, asyncio, sys
import aiogram as aio
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = aio.Bot('5144955139_AAH3Zzp812at5KByFB3KhLMeDsiAwAfIFDY'.replace("_",":"), parse_mode=types.ParseMode.HTML)
dp = aio.Dispatcher(bot, storage=MemoryStorage())
admin_code = '000'

logging.basicConfig(level=logging.INFO)




class States(StatesGroup):
    set_code = State()
    ignor = State()

@dp.message_handler(commands=['start'], state=None)
async def start_handler(message):
	await message.answer("Привет. Я бот с открытым исходным кодом(<a href='https://github.com/ChulaUserBot/BotForSuperSecretCode'>ссылка</a>), который сможет выдать тебе секретный код\nНо для доступа к коду ты должен написать пароль от админ пенели", disable_web_page_preview=True)
	await message.answer("Введите пароль:")
	await States.set_code.set()
  
@dp.message_handler(state=States.set_code)
async def code_handler(message):
    if message.text==admin_code:
        await message.answer("Успешно. Вы вошли в админ панель")
        await asyncio.sleep(1)
        await message.answer("Произошла неизвестная ошибка\nОшибка:<code>+Z8oHEwSuVXQ5YTgy</code>", parse_mode='html')
        await asyncio.sleep(1)
        await message.answer("Ошиббббббббббб!!?!:%?ка")
        await asyncio.sleep(.5)
        await message.answer("Система отключается....")
        await States.ignor.set()
    else:
        await message.answer("Неверный пароль")
  
    

aio.executor.start_polling(dp)
