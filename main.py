from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API
from keboards.key_in import key1, key2
import random
from datetime import datetime

bot = Bot(token=TELEGRAM_API)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы загрузить бота'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет ты на клавиатуре 1, нажми кнопку, чтобы перейти на вторую клавиатуру.', reply_markup=key1())


@dp.callback_query_handler(lambda c: c.data == 'send_random')
async def randon_num(callback_query: types.CallbackQuery):
    rand_num = random.randint(1, 100)
    await callback_query.message.answer(f'Ваше случайное число: {rand_num}')


@dp.callback_query_handler(lambda c: c.data == 'send_datatime')
async def send_datatime(callback_query: types.CallbackQuery):
    current_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f'Текущее время: {current_time}')


@dp.callback_query_handler(lambda c: c.data == 'ladyGaga')
async def send_datatime(callback_query: types.CallbackQuery):
    url = 'https://ru.wikipedia.org/wiki/Леди_Гага'
    await callback_query.message.answer(f'Биография Леди Гаги {url}')


@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на вторую клавиатуру', reply_markup=key2())


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на первую клавиатуру', reply_markup=key1())


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

