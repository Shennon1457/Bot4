from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key1():
    keyboard1 = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Переключиться на клавиатуру 2', callback_data='go_to_2')
    button2 = InlineKeyboardButton('Отправь случайное число', callback_data='send_random')
    keyboard1.add(button1, button2)
    return keyboard1


def key2():
    keyboard2 = InlineKeyboardMarkup(row_width=1)
    button3 = InlineKeyboardButton('Переключиться на клавиатуру 1', callback_data='go_to_1')
    button4 = InlineKeyboardButton('Текущее время', callback_data='send_datatime')
    button5 = InlineKeyboardButton('Биография леди Гаги', callback_data='ladyGaga')
    keyboard2.add(button3, button4, button5)
    return keyboard2
