import telebot
import schedule
import time
import threading

import constants


bot = telebot.TeleBot(token=constants.TOKEN)

subscribed_users = set()


@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[0]])
def start_command(user_message: telebot.types.Message):
    user_id = user_message.from_user.id
    subscribed_users.add(user_id)
    print(subscribed_users)
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


@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[2]])
def subscribe_command(user_message: telebot.types.Message):
    user_id = user_message.from_user.id
    print(subscribed_users)
    if user_id in subscribed_users:
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES["already_subscribed"]
        )
    else:
        subscribed_users.add(user_id)
        print(subscribed_users)
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES["user_subscribed"]
        )


@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[3]])
def unsubscribe_command(user_message: telebot.types.Message):
    user_id = user_message.from_user.id
    if user_id in subscribed_users:
        print(subscribed_users)
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES["user_unsubscribed"]
        )
    else:
        print(subscribed_users)
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES["not_subscribed"]
        )


@bot.message_handler(commands=[list(constants.BOT_COMMANDS.keys())[4]])
def status_command(user_message: telebot.types.Message):
    user_id = user_message.from_user.id
    if user_id in subscribed_users:
        print(subscribed_users)
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES["already_subscribed"]
        )
    else:
        bot.reply_to(
            message=user_message,
            text=constants.BOT_MESSAGES[""]
        )


def send_reminder():
    for user_id in subscribed_users:
        try:
            bot.send_message(
                chat_id=user_id,
                text=constants.BOT_MESSAGES["reminder"]
            )
        except Exception as e:
            print(f"Failed to send reminder to {user_id}: {e}")


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(60)


def setup_scheduler():
    days_map = {
        "Понедельник": "monday",
        "Вторник": "tuesday",
        "Среда": "wednesday",
        "Четверг": "thursday",
        "Пятница": "friday",
        "Суббота": "saturday",
        "Воскресенье": "sunday"
    }

    day_en = days_map.get(
        constants.CLASS_DAY.capitalize(),
        "THURSDAY"
    )

    getattr(schedule.every(), day_en).at(
        constants.REMINDER_TIME).do(send_reminder)

    scheduler_thread = threading.Thread(target=schedule_checker)
    scheduler_thread.daemon = True
    scheduler_thread.start()


if __name__ == "__main__":
    try:
        setup_scheduler()
        print(
            f"Bot started. Reminders scheduled for {constants.CLASS_DAY} at {constants.REMINDER_TIME}")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot crashed: {e}")
