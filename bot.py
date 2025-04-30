import telebot

import constants


bot = telebot.TeleBot(token=constants.TOKEN)

subscribed_users = set()

@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[0]])
def start_command(user_message: telebot.types.Message):
    user_id = user_message.from_user.id
    subscribed_users.add(user_id)
    bot.reply_to(
        message=user_message,
        text=constants.BOT_MESSAGES["welcome_message"]
        )


@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[1]])
def help_command(user_message: telebot.types.Message):
    bot.reply_to(
        message=user_message,
        text=constants.BOT_MESSAGES["help_message"]
    )

if __name__ == "__main__":
    bot.polling(none_stop=True)
