#aiogram aiomongo  

from aiogram import Bot, types
from pymongo import MongoClient
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.helper import Helper, HelperMode, Item
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.utils.markdown import text, bold, code
from aiogram.types import ParseMode, ReplyKeyboardRemove

from keyboard import board_1, board_3
from functions import parser, db_list, create_inline_keyboard, create_reply_keyboard, create_reply_keyboard_1
from config import TOKEN, MAIN_DB, ADMIN_DB, PASSWORD

client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db[MAIN_DB]
adm_collection = db[ADMIN_DB]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MongoStorage())

class States(Helper):
    mode = HelperMode.snake_case
    ADMIN = Item()
    FIO = Item()
    DOLJ = Item()
    ADRESS = Item()
    EMAIL = Item()
    PHONE = Item()
    CHANGE = Item()

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    js = new_collection.find({}, { '_id' : 0})
    full = db_list(js)
    code = callback_query.data[-1]
    if  code.isdigit():
        code = int(code)
        full_text = ''
        for i in range(len(full)):
            if code == i:
                for g in full[i]:
                    full_text += g + '\n'
                await bot.send_message(callback_query.from_user.id, full_text)

@dp.message_handler(commands=['start'], state = '*')
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Добрейший вечерочек!\nПиши /help, '
                        'чтобы узнать список доступных команд!')

@dp.message_handler(commands=['help'], state = '*')
async def process_help_command(msg: types.Message):
    mess = text(bold('Смотри, я могу ответить за следующее:'),
                '/info - выведет список', '/worker - поиск по должности', 
                '/edit - внесение изменений', sep = "\n")
    await bot.send_message(msg.from_user.id, mess, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['edit'], state = '*')
async def admin_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Введите пароль для перехода в режим администратора: ')  
    #проверка пароля

@dp.message_handler(commands=['info'], state = '*')
async def list_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Как много информации тебе нужно?", reply_markup=board_1)
    #клав полная - фио

@dp.message_handler(commands=['worker'], state = '*')
async def process_worker_command(msg: types.Message):
    board_2 = create_inline_keyboard()
    await bot.send_message(msg.from_user.id, "Вот все руководство, выбирай", reply_markup=board_2)
    #выводит клав с должностями

@dp.message_handler(state=States.ADMIN, content_types=['text'])
async def admin(msg: types.Message, state: FSMContext):
    text = msg.text
    user_id = msg.from_user.id
    print(user_id)
    fio = ''
    if text == 'Создать':
        if fio == '':
            await state.set_state(States.FIO)
            await msg.reply('Введи фио')
            return
    elif text == 'Изменить':
        board_4 = create_reply_keyboard()
        await state.set_state(States.CHANGE)
        js = adm_collection.find({}, { 'doljname' : 1, '_id' : 0})
        full = db_list(js)
        g = 1
        full_text = ''
        for elem in full:
            for i in elem:
                full_text += f'{g}' + '. ' + i + '\n'
                g += 1
        await bot.send_message(msg.from_user.id, full_text)
        await bot.send_message(msg.from_user.id, "Это весь список, кого будем редактировать?", reply_markup=board_4)
        #фамилия+ параметр замены
    elif text == 'Удалить':
        pass
        #фамилия+ удаление дока
    elif text == 'Сохранить':
        new_collection.remove({})
        docs = adm_collection.find({},{'_id' : 0})
        full = []
        for doc in docs:
            if 'admin_id' in doc:
                if doc['admin_id'] == user_id:
                    adm_collection.update({'doljname' : doc[doljname]}, {'$unset': {'admin_id' : 1}})
                doc.pop['admin_id']
            full.append(doc)
        new_collection.insert_many(full)
        await state.reset_state()
        await bot.send_message(msg.from_user.id, "Все изменения сохранены. Больше ты не админ", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state=States.FIO, content_types=['text'])
async def fio(msg: types.Message, state: FSMContext):
    fio = msg.text
    fio = fio.split(' ')
    await state.set_state(States.ADMIN)
    await state.update_data(Fname=fio[0])
    await state.update_data(Name=fio[1])
    await state.update_data(Oname=fio[2])
    await state.set_state(States.DOLJ)
    await bot.send_message(msg.from_user.id, "Введи должность:" )

@dp.message_handler(state=States.DOLJ, content_types=['text'])
async def dolj(msg: types.Message, state: FSMContext):
    dolj = msg.text
    await state.set_state(States.ADMIN)
    await state.update_data(doljname=dolj)
    await state.set_state(States.ADRESS)
    await bot.send_message(msg.from_user.id, "Введи кабинет: ")

@dp.message_handler(state=States.ADRESS, content_types=['text'])
async def adress(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.set_state(States.ADMIN)
    await state.update_data(Room=adress)
    await state.set_state(States.PHONE)
    await bot.send_message(msg.from_user.id, "Введи телефон: ")

@dp.message_handler(state=States.PHONE, content_types=['text'])
async def phone(msg: types.Message, state: FSMContext):
    phone = msg.text
    await state.set_state(States.ADMIN)
    await state.update_data(Phone=phone)
    await state.set_state(States.EMAIL)
    await bot.send_message(msg.from_user.id, "Введи email: ")

@dp.message_handler(state=States.EMAIL, content_types=['text'])
async def email(msg: types.Message, state: FSMContext):
    email = msg.text
    await state.set_state(States.ADMIN)
    await state.update_data(Mail=email)
    user_data = await state.get_data()
    results = []
    results.append(user_data)
    adm_collection.insert_many(results)
    await bot.send_message(msg.from_user.id, "Если это все, что ты хотел - жми 'Сохранить', "
                            "ну или выбирай, что будем делать", reply_markup=board_3)

@dp.message_handler(state=States.CHANGE, content_types=['text'])
async def change(msg: types.Message, state: FSMContext):
    text = msg.text
    board_5 = create_reply_keyboard_1
    if  text.isdigit():
        code = int(text)
        #проверка по id
        change = adm_collection.find({}, {'_id' : 0}).skip(code-1).limit(1)
        full = db_list(change)
        user_id = msg.from_user.id
        if len(full[0]) > 7:
            if full[0][7] == user_id:
                await bot.send_message(msg.from_user.id, 'Редактирование сейчас недоступно, выберите другого человека', reply_markup=board_4)
                return
        else:
            adm_collection.update({'doljname' : full[0][0]}, {'$set': {'admin_id' : user_id}})
        await state.update_data(code=text)
        full_text = ''
        for elem in full:
            for value in elem:
                full_text += value + '\n'
        await bot.send_message(msg.from_user.id, full_text)
        await bot.send_message(msg.from_user.id, "Что будем менять?", reply_markup=board_5)
    elif text == 'Назад':
        await state.set_state(States.ADMIN)
        await bot.send_message(msg.from_user.id, "Если это все, что ты хотел - жми 'Сохранить', "
                            "ну или выбирай, что будем делать", reply_markup=board_3)
    else:
        butt_list = ['Должность', 'Фамилия', 'Имя', 'Отчество', 'Кабинет', 'Телефон', 'Email']
        key_list = ['doljname', 'Fname', 'Name', 'Oname', 'Room', 'Phone' 'Mail']
        for i in range(len(butt_list)):
            if text == butt_list[i]:
                await state.update_data(text=i)
                await bot.send_message(msg.from_user.id, "Введи новое значение")
                return
        data = await state.get_data()
        if 'text' in data:
            code = int(data['code'])
            num = int(data['text'])
            change = adm_collection.find().skip(code-1).limit(1)
            full = db_list(change)
            adm_collection.update({'doljname' : full[0][0], 'Fname' : full[0][1]}, {'$set': {key_list[num] : text}})
            await state.set_state(States.ADMIN)
            await bot.send_message(msg.from_user.id, "Если это все, что ты хотел - жми 'Сохранить', ну или выбирай, что будем делать", reply_markup=board_3)
        else:
            await bot.send_message(msg.from_user.id, "Выбери, что будем менять на клавиатуре, либо напиши 'Назад', вернуться", reply_markup=board_5)

@dp.message_handler(content_types=['text'], state = '*')
async def echo(msg: types.Message, state: FSMContext):
    text = msg.text
    if text == 'Полная':
        js = new_collection.find({}, { '_id' : 0})
        full = db_list(js)
        for elem in full:
            full_text = ''
            for i in elem:
                full_text += i + '\n'
            await bot.send_message(msg.from_user.id, full_text)
    elif text == 'Фио':
        js = new_collection.find({}, { 'doljname' : 1, 'Fname' : 1, 'Name': 1, 'Oname': 1, '_id' : 0})
        full = db_list(js)
        for elem in full:
            full_text = []
            for i in elem:
                full_text.append(i)
            full_text.insert(1, '-')
            full_text = ' '.join(full_text)
            await bot.send_message(msg.from_user.id, full_text)
    elif text == PASSWORD:
        await state.set_state(States.ADMIN)
        check = await state.get_state()
        print(check)
        await bot.send_message(msg.from_user.id, "Теперь ты админ, что будем делать?", reply_markup=board_3)
    else:
        await bot.send_message(msg.from_user.id, 'Я не знаю таких слов')

if __name__ == '__main__':
    #parser()
    executor.start_polling(dp)