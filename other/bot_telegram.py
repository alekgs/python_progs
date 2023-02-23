import random
from datetime import date
import telebot

# AleXaS_bot token
token = "5505968935:AAH7m0DCsa9ND2bipgo_vsrEafrVNtL8LFE"
bot = telebot.TeleBot(token)

HELP = """
/help   - вывести список доступных команд
/add    - добавить задачу в список 
/show [dd.mm.yyyy] - вывод списка задач.\nЕсли дата не указана, то выводит все задачи на текущую дату.
Можно задать несколько дат, разделённых пробелом
/random - добавить случайную задачу на текущую дату
/exit   - завершить работу"""

tasks = {}


# Функция для добавления задачи на определённую дату
def add_todo(dat, task):
    if dat in tasks:
        tasks[dat].append(task)
    else:
        tasks[dat] = []
        tasks[dat].append(task)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    split_cmd = message.text.split(maxsplit=2)
    dat = split_cmd[1]
    task = split_cmd[2]
    if len(task) <= 3:
        text = 'Название задачи должно быть больше 3 символов !\nОперация ввода отклонена.'
    else:
        text = 'Задача добавлена'
        add_todo(dat, task)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
    random_tasks = ['Изучить Python',
                    'Сходить в магазин',
                    'Вынести мусор',
                    'Подстричься',
                    'Покормить кота',
                    'Помыть машину',
                    'Сходить на тренировку',
                    'Сходить в сауну']

    today = date.today().strftime("%d.%m.%Y")
    task = random.choice(random_tasks)
    add_todo(today, task)
    text = 'Задача добавлена'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show'])
def show(message):
    # убираем /show из переданной строки
    date_string = message.text.removeprefix('/show')

    # Если дата не введена, то выводим на текущую дату
    # Введена команда /show без параметров
    msg = ''
    if len(date_string) == 0:
        dat = date.today().strftime("%d.%m.%Y")
        if dat in tasks:
            msg = msg + 'Список задач на <b>' + dat + '</b>\n\n'
            for task in tasks[dat]:
                msg = msg + '[ ] ' + task + '\n'
        else:
            msg = 'Задач на ' + dat + ' нет\n'
        bot.send_message(message.chat.id, msg, parse_mode='html')
    else:
        split_date = date_string.split()
        for dt in split_date:
            msg = ''
            # Вывод задач
            if dt in tasks:
                msg = msg + 'Список задач на ' + dt + '\n'
                for task in tasks[dt]:
                    msg = msg + '[ ] ' + task + '\n\n'
            else:
                msg = 'Задач на ' + dt + ' нет\n'
            bot.send_message(message.chat.id, msg)
            # msg = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.chat.username
    bot.send_message(message.chat.id, 'Привет, ' + name + '!')
    bot.send_message(message.chat.id, HELP)


# Постоянно обращается к серверам Телеграм
bot.polling(none_stop=True)

# @bot.message_handler(content_types=["text"])
# def echo(message):
#     # text = message.text
#     # print(message.chat.id)
#     name = message.chat.username
#     print(name, ':', message.text)
#     if 'alekgs' in name:
#         bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
#         # print(bot.user.username, ':', 'Ба! Знакомые все лица!')


# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Кнопка")
#     markup.add(item1)

# bot.infinity_polling()

# run = True
#
# while run:
#     command = input("Введите команду: ")
#
#     if command == "show":
#         date = input("Введите дату для отображения списка задач: ")
#         if date in tasks:
#             for task in tasks[date]:
#                 print(date, "-", task)
#         else:
#             print('Такой даты нет')
#
#     elif command == "exit" or command == "stop":
#         break
#
#     else:
#         print("Неизвестная команда")
#         break
#
# print("Завершение работы")
