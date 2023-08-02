import telebot
from telebot import types

bot = telebot.TeleBot("6521779402:AAH1WIw3EHsiHjCmKFNHdr-rbkn8HKG7bWI")
result = 0

questions_list = [
    {
        "title": "Вопрос 1. Как вы себя чувствуете (в настоящее время, ранее)",
        "options": [
            {"text": "Я не чувствую себя расстроенным, печальным", "points": 0},
            {"text": "Я расстроен", "points": 1},
            {"text": "Я все время расстроен и не могу от этого отключиться", "points": 2},
            {"text": "Я настолько расстроен и несчастлив, что не могу это выдержать", "points": 3}
        ]
    },
    {
        "title": "Вопрос 2. Есть ли тревожность, степень тревожности (в настоящее время, ранее)",
        "options": [
            {"text": "Я не тревожусь о своем будущем", "points": 0},
            {"text": "Я чувствую, что озадачен будущим", "points": 1},
            {"text": "Я чувствую, что меня ничего не ждет в будущем", "points": 2},
            {"text": "Мое будущее безнадежно, и ничто не может измениться к лучшему", "points": 3}
        ]
    },
    {
        "title": "Вопрос 3. Чувствуете ли вы себя неудачником?",
        "options": [
            {"text": "Я не чувствую себя неудачником", "points": 0},
            {"text": "Я чувствую, что терпел больше неудач, чем другие люди", "points": 1},
            {"text": "Когда я оглядываюсь на свою жизнь, я вижу в ней много неудач", "points": 2},
            {"text": "Я чувствую, что как личность я - полный неудачник", "points": 3}
        ]
    },
    {"title": "Вопрос 4. Степень удовлетворения жизнью (в настоящее время и ранее)",
        "options": [
            {"text": "Я получаю столько же удовлетворения от жизни, как раньше", "points": 0},
            {"text": "Я не получаю столько же удовлетворения от жизни, как раньше", "points": 1},
            {"text": "Я больше не получаю удовлетворения ни от чего", "points": 2},
            {"text": "Я полностью не удовлетворен жизнью. и мне все надоело", "points": 3}
        ]
    },
    {
        "title": "Вопрос 5. Есть ли чувство вины?",
        "options": [
            {"text": "Я не чувствую себя в чем-нибудь виноватым", "points": 0},
            {"text": "Достаточно часто я чувствую себя виноватым", "points": 1},
            {"text": "Большую часть времени я чувствую себя виноватым", "points": 2},
            {"text": "Я постоянно испытываю чувство вины", "points": 3}
        ]
    }
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Информация")
    btn2 = types.KeyboardButton("Начать тест")
    markup.add(btn1, btn2)
    name = message.from_user.first_name
    mesg = bot.send_message(message.chat.id, f"{name}, приветствую Вас на странице прохождения теста депрессии Бека", reply_markup=markup)
    bot.register_next_step_handler(mesg, get_messages)

@bot.message_handler(commands=['text'])
def get_messages(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, 'В этом опроснике содержатся группы утверждений. Внимательно прочитайте каждую группу утверждений. Затем определите в каждой группе одно утверждение, которое лучше всего соответствует тому, как вы себя чувствовали на этой неделе и сегодня. Онлайн-тест не может быть использован для самостоятельной постановки диагноза! В случае любых сомнений обращайтесь к квалифицированным специалистам.', parse_mode='Markdown')
    elif message.text == 'Начать тест':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1_1 = types.KeyboardButton(questions_list[0]["options"][0]["text"])
        btn1_2 = types.KeyboardButton(questions_list[0]["options"][1]["text"])
        btn1_3 = types.KeyboardButton(questions_list[0]["options"][2]["text"])
        btn1_4 = types.KeyboardButton(questions_list[0]["options"][3]["text"])
        markup.add(btn1_1, btn1_2, btn1_3, btn1_4)
        bot.send_message(message.chat.id, questions_list[0]["title"], reply_markup = markup)
        bot.register_next_step_handler(message, questions)
    else:
        bot.send_message(message.chat.id, "Выберите команду")

def questions(message):
    global result
    for i in range(1, len(questions_list)):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn2_1 = types.KeyboardButton(questions_list[i]["options"][0]["text"])
        btn2_2 = types.KeyboardButton(questions_list[i]["options"][1]["text"])
        btn2_3 = types.KeyboardButton(questions_list[i]["options"][2]["text"])
        btn2_4 = types.KeyboardButton(questions_list[i]["options"][3]["text"])
        markup.add(btn2_1,btn2_2,btn2_3,btn2_4)
        bot.send_message(message.chat.id, questions_list[i]["title"], reply_markup=markup)
        if message.text == questions_list[i-1]["options"][0]["text"]:
            result += questions_list[i-1]["options"][0]["points"]
        elif message.text == questions_list[i-1]["options"][1]["text"]:
            result += questions_list[i-1]["options"][1]["points"]
        elif message.text == questions_list[i-1]["options"][2]["text"]:
            result += questions_list[i-1]["options"][2]["points"]
        elif message.text == questions_list[i-1]["options"][3]["text"]:
            result += questions_list[i-1]["options"][3]["points"]
        ##bot.register_next_step_handler(message, questions)
    bot.register_next_step_handler(message, final_result)

def final_result(message):
    global result
    if message.text == questions_list[len(questions_list)-1]["options"][0]["text"]:
        result += 0
    elif message.text == questions_list[len(questions_list)-1]["options"][1]["text"]:
        result += 1
    elif message.text == questions_list[len(questions_list)-1]["options"][2]["text"]:
        result += 2
    else:
        result += 3
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_res = types. KeyboardButton("Узнать результат")
    markup.add(btn_res)
    bot.send_message(message.chat.id, "Нажмите, чтобы узнать результат", reply_markup=markup)
    bot.register_next_step_handler(message, res)

def res(message):
    global result
    if result == 1 or (result > 20 and result % 10 == 1):
        bot.send_message(message.chat.id, f"Ваш результат {result} балл")
    elif result == 2 or result == 3 or result == 4 or (result > 20 and (result % 10 == 2 or result % 10 == 3 or result % 10 == 4)): 
        bot.send_message(message.chat.id, f"Ваш результат {result} балла")
    else:
        bot.send_message(message.chat.id, f"Ваш результат {result} баллов")

    if result <= 13:
        bot.send_message(message.chat.id, "Это является показателем нормы")
        photo = open('ulibka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif result >= 14 and result <= 19:
        bot.send_message(message.chat.id, "Это является показателем легкого депрессивного состояния")
        photo = open('', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif result >= 20 and result <= 28:
        bot.send_message(message.chat.id, "Это является показателем умеренного депрессивного состояния")
        photo = open('', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Это является показателем тяжелой депрессии")
        photo = open('', 'rb')
        bot.send_photo(message.chat.id, photo)
    ##bot.send_message(message.chat.id, "Онлайн-тест не может быть использован для самостоятельной постановки диагноза. В случае любых сомнений обращайтесь к квалифицированным специалистам")
    ##bot.send_message(message.chat.id, "Чтобы начать заново введите "/start"")
    result = 0

bot.polling(none_stop=True)