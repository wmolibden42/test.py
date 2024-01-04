from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_start = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard= True)
kb_st1 = KeyboardButton('Помощь')
#kb_mn1 = KeyboardButton('Спасибо!')
kb_start.add(kb_st1)

#kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#kb_mn1 = KeyboardButton('Спасибо!')
#kb_menu.add(kb_mn1)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton ('Статистика сегодня')
kb2 = KeyboardButton ('Статистика месяц')
kb3 = KeyboardButton ('Помощь')
kb.add(kb1, kb2, kb3)

inkb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Подъем',
                           callback_data='up_time')
ib2 = InlineKeyboardButton(text='Отбой',
                           callback_data='down_time')
ib3 = InlineKeyboardButton(text='Настроение',
                           callback_data='happy_stat')
ib4 = InlineKeyboardButton(text='Вернуться в автоматический режим',
                           callback_data='close')

inkb.add(ib1,ib2,ib3).add(ib4)



#@dp.message(F.text.lower() == "Отбой")
#async def with_puree(message: types.Message):
#    await message.reply("Напиши время отхода ко сну вчера:")

#@dp.message(F.text.lower() == "Подъем")
#async def without_puree(message: types.Message):
#    await message.reply("В какое время ты проснулась сегодня?: ")
#ikb.add(ib1, ib2, ib3)