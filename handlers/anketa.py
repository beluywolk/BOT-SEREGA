from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_kb import submit_markup
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    age = State()
    direction = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.chat.type == 'private':
            await FSMAdmin.id.set()
            await message.answer(
                f"укажите id пользователя",

            )
        else:
            await message.answer('Пиши в личку!')


async def add_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        data['id'] = message.text
    await FSMAdmin.next()
    await message.answer('Как звать?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько лет?')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if not 1 < int(message.text) < 200:
            await message.answer('Доступ воспрещен!')
            await state.finish()
            return

        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Направление')
    except:
        await message.answer('Пиши числа!')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Группа')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await message.answer('Все верно???', reply_markup=submit_markup)
    await FSMAdmin.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await message.answer('Регистрация завершена')
        await state.finish()
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('НИПОНЯЛ')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_handlers_anketa(dp: Dispatcher):


    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(add_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
