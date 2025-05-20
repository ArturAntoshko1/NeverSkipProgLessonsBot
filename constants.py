from os import getenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv("TOKEN")

CLASS_DAY = "Четверг"
CLASS_TIME = "19:15"
REMINDER_TIME = "18:15"

BOT_COMMANDS = {
    "start": "Включить бота🐧",
    "help": "Вывести это сообщение🎂",
    "subscribe": "Подписаться на уведомления о занятиях🍇",
    "unsubscribe": "Отписаться от уведомлений🤓",
    "status": "Проверить, подписаны ли вы на уведомления🥥",
}

BOT_MESSAGES = {
    "welcome_message":
    f"Привет! Я буду напоминать тебе про занятия по программированию каждый {CLASS_DAY} в {CLASS_TIME}. Ты будешь получать уведомление в {REMINDER_TIME}",
    "help_message":
    f"Я бот-напоминалка для занятий по программированию",
    "already_subscribed":
    f"Вы подписаны на уведомления о занятиях! уведомления будут приходить каждый {CLASS_DAY} в {REMINDER_TIME}🐱‍👤",
    "user_subscribed":
    f"Вы успешно подписались на уведомления о занятиях! Вы будете получать напоминания каждый {CLASS_DAY} в {REMINDER_TIME}.🐧",
    "not_subscribed":
    f"Вы не подписаны на уведомления! Что бы подписаться, нажмите /subscribe",
    "user_unsubscribed":
    f"Вы отписались от уведомлений!🏹"
    }
