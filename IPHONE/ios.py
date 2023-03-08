import locale
from datetime import datetime
import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot import types


def IPHONE():
    locale.setlocale(locale.LC_ALL, "")


    token="6158082223:AAGtiE0RhfkH8GWjRNXcJiT4-YPx7-yxHAc"
    bot=telebot.TeleBot(token)


    img = Image.open('IOS.jpg')
    img = img.copy()
    text_position = (571, 406.5)
    draw0 = ImageDraw.Draw(img)
    #x, y, w, h
    draw0.rectangle((570, 400, 650, 500), fill="#ffffff")
    text_color1 = (145, 145, 147)
    text_color = (41, 41, 43)
    time = datetime.now().strftime("%H:%M")
    text = str(time)
    fontsize = 23
    font = ImageFont.truetype('sf.ttf', fontsize)
    img_draw = ImageDraw.Draw(img)
    #x, y, w, h
    img_draw.rectangle((83, 850, 385, 650), fill="#E9E9EB")
    draw = ImageDraw.Draw(img)

    draw.text(
        text_position,
        text,
        text_color1,
        font,
        )

    text_position2 = (83, 652)
    fontsize2 = 37
    text0 = "ONAY! ALA"
    font2 = ImageFont.truetype('sf.ttf', fontsize2)
    qmg = ImageDraw.Draw(img)
    qmg.text(
        text_position2,
        text0,
        text_color,
        font2
    )

    text_position6 = (83, 700)
    fontsize6 = 37
    timee = datetime.now().strftime("%d/%m %H:%M")
    text3 = "AT " + timee
    draw6 = ImageDraw.Draw(img)
    font3 = ImageFont.truetype('sf.ttf', fontsize6)
    ymg = ImageDraw.Draw(img)
    ymg.text(
        text_position6,
        text3,
        text_color,
        font3
    )

    text_position4 = (76, 40)
    time3 = datetime.now().strftime("%H:%M")
    text3 = str(time3)
    fontsize4 = 45
    font4 = ImageFont.truetype('sf.ttf', fontsize4)
    img_draw = ImageDraw.Draw(img)
    #x, y, w, h
    img_draw.rectangle((200, 82, 70, 42), fill="#f7f7f7")
    draw4 = ImageDraw.Draw(img)
    draw4.text(
        text_position4,
        text3,
        text_color,
        font4,
        )


    @bot.message_handler(content_types=['text', 'photo'],)
    def start(message):
      bot.send_message(message.chat.id, "Введите код:" )
      bot.register_next_step_handler(message, bus)


    def bus(message):
      global kods
      fontsize1 = 36
      text_color6 = (225, 225, 225)
      text_position1 = (857, 485)
      kods = message.text
      draw1 = ImageDraw.Draw(img)
      #x, y, w, h
      draw1.rectangle((859, 485, 1005, 521), fill="#34C85A")
      font1 = ImageFont.truetype('sf.ttf', fontsize1)
      amg = ImageDraw.Draw(img)
      amg.text(
          text_position1,
          kods,
          text_color6,
          font1
          )

      bot.send_message(message.chat.id, "Введите номер автобуса:")
      bot.register_next_step_handler(message, kod)

    def kod(message):
      busik = message.text

      text_position3 = (83, 746)
      fontsize3 = 37
      font3 = ImageFont.truetype('sf.ttf', fontsize3)


      num = ImageDraw.Draw(img)
      num.text(
          text_position3,
          busik+", #3023,80₸" ,
          text_color,
          font3
      )
      img.save('Iphone.jpg')
      photo = "Iphone.jpg"
      bot.send_photo(message.chat.id, open(photo, 'rb'))




    print("START")
    bot.infinity_polling()

IPHONE()
