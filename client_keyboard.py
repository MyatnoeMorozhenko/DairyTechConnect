from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

#Основное меню
"""b1 = InlineKeyboardButton('⚙️Настройки', callback_data='button1')"""
b2 = InlineKeyboardButton('Помощь', url='https://t.me/testingme_supportbot')
b3 = InlineKeyboardButton('📝 Инструкция', callback_data='button3')
back_to_menu = InlineKeyboardButton('Вернуться в главное меню', callback_data='back')
website = InlineKeyboardButton('DairyTech Connect', web_app=WebAppInfo(url = 'https://app.dairytech-connect.com/event/1099/feed'))

keyb_client = InlineKeyboardMarkup().add(b2).insert(b3).add(website)
keyb_client01 = InlineKeyboardMarkup().add(b2).insert(b3).add(website).add(back_to_menu)