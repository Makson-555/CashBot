import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .conf import bot
from .models import UserProfile, Start, MinimalDepozitQancha, OneDeposite, CallBack, Pul, Sharhlar, SharhlarImage, Litsenziya


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
        return HttpResponse('')
    return HttpResponse('Invalid request method')


@bot.message_handler(commands=['start'])
def start(message):
    start_obj = Start.objects.first()
    if start_obj:
        bot.send_message(message.chat.id, start_obj.text, reply_markup=create_reply_markup())


def create_reply_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    minimal_deposit_button = KeyboardButton('Minimal depozit qancha?')
    comments_button = KeyboardButton('Sharhlar')
    license_button = KeyboardButton('Litsenziya')
    markup.add(minimal_deposit_button, comments_button, license_button)
    return markup


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Minimal depozit qancha?':
        minimal_depozit_obj = MinimalDepozitQancha.objects.first()
        if minimal_depozit_obj:
            bot.send_message(message.chat.id, minimal_depozit_obj.text, reply_markup=deposit())
    elif message.text == '650.000 so\'m':
        one_deposite_obj = OneDeposite.objects.first()
        if one_deposite_obj:
            bot.send_message(message.chat.id, one_deposite_obj.text, reply_markup=one_deposit_options())
    elif message.text == '1.000.000 so\'m':
        one_deposite_obj = OneDeposite.objects.first()
        if one_deposite_obj:
            bot.send_message(message.chat.id, one_deposite_obj.text, reply_markup=one_deposit_options())
    elif message.text == '5.000.000 so\'m':
        one_deposite_obj = OneDeposite.objects.first()
        if one_deposite_obj:
            bot.send_message(message.chat.id, one_deposite_obj.text, reply_markup=one_deposit_options())
    elif message.text == 'Ha':
        callback_obj = CallBack.objects.first()
        if callback_obj:
            bot.send_message(message.chat.id, callback_obj.text)
    elif message.text == 'Yo\'q':
        callback_obj = CallBack.objects.first()
        if callback_obj:
            bot.send_message(message.chat.id, callback_obj.text)
    elif message.text == 'Ha, lekin keyinroq':
        callback_obj = CallBack.objects.first()
        if callback_obj:
            bot.send_message(message.chat.id, callback_obj.text)
    elif message.text == 'Pul yo\'q':
        pul_obj = Pul.objects.first()
        if pul_obj:
            bot.send_message(message.chat.id, pul_obj.text, reply_markup=pul_options())
    elif message.text == 'Men kerakli miqdorni topdim':
        callback_obj = CallBack.objects.first()
        if callback_obj:
            bot.send_message(message.chat.id, callback_obj.text)
    if message.text == 'Sharhlar':
        sharhlar_obj = Sharhlar.objects.first()
        if sharhlar_obj:
            sharhlar_images = SharhlarImage.objects.filter(sharhlar=sharhlar_obj)
            images_count = sharhlar_images.count()
            if images_count % 3 != 0:
                for i in range(0, images_count, 3):
                    row_images = sharhlar_images[i:i + 3]
                    photo_rows = []
                    for image in row_images:
                        photo_rows.append(image.image)
                    bot.send_media_group(message.chat.id,
                                         [telebot.types.InputMediaPhoto(media) for media in photo_rows])
            else:
                for i in range(0, images_count, 2):
                    row_images = sharhlar_images[i:i + 2]
                    photo_rows = [image.image for image in row_images]
                    bot.send_media_group(message.chat.id,
                                         [telebot.types.InputMediaPhoto(media) for media in photo_rows])
            bot.send_message(message.chat.id, sharhlar_obj.text)
    elif message.text == 'Litsenziya':
        litsenziya_obj = Litsenziya.objects.first()
        if litsenziya_obj:
            bot.send_photo(message.chat.id, litsenziya_obj.image)


def deposit():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    deposit_650_button = KeyboardButton('650.000 so\'m')
    deposit_1000_button = KeyboardButton('1.000.000 so\'m')
    deposit_5000_button = KeyboardButton('5.000.000 so\'m')
    no_money_button = KeyboardButton('Pul yo\'q')
    comments_button = KeyboardButton('Sharhlar')
    license_button = KeyboardButton('Litsenziya')
    markup.add(deposit_650_button, deposit_1000_button, deposit_5000_button, no_money_button, comments_button, license_button)
    return markup


def one_deposit_options():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    yes_button = KeyboardButton('Ha')
    no_button = KeyboardButton('Yo\'q')
    later_button = KeyboardButton('Ha, lekin keyinroq')
    markup.add(yes_button, no_button, later_button)
    return markup


def pul_options():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    need_amount_button = KeyboardButton('Men kerakli miqdorni topdim')
    markup.add(need_amount_button)
    return markup