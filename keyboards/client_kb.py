from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")

share_location = KeyboardButton("Share location", request_location=True)
share_info = KeyboardButton("Share info", request_contact=True)

start_markup.add(start_button, info_button).add(share_location, share_info)



submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('Нет'))

