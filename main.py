import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboards as kbrd

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда \start добавляет кнопки
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет, я - бот c кнопками.', reply_markup=kbrd.reply_kbrd)

# Тут список доступных команд и их описание
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Тут можно применить такие команды:\n/help - хелп;\n/start - тут можно поздороваться с ботом;'
                         '\n/links - кнопки со ссылками;\n/dynamic - пример с динамическим изменением клавиатуры.')

# Следующие два обработчика для Reply-кнопок, доступных после \start
@dp.message(F.text == 'Привет!')
async def hi_button(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

@dp.message(F.text == 'Пока!')
async def bye_button(message: Message):
    await message.answer(f"Пока, {message.from_user.full_name}!")

# Тут Inline-кнопки с необходимыми ссылками
@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Кошачьи новости. "Juicy.exe". "Никому не верю"', reply_markup=kbrd.inline_kbrd_links)

# Команда для вызова изменяемой Inline-клавиатуры
@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Показать больше?', reply_markup=kbrd.inline_kbrd)

@dp.callback_query(F.data == 'show_more')
async def more(callback: CallbackQuery):
    await callback.answer('Будет тебе больше')
    await callback.message.edit_text('Выбирай', reply_markup=await kbrd.inline_builder())

# Обработчик callback-запросов с комментариями бота
@dp.callback_query(F.data.in_(kbrd.options))
async def option(callback: CallbackQuery):
    selected = callback.data
    await callback.answer(f'Ты клацнул {selected}')
    await callback.message.answer(f'Ты клацнул {selected}')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())