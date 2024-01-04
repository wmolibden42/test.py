from aiogram import Bot, Dispatcher, executor, types
from keyboard import kb, inkb, kb_start
from aiogram.types import ReplyKeyboardRemove, InlineQueryResultArticle, InputTextMessageContent
import asyncio
import aiogram
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import hashlib
from aiogram.dispatcher import FSMContext

storage = MemoryStorage ()

#import sqlite3
#import basa as db
#from basa import create_profile, db_start, edit_profile

TOKEN_API = ('6704702920:AAHiV01ua2oTWCP8c6skC6IYFU5OVjUX-5o')
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())

class ProfileStateGroup (StatesGroup):
     up_time = State ()
     down_time = State ()
     happy_stat = State ()

cb = CallbackData('ikb', 'action')

async def on_startup(_):
    #await db_start()
    print('I redy')

@dp.message_handler(commands=['start'])
async def cmd_start_db(message: types.Message):
    await message.answer(text='''
Привет! 
Я твой незаменимый помощник! 
Постараюсь сделать так, чтобы все было понятно! 
Я автоматический, но всегда готов помочь!
                            ''', reply_markup = kb_start)
    await message.delete()
    #await create_profile(user_id=message.from_user.id)


@dp.message_handler(text=["Помощь", 'help', "помощь"])
async def help_comm(message: types.Message):
    await message.answer(text='''
Привет! 
Я работаю в автоматическом режиме. 
Когда придет время, я напомню о себе, но если ты не успела ответить на мои вопросы или же я не сработал или сработал не верно, ты можешь в ручную ввести данные, которые мы пропустили! 
Для этого выбери необходимую кнопку и введи значение, которое хочешь зафиксировать!
    ''', reply_markup= inkb)

@dp.callback_query_handler(text='close')
async def ikb_cb_handler(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback_query.from_user.id, text = '''
Ты вернулась в главное меню!
Я твой незаменимый помощник! 
Постараюсь сделать так, чтобы все было понятно! 
Я автоматический, но всегда готов помочь!
                                                                       ''', reply_markup=kb_start)
    await callback_query.message.delete()

@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery, state=None):
    if callback_query.data == 'up_time':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Запиши время подъема: ')
        await ProfileStateGroup.up_time.set()
    elif callback_query.data == 'down_time':
        await bot.send_message(chat_id=callback_query.from_user.id, text="Запиши время отбоя:")
        await ProfileStateGroup.down_time.set()
    elif callback_query.data == 'happy_stat':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Запиши свое настроение:')
        await ProfileStateGroup.happy_stat.set()

@dp.message_handler(content_types=['up_time'], state=ProfileStateGroup.up_time)
async def time_up_st(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['up_time'] = message.text
    await message.reply('Отлично, я запомнил время подъема!')
    await state.finish()

@dp.message_handler(content_types=['down_time'], state=ProfileStateGroup.down_time)
async def time_down_st(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['down_time'] = message.text
    await message.reply ('Отлично, я запомнил время отбоя"')
    await state.finish()


@dp.message_handler(content_types=['happy_stat'], state=ProfileStateGroup.happy_stat)
async def happy_stat_st(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['happy_stat'] = message.text

    await message.reply('Отлично, я записал твою оценку!')
    await state.finish()

@dp.message_handler()
async def ull_mess (message: types.Message):
    await message.answer ('Я еще не знаю, как реагировать на твое сообщение. Попробуй выбрать что-то из того, что есть в моих командах или дождись сообщения.'
                          ' Можешь написать мне "помощь"')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
#@dp.message_handler(text=['Подъем'])
#async def up_comm (message: types.Message):
#    await message.answer("Напиши время, в которое ты сегодня проснулась: ")

#@dp.message_handler()
#async def up_ans (message: types.Message):
        #up_answ = message.text
        #await message.answer('Отлично! Я запомнил!')


#@dp.message_handler(text=['Отбой'])
#async def down_comm (message: types.Message):
#    await message.answer("Зафиксируй время, когда ты отправилась спать вчера: ")

#@dp.message_handler(text=['Настроение'])
#async def happy_comm (message: types.message):
#    await message.answer('Запиши свое настроение в данный момент. Что с тобой случилось за сегодня? Расскажи обо всем, чем бы тебе хотелось поделиться:')
       # async def down_p (d_p: types.Message):
          #  await bot.send_message(down_p.from_user.id, down_p.text)
#@db.callback_query_handler()
#async def funck_calback(calback: types.CallbackQuery)



