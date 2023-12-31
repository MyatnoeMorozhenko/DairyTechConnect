import os
import psycopg2
import logging
from dotenv import load_dotenv

from aiogram import Bot, types, Dispatcher
from client_keyboard import keyb_client
from aiogram.utils import executor
from client_keyboard import keyb_client01

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)
DB_URL = os.getenv('DATABASE_URL')

### To connect with DATABASE
db = psycopg2.connect(DB_URL, sslmode='require')
db_object = db.cursor()

photo = open('DairyTech.jpeg', 'rb')

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    with open('DairyTech.jpeg', 'rb') as photo:
        await bot.send_photo(msg.from_user.id, caption = f"Добрый день, {msg.from_user.full_name}\!\n\nРады приветсвовать в нашем онлайн бизнес сообществе **DairyTech Connect** для специалистов молочной отрасли\.\n\n • Отраслевое сообщество для делового общения\n • Площадка для обмена новостями, экспертизой, аналитикой индустрии\n • Профильные онлайн\-мероприятия\n\n||Перейти на страницу сообщества можно, нажав на кнопку DairyTech Connect или по [ссылке](https://app.dairytech-connect.com/event/1099/feed)||",
                         parse_mode='MarkdownV2',photo=photo,
                         reply_markup=keyb_client)
    
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()
    
    if not result:
        db_object.execute("INSERT INTO users (id, username) VALUES (%s, %s)", (user_id, username))
        db.commit()
        
#Launch of messages distribution

@dp.message_handler(commands=['send'])
async def send(msg: types.Message):
    if msg.from_user.id == 5863593481:
        text = msg.text[6:]
        db_object.execute("SELECT id FROM users")
        result1 = db_object.fetchall()
        for row in result1:
                await bot.send_message(row[0], text)
        await bot.send_message(msg.from_user.id, "Успешная рассылка")

#WebApp handler

@dp.callback_query_handler(lambda c: True)
async def settings(callback_query: types.CallbackQuery):
    if callback_query.data == 'button3':
        await callback_query.message.edit_caption(
            'Чтобы зарегистрироваться или войти в сообшество, нажмите кнопку <b>DairyTech Connect</b>. \n\n<i>DairyTech Connect остается в Вашем телеграм 24/7, просматривайте новости, участвуйте и посещайте онлайн-мероприятия, обменивайтесь экспертным мнением, не выходя из телеграм.</i>',
            reply_markup=keyb_client01, parse_mode='HTML')
    if callback_query.data == 'website':
        await callback_query.message.edit_caption(
            'Ты на основной странице DairyTech Connect',
            reply_markup=keyb_client)
    if callback_query.data == 'back':
        await callback_query.message.edit_caption(f"Добрый день, {callback_query.from_user.full_name}\!\n\nРады приветсвовать в нашем онлайн бизнес сообществе **DairyTech Connect** для специалистов молочной отрасли\.\n\n • Отраслевое сообщество для делового общения\n • Площадка для обмена новостями, экспертизой, аналитикой индустрии\n • Профильные онлайн\-мероприятия\n\n||Перейти на страницу сообщества можно, нажав на кнопку DairyTech Connect или по [ссылке](https://app.dairytech-connect.com/event/1099/feed)||",
            reply_markup=keyb_client, parse_mode='MarkdownV2')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


