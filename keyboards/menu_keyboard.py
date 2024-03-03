from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from payments.paymants import get_payment_link

one_month_price_id = 'price_1OoQd7JrdIO4YObvc2cQl7NJ'
three_month_price_id = 'price_1OoQdMJrdIO4YObvNwIT8HdZ'
year_price_id = 'price_1OoQdaJrdIO4YObvqaNOdyKg'


def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='English 🇬🇧')],
                                             [KeyboardButton(text='Русский 🇷🇺')],
                                             [KeyboardButton(text='Ελληνικά 🇬🇷')],
                                             ],resize_keyboard=True,input_field_placeholder="Choose the language!",one_time_keyboard=True)
    return keyboard


def get_english_keyboard(link):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='1 month 49$',url=get_payment_link(one_month_price_id,link))],
         [InlineKeyboardButton(text='3 month 139$',url=get_payment_link(three_month_price_id,link))],
         [InlineKeyboardButton(text='1 year 1,999$',url=get_payment_link(year_price_id,link))],
         ]
    )
    return keyboard

def get_russian_keyboard(link):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text = '1 месяц 49$',url=get_payment_link(one_month_price_id,link))],
         [InlineKeyboardButton(text='3 месяца 139$',url =get_payment_link(three_month_price_id,link))],
         [InlineKeyboardButton(text='12 месяцев 1,999$',url = get_payment_link(year_price_id,link))]]
    )
    return keyboard

def get_greace_keyboard(link):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text = '1 μήνας 49$',url=get_payment_link(one_month_price_id,link))],
         [InlineKeyboardButton(text = '3 μήνες 139$',url=get_payment_link(three_month_price_id,link))],
         [InlineKeyboardButton(text='12 μήνες 1,999$',url=get_payment_link(year_price_id,link))],]
    )
    return keyboard