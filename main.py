




import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards.menu_keyboard import *
from filters.menu_filters import *
from aiogram.types import FSInputFile


TOKEN = ''
dp = Dispatcher()

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = get_start_keyboard()
    await message.answer(f"Hello,choose the language!",reply_markup=keyboard)


@dp.message(LanguageFilter("English 🇬🇧"))
async def english_menu_filter(message: Message) -> None:
    link = await bot.create_chat_invite_link(chat_id=-1002027704795,member_limit=1)
    keyboard = get_english_keyboard(link)
    photo = FSInputFile('photo.jpeg')
    await message.answer_photo(photo=photo,caption=f"Welcome to the Tremendous Growth Private Group!\n 🌟 Here, you'll discover a wealth of knowledge on income enhancement, investment strategies, and direct access to my company's resources.\n I'm here to guide you, teach you new skills, and share insights from my personal entrepreneurial journey in Dubai over the past 7 years. \nLet's embark on this transformative journey together! 💼✨",reply_markup=keyboard)

@dp.message(LanguageFilter("Русский 🇷🇺"))
async def russian_menu_filter(message: Message) -> None:
    link = await bot.create_chat_invite_link(chat_id=-1002027704795,member_limit=1)
    keyboard = get_russian_keyboard(link)
    photo = FSInputFile('photo.jpeg')
    await message.answer_photo(photo=photo,caption=f"Добро пожаловать в частную группу Tremendous Growth!\n 🌟 Здесь вы откроете для себя массу знаний об увеличении дохода, инвестиционных стратегиях и прямой доступ к ресурсам моей компании. \nЯ здесь, чтобы направлять вас, научить новым навыкам и поделиться идеями из моего личного предпринимательского пути в Дубае за последние 7 лет. \nДавайте вместе отправимся в это преобразующее путешествие! 💼✨",reply_markup=keyboard,)

@dp.message(LanguageFilter('Ελληνικά 🇬🇷'))
async def greace_menu_filter(message: Message) -> None:
    link = await bot.create_chat_invite_link(chat_id=-1002027704795,member_limit=1)
    keyboard = get_greace_keyboard(link)
    photo = FSInputFile('photo.jpeg')
    await message.answer_photo(photo=photo,caption='Καλώς ήρθατε στον Ιδιωτικό Όμιλο Τεράστιας Ανάπτυξης! \n🌟 Εδώ, θα ανακαλύψετε πλήθος γνώσεων σχετικά με τη βελτίωση του εισοδήματος, τις επενδυτικές στρατηγικές και την άμεση πρόσβαση στους πόρους της εταιρείας μου. \nΕίμαι εδώ για να σας καθοδηγήσω, να σας διδάξω νέες δεξιότητες και να μοιραστώ πληροφορίες από το προσωπικό μου επιχειρηματικό ταξίδι στο Ντουμπάι τα τελευταία 7 χρόνια.\n Ας ξεκινήσουμε μαζί αυτό το μεταμορφωτικό ταξίδι! 💼✨',reply_markup=keyboard)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())