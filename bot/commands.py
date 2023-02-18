from telebot import types
import os
from helpers.classes.command import BaseCommand



class StartCommand(BaseCommand):
    commands = ["start", "help"]
    base_command = "start"
    description = "Start the bot"

    def command(self, message: types.Message) -> None:
        self.bot.send_message(
            chat_id=message.chat.id,
            text=self.get_start_message(message.from_user.first_name),
        )

    def get_start_message(self, name) -> str:
        """Generate the Welcome text to the user"""
        start_text = f"""Hi {name} , I am your AI assistant🤖 and am here for Helping you message me whenever you need 😉! ,There are some things I can help you with."""
        return start_text


