from sre_parse import State
from aiogram.dispatcher.filters.state import StatesGrop


class Stats(StatesGrop):
    stats_one = State()
    stats_two = State()
