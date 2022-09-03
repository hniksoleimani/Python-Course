import telebot
import random
import numpy as np
import qrcode
from khayyam import JalaliDatetime
from gtts import gTTS
mybot = telebot.TeleBot("5788490153:AAFQQxgTFBLvCFSwTE9JP6pLDT1p0NhKUR0")



user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

@mybot.message_handler(commands=['start'])
def send_welcome(message):
    mybot.reply_to(message,"Hello, welcome to my bot,\n The list of available commands are the following: \n /start \n /game \n /age \n /voice \n /max  \n /argmax \n /qrcode")


 
game_markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
game_button = telebot.types.KeyboardButton('new game') 
game_markup.add(game_button)
numbr = random.randint(1,10)
print(numbr)
# @mybot.message_handler(func=lambda m: True)
@mybot.message_handler(commands=['game'])
def game(message_):
    mybot.reply_to(message_,"Enter a number.")
    mybot.register_next_step_handler(message_,guess)
@mybot.message_handler(func=lambda m: True) 
def guess(message):
    print(message.text)
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        if int(message.text) == numbr:
            mybot.reply_to(message, 'you win!', reply_markup=game_markup)
            mybot.register_next_step_handler(message,game)
            numbr = random.randint(1,10)
        elif int(message.text) > numbr:  
            mybot.reply_to(message, "a little lower.")
        elif int(message.text) < numbr:
            mybot.reply_to(message, "a little higher.")

        else:    
            mybot.send_message(message.chat.id, 'I dont understand.') 
    except:
        mybot.reply_to(message, "Not a number.")




@mybot.message_handler(commands=['age'])
def age(message_):
    mybot.reply_to(message_, 'Enter your birthdate in hijri[1364/12/1]:')
    mybot.register_next_step_handler(message_,age2)
    print(JalaliDatetime.now())
def age2(message):
    print(message.text)
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        age = int(JalaliDatetime.now().year)-int(message.text[0:4])
        mybot.reply_to(message, f'Your age is:{age} years old')

    except:
        mybot.reply_to(message, "Wrong format")

@mybot.message_handler(commands=['voice'])
def text2speech(message_):
    mybot.reply_to(message_, 'Enter a sentence in english:')
    mybot.register_next_step_handler(message_,voice)
def voice(message):
    print(message.text)
    language = 'en'
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        input_text = str(message.text)
        rec = gTTS(text=input_text, lang=language, slow=False)
        rec.save('./Voice.mp3')
        mybot.reply_to(message, 'Recording complete.')
        record = open('./Voice.mp3', 'rb')
        mybot.send_audio(message.chat.id, record)
    except:
        mybot.reply_to(message, "Wrong format")

@mybot.message_handler(commands=['max'])
def max(message_):
    mybot.reply_to(message_, 'Enter some numbers[x,y,z,...]:')
    mybot.register_next_step_handler(message_,max2)
def max2(message):
    print(message.text)
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        string = message.text
        array = string.split(',')
        arr = []
        for i in range(len(array)):
            arr.append(int(array[i]))
        indice = np.where(arr==np.amax(arr))
        ind = str(indice).split('[')
        ind2 = str(ind[1]).split(']')
        ind3 = int(ind2[0])
        mybot.reply_to(message, f'Highest value is:{np.max(arr)} \n and index number is {ind3+1}')

    except:
        mybot.reply_to(message, "Wrong format")


# img = qrcode.make(input_text)
       
@mybot.message_handler(commands=['qrcode'])

def qrcode1(message_):
    mybot.reply_to(message_, 'Type a sentence:')
    mybot.register_next_step_handler(message_,qrcode2)
def qrcode2(message):
    
    print(message.text)
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        input_text = str(message.text)
        img = qrcode.make(input_text)
        img.save('./qrcode.png')
        mybot.reply_to(message, 'QRcode is complete')
        photo = open('qrcode.png', 'rb')
        mybot.send_photo(message.chat.id, photo)

    except:
        mybot.reply_to(message, "Wrong format")


       
@mybot.message_handler(commands=['help'])
def my_function_1(message):
    mybot.reply_to(message,"Hello, \n The list of available commands are the following: \n /start \n /game \n /age \n /voice \n /max  \n /argmax \n /qrcode")



       
mybot.polling()


