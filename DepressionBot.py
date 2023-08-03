import telebot
from telebot import types

bot = telebot.TeleBot("6521779402:AAH1WIw3EHsiHjCmKFNHdr-rbkn8HKG7bWI")
result = 0
i = 0

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
    },
    {
        "title": "Вопрос 6. Есть ли ожидание наказания?",
        "options": [
            {"text": "Я не считаю, что я заслуживаю наказания", "points": 0},
            {"text": "Я допускаю, что заслуживаю наказания", "points": 1},
            {"text": "Я все время жду наказания", "points": 2},
            {"text": "Я чувствую, что судьба наказывает меня", "points": 3}
        ]
    },
    {
        "title": "Вопрос 7. Есть ли чувство разочарования собой?",
        "options": [
            {"text": "Я вполне доволен собой", "points": 0},
            {"text": "Я недоволен собой", "points": 1},
            {"text": "Я противен себе", "points": 2},
            {"text": "Я ненавижу себя", "points": 3}
        ]
    },
    {
        "title": "Вопрос 8. Отношение к себе (критика, обвинение себя в неправильном поведении)",
        "options": [
            {"text": "Я не думаю, что я хуже других людей", "points": 0},
            {"text": "Я критикую себя за слабости и ошибки", "points": 1},
            {"text": "Я постоянно ругаю себя за разного рода проступки и ошибки", "points": 2},
            {"text": "Я ругаю себя за все плохое, что происходит вокруг", "points": 3}
        ]
    },
    {
        "title": "Вопрос 9. Преследуют ли суицидальные мысли?",
        "options": [
            {"text": "У меня не возникает мысли о самоубийстве", "points": 0},
            {"text": "У меня появляются мысли о том, чтобы покончить с собой, но я не сделаю этого", "points": 1},
            {"text": "Я хочу покончить с собой", "points": 2},
            {"text": "Я бы покончил с собой, если бы мне представилась возможность", "points": 3}
        ]
    },
    {
        "title": "Вопрос 10. Появилась ли плаксивость?",
        "options": [
            {"text": "Я плачу не чаще обычного", "points": 0},
            {"text": "Я плачу чаще обычного", "points": 1},
            {"text": "Я все время плачу", "points": 2},
            {"text": "Раньше я часто плакал, но теперь не могу заплакать, даже когда хочется плакать", "points": 3}
        ]
    },
    {
        "title": "Вопрос 11. Увеличилась ли раздражительность?",
        "options": [
            {"text": "Я испытываю раздражение не чаще обычного", "points": 0},
            {"text": "Я раздражаюсь чаще обычного", "points": 1},
            {"text": "Я испытываю постоянное чувство внутреннего недовольства и раздражения", "points": 2},
            {"text": "Мне глубоко безразлично то, что раньше вызывало раздражение", "points": 3}
        ]
    },
    {
        "title": "Вопрос 12. Не потерян ли интерес к жизни и людям?",
        "options": [
            {"text": "Я не утратил интереса к людям", "points": 0},
            {"text": "Люди интересуют меня меньше, чем прежде", "points": 1},
            {"text": "Я почти утратил интерес к людям", "points": 2},
            {"text": "Люди глубоко безразличны мне", "points": 3}
        ]
    },
    {
        "title": "Вопрос 13. Легко ли принимать решения?",
        "options": [
            {"text": "Мне не стало труднее принимать решения", "points": 0},
            {"text": "Теперь я чаще обычного медлю с принятием решения", "points": 1},
            {"text": "Я с огромным трудом принимаю решения", "points": 2},
            {"text": "Я не в состоянии принимать решения", "points": 3}
        ]
    },
    {
        "title": "Вопрос 14. Насколько изменилось восприятие своей внешности?",
        "options": [
            {"text": "Я не считаю, что выгляжу хуже обычного", "points": 0},
            {"text": "Меня беспокоит, что я выгляжу хуже обычного и кажусь старше своих лет", "points": 1},
            {"text": "Я чувствую, что с каждым днем выгляжу все хуже и хуже", "points": 2},
            {"text": "Я убежден, что выгляжу ужасно", "points": 3}
        ]
    },
    {
        "title": "Вопрос 15. Изменилась ли работоспособность?",
        "options": [
            {"text": "Мне работается так же, как прежде", "points": 0},
            {"text": "Теперь мне приходится заставлять себя приниматься за работу", "points": 1},
            {"text": "Я с трудом заставляю себя приниматься за работу", "points": 2},
            {"text": "Я не в состоянии работать", "points": 3}
        ]
    },
    {
        "title": "Вопрос 16. Нарушился ли сон?",
        "options": [
            {"text": "Я сплю не меньше и не хуже обычного", "points": 0},
            {"text": "Я сплю хуже обычного", "points": 1},
            {"text": "Я просыпаюсь на 1-2 часа раньше обычного и мне трудно снова заснуть", "points": 2},
            {"text": "Я просыпаюсь на несколько часов раньше обычного и уже не могу заснуть", "points": 3}
        ]
    },
    {
        "title": "Вопрос 17. Часто ли чувствуете себя усталым?",
        "options": [
            {"text": "Я устаю не больше обычного", "points": 0},
            {"text": "Я устаю быстрее, чем обычно", "points": 1},
            {"text": "Я устаю от любого занятия", "points": 2},
            {"text": "Я чувствую себя таким усталым, что не в состоянии чем-либо заниматься", "points": 3}
        ]
    },
    {
        "title": "Вопрос 18. Изменился ли аппетит?",
        "options": [
            {"text": "У меня нормальный аппетит", "points": 0},
            {"text": "Мой аппетит стал хуже", "points": 1},
            {"text": "У меня почти нет аппетита", "points": 2},
            {"text": "У меня совсем нет аппетита", "points": 3}
        ]
    },
    {
        "title": "Вопрос 19. Изменился ли вес тела?",
        "options": [
            {"text": "Мой вес остается почти неизменным", "points": 0},
            {"text": "За последнее время я похудел больше, чем на 2 кг", "points": 1},
            {"text": "За последнее время я похудел больше, чем на 4 кг", "points": 2},
            {"text": "За последнее время я похудел больше, чем на 6 кг", "points": 3}
        ]
    },
    {
        "title": "Вопрос 20. Степень беспокойства о своем физическом здоровье",
        "options": [
            {"text": "Мое здоровье не дает мне особых поводов для беспокойства", "points": 0},
            {"text": "Меня беспокоят физические симптомы (боли, расстройства желудка, запоры и др.)", "points": 1},
            {"text": "Я очень обеспокоен имеющимися симптомами, и мне трудно думать о другом", "points": 2},
            {"text": "Я не могу думать ни о чем, кроме беспокоящих меня симптомов", "points": 3}
        ]
    },
    {
        "title": "Вопрос 21. Изменилось ли отношение к сексуальной жизни?",
        "options": [
            {"text": "Я сохраняю обычный интерес к сексу", "points": 0},
            {"text": "Сейчас секс интересует меня меньше, чем обычно", "points": 1},
            {"text": "Мой интерес к сексу заметно снизился", "points": 2},
            {"text": "Я полностью утратил интерес к сексу", "points": 3}
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
    global i
    i += 1
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
    
    if i == len(questions_list)-1:
        bot.register_next_step_handler(message, final_result)
    else:
        bot.register_next_step_handler(message, questions)
    

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
        bot.send_photo(message.chat.id, open('bot\хорошее_настроение.jpg', 'rb'))
    elif result >= 14 and result <= 19:
        bot.send_message(message.chat.id, "Это является показателем легкого депрессивного состояния")
        bot.send_photo(message.chat.id, open('bot\плохое_настроение.jpeg', 'rb'))
    elif result >= 20 and result <= 28:
        bot.send_message(message.chat.id, "Это является показателем умеренного депрессивного состояния")
        bot.send_photo(message.chat.id, open('bot\умеренная.jpg', 'rb'))
    else:
        bot.send_message(message.chat.id, "Это является показателем тяжелой депрессии")
        bot.send_photo(message.chat.id, open('bot\тяжелая.jpg', 'rb'))
    bot.send_message(message.chat.id, "Онлайн-тест не может быть использован для самостоятельной постановки диагноза. В случае любых сомнений обращайтесь к квалифицированным специалистам")
    bot.send_message(message.chat.id, "Чтобы начать заново введите /start")
    result = 0

bot.polling(none_stop=True)