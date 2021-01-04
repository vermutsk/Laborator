from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

butt_full = KeyboardButton('Полная')
butt_fio = KeyboardButton('Фио')
butt_new = KeyboardButton('Создать')
butt_change = KeyboardButton('Изменить')
butt_delete = KeyboardButton('Удалить')
butt_save = KeyboardButton('Сохранить')
board_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(butt_full, butt_fio)
board_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(butt_new, butt_change, butt_delete).add(butt_save)