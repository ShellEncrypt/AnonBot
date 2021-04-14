import telebot
import pickle
import tkn

def load(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

bot = telebot.TeleBot(tkn.token)

all_chats = load("filename.txt") or {1083482390}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Напиши сообщение, и все пользователи его увидят')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    all_chats.add(message.chat.id)
    with open("filename.txt", "wb") as f:
        pickle.dump(all_chats, f)
    with open("filename.txt", "rb") as f:
        ddd = pickle.load(f)
        print(ddd)
        for id in ddd:
            bot.send_message(id, message.text)

bot.polling()