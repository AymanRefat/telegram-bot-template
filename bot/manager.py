from dotenv import load_dotenv
from helpers import BaseBotManager
from .commands import StartCommand

load_dotenv()


class BotManager(BaseBotManager):
    commands = [StartCommand]
    features = []

    def start_bot(self) -> None:
        self.register_features()
        self.set_bot_commands()
        self.bot.infinity_polling()


manager = BotManager()
