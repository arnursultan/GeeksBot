from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton('Backend', callback_data='backend'),
    InlineKeyboardButton('Frontend', callback_data='frontend'),
    InlineKeyboardButton('UX/UI', callback_data='uxui'),
    InlineKeyboardButton('Android-разработка', callback_data='android'),
    InlineKeyboardButton('IOS-разработка', callback_data='ios'),
    InlineKeyboardButton('Контакты', callback_data='contact'),
]

button = InlineKeyboardMarkup().add(*buttons)