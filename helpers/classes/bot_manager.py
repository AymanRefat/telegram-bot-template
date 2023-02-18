from abc import ABC
import logging
import telebot
import os
from .feature import BaseCommand, BaseFeature


class TokenManager:
    __token: str
    token_env_name: str = "TOKEN"

    def get_token(self) -> None:
        """get the token from the env vars and set it"""
        self.__token = os.getenv(self.token_env_name)

        return self.__token


class BaseBotManager(ABC):
    """the Manager who will control the Bot Features"""

    token_manager: TokenManager = TokenManager()
    features: list[BaseFeature]
    commands: list[BaseCommand]
    bot: telebot.TeleBot

    def __init__(self, **kwargs) -> None:
        self.bot = telebot.TeleBot(self.token_manager.get_token(), **kwargs)
        self.logger = telebot.logger
        self.logger.setLevel(logging.INFO)

    def register_features(self) -> None:
        self.__register_commands()
        for feature in self.features:
            feature(self.bot, self.logger).register()

    def __register_commands(self) -> None:
        """Register all Written commands in the list"""
        for command in self.commands:
            command(self.bot, logger=self.logger).register()

    def get_bot_commands(self) -> list[BaseCommand]:
        commands = []
        for feature in self.features:
            commands += feature.get_bot_commands()
        for command in self.commands:
            commands.append(command.get_bot_command())
        return commands

    def set_bot_commands(self) -> None:
        self.bot.set_my_commands(self.get_bot_commands())
