from abc import ABC, abstractclassmethod
from telebot import TeleBot
from telebot import types
from logging import Logger


class BaseCommand(ABC):
    """BaseCommand enable you to write your commands and turn them on and off without removing the code
    - To enable the command run -> ``Command.register(commands,**kwargs)``
    """

    commands: list[str] = []
    description: str
    base_command: str

    def __init__(self, bot: TeleBot, logger: Logger) -> None:
        self.bot = bot
        self.logger = logger

    @abstractclassmethod
    def command(cls, message: types.Message) -> None:
        """Bot Command"""

    def register(self, **kwargs) -> None:
        """register the ``command`` function to the bot object"""

        @self.bot.message_handler(commands=self.commands, **kwargs)
        def handler(message):
            self.command(message)

        self.logger.info(f"{self.__class__.__name__} is installed")

    @classmethod
    def get_command_name(cls) -> str:
        """Return the command name which will be published, by default return the First one"""
        if len(cls.commands) == 0:
            raise NameError(
                "No Command Name Found Please add 'commands' to Your Command"
            )
        else:
            if cls.base_command:
                return cls.base_command
            return cls.commands[0]

    @classmethod
    def get_bot_command(cls) -> types.BotCommand:
        return types.BotCommand(cls.get_command_name(), cls.description)
