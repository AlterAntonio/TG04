from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Reply-клавиатура с привет/пока кнопками
reply_kbrd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет!'), KeyboardButton(text='Пока!')]
], resize_keyboard=True)

# Inline-клавиатура со ссылками
inline_kbrd_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://catsroom24.com/koty-kontroliruyut-lichnuyu-zhizn-svoih-vladelcev')],
    [InlineKeyboardButton(text='Музыка', url='https://www.youtube.com/watch?v=vV_7OQOEPRU')],
    [InlineKeyboardButton(text='Видео', url='https://www.youtube.com/watch?v=KmHkajDI97o')]
])

# Inline-клавиатура с кнопкой, изменяющей сообщение и клавиатуру
inline_kbrd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data='show_more')]
])

# Билдер Inline-клавиатуры для опциональных кнопок
options = ['Опция 1', 'Опция 2']
async def inline_builder():
    kbrd = InlineKeyboardBuilder()
    for key in options:
        kbrd.add(InlineKeyboardButton(text=key, callback_data=key))
    return kbrd.as_markup()