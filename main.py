import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, types, Dispatcher
from client_keyboard import keyb_client
from aiogram.utils import executor
from client_keyboard import keyb_client01

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def buy(msg: types.Message):
    with open('DairyTech.jpeg', 'rb') as photo:
        await bot.send_photo(msg.from_user.id, caption = f"Добрый день, {msg.from_user.full_name}\!\n\nРады приветсвовать в нашем онлайн бизнес сообществе **DairyTech Connect** для специалистов молочной отрасли\.\n\n • Отраслевое сообщество для делового общения\n • Площадка для обмена новостями, экспертизой, аналитикой индустрии\n • Профильные онлайн\-мероприятия\n\n||Перейти на страницу сообщества можно, нажав на кнопку DairyTech Connect или по [ссылке](https://app.dairytech-connect.com/event/1099/feed)||",
                         parse_mode='MarkdownV2',photo=photo,
                         reply_markup=keyb_client)

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


