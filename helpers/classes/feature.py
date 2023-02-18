from abc import ABC, abstractclassmethod
from telebot import types
from telebot import TeleBot
from .query import BaseQuery
from .command import BaseCommand
from logging import Logger


class BaseFeature(ABC):
    """Base Class to Inherit from , has all about the Feature (Installed Files , Commands , install Function )"""

    commands:list[BaseCommand]
    register_message: str = "Feature Installed"
    queries: list[BaseQuery]

    def __init__(self, bot: TeleBot, logger: Logger = None) -> None:
        self.logger = logger
        self.bot = bot

    def __register_commands(self) -> None:
        """Register all Written commands in the list"""
        for command in self.commands:
            command(self.bot, logger=self.logger).register()

    def __register_queries(self) -> None:
        """Register all Written queries in the list"""
        for query in self.queries:
            query(self.bot, self.logger).register()

    def register(self) -> None:
        self.__register_commands()
        self.__register_queries()
        self.logger.info(f"{self.__class__.__name__}  is installed")

    @classmethod
    def get_bot_commands(self) -> list[types.BotCommand]:
        return [command.get_bot_command() for command in self.commands]
