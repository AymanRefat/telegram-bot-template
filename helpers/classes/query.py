from abc import ABC, abstractmethod
from telebot import TeleBot
from logging import Logger


class BaseQuery(ABC):
    def __init__(self, bot: TeleBot, logger: Logger) -> None:
        self.bot = bot
        self.logger = logger

    def register(self) -> None:
        @self.bot.callback_query_handler(self.dispather)
        def somefunc(query):
            self.query(query)

        self.logger.info(f"{self.__class__.__name__} is installed")

    @abstractmethod
    def dispather(self, call) -> bool:
        """Should Return True or False whether mean Run the Query or Not"""

    @abstractmethod
    def query(self, query):
        """The Query"""
