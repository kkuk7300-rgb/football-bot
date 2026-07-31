"""
Telegram-бот: расписание футбольных матчей + аналитика.
"""

import asyncio
import logging
from datetime import date, timedelta

import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import BOT_TOKEN, FOOTBALL_API_KEY

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

API_BASE = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": FOOTBALL_API_KEY}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
