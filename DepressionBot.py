import telebot
from telebot import types

bot = telebot.TeleBot("6521779402:AAH1WIw3EHsiHjCmKFNHdr-rbkn8HKG7bWI")
result = 0

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
        btn1_1 = types.KeyboardButton('Я не чувствую себя расстроенным, печальным')
        btn1_2 = types.KeyboardButton('Я расстроен')
        btn1_3 = types.KeyboardButton('Я все время расстроен и не могу от этого отключиться')
        btn1_4 = types.KeyboardButton('Я настолько расстроен и несчастлив, что не могу это выдержать')
        markup.add(btn1_1, btn1_2, btn1_3, btn1_4)
        bot.send_message(message.chat.id, "Вопрос 1", reply_markup = markup)
        bot.register_next_step_handler(message, question2)
    else:
        bot.send_message(message.chat.id, "Выберите команду")

def question2(message):
    global result
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn2_1 = types.KeyboardButton('Я не тревожусь о своем будущем')
    btn2_2 = types.KeyboardButton('Я чувствую, что озадачен будущим')
    btn2_3 = types.KeyboardButton('Я чувствую, что меня ничего не ждет в будущем')
    btn2_4 = types.KeyboardButton('Мое будущее безнадежно, и ничто не может измениться к лучшему')
    markup.add(btn2_1,btn2_2,btn2_3,btn2_4)
    bot.send_message(message.chat.id, "Вопрос 2", reply_markup=markup)
    if message.text == "Я не чувствую себя расстроенным, печальным":
        result += 0
    elif message.text == "Я расстроен":
        result += 1
    elif message.text == "Я все время расстроен и не могу от этого отключиться":
        result += 2
    elif message.text == "Я настолько расстроен и несчастлив, что не могу это выдержать":
        result += 3
    bot.register_next_step_handler(message, question3)

def question3(message):
    global result
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn3_1 = types.KeyboardButton('Я не чувствую себя неудачником')
    btn3_2 = types.KeyboardButton('Я чувствую, что терпел больше неудач, чем другие люди')
    btn3_3 = types.KeyboardButton('Когда я оглядываюсь на свою жизнь, я вижу в ней много неудач')
    btn3_4 = types.KeyboardButton('Я чувствую, что как личность я - полный неудачник')
    markup.add(btn3_1, btn3_2, btn3_3, btn3_4)
    bot.send_message(message.chat.id, "Вопрос 3", reply_markup=markup)
    if message.text == "Я не тревожусь о своем будущем":
        result += 0
    elif message.text == "Я чувствую, что озадачен будущим":
        result += 1
    elif message.text == "Я чувствую, что меня ничего не ждет в будущем":
        result += 2
    else:
        result += 3
    bot.register_next_step_handler(message, question4)

def question4(message):
    global result
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn4_1 = types.KeyboardButton('Я получаю столько же удовлетворения от жизни, как раньше')
    btn4_2 = types.KeyboardButton('Я не получаю столько же удовлетворения от жизни, как раньше')
    btn4_3 = types.KeyboardButton('Я больше не получаю удовлетворения ни от чего')
    btn4_4 = types.KeyboardButton('Я полностью не удовлетворен жизнью. и мне все надоело')
    markup.add(btn4_1, btn4_2, btn4_3, btn4_4)
    bot.send_message(message.chat.id, "Вопрос 4", reply_markup=markup)
    if message.text == "Я не чувствую себя неудачником":
        result += 0
    elif message.text == "Я чувствую, что терпел больше неудач, чем другие люди":
        result += 1
    elif message.text == "Когда я оглядываюсь на свою жизнь, я вижу в ней много неудач":
        result += 2
    else:
        result += 3
    bot.register_next_step_handler(message, question5)

def question5(message):
    global result
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn5_1 = types.KeyboardButton('Я не чувствую себя в чем-нибудь виноватым')
    btn5_2 = types.KeyboardButton('Достаточно часто я чувствую себя виноватым')
    btn5_3 = types.KeyboardButton('Большую часть времени я чувствую себя виноватым')
    btn5_4 = types.KeyboardButton('Я постоянно испытываю чувство вины')
    markup.add(btn5_1, btn5_2, btn5_3, btn5_4)
    bot.send_message(message.chat.id, "Вопрос 5", reply_markup=markup)
    if message.text == "Я получаю столько же удовлетворения от жизни, как раньше":
        result += 0
    elif message.text == "Я не получаю столько же удовлетворения от жизни, как раньше":
        result += 1
    elif message.text == "Я больше не получаю удовлетворения ни от чего":
        result += 2
    else:
        result += 3
    bot.register_next_step_handler(message, final_result)

def final_result(message):
    global result
    if message.text == "Я не чувствую себя в чем-нибудь виноватым":
        result += 0
    elif message.text == "Достаточно часто я чувствую себя виноватым":
        result += 1
    elif message.text == "Большую часть времени я чувствую себя виноватым":
        result += 2
    else:
        result += 3
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_res = types. KeyboardButton("Узнать результат")
    markup.add(btn_res)
    bot.send_message(message.chat.id, "Нажмите, чтобы узнать результат", reply_markup=markup)
    bot.register_next_step_handler(message, res)

def res(message):
    if message.text == "Узнать результат":
        global result
        bot.send_message(message.chat.id, f"Ваш результат {result} баллов. Этот результат является показателем нормы")
        photo = open('ulibka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        result = 0

bot.polling(none_stop=True)