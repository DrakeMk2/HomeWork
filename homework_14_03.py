from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

inline_buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1 Яблоко', callback_data='product_buying')],
        [InlineKeyboardButton(text='2 Яблока', callback_data='product_buying')],
        [InlineKeyboardButton(text='3 Яблока', callback_data='product_buying')],
        [InlineKeyboardButton(text='4 Яблока', callback_data='product_buying')]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; '
        f'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий вашему здоровью.', reply_markup=kb)
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Астродройд модели R2-D2.')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    print('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    print('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    print('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f'Ваша норма каллорий: {result} (+5 для мужчин, или -161 для женщин).')
    print(f'Ваша норма каллорий: {result}')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer(text='Название: Яблоки | Описание: 1 штука | Цена: 100')
    with open('product_1.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Яблоки | Описание: 2 штуки | Цена: 200')
    with open('product_2.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Яблоки | Описание: 3 штуки | Цена: 300')
    with open('product_3.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Яблоки | Описание: 4 штуки | Цена: 400')
    with open('product_4.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_buying)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer(f'Нажмите на /start, чтобы начать общение.')
    print(f'Нажмите на /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
