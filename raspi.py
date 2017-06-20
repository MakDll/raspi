import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

sta = "The device is "
tus = "off" #ultimo stato
#def usr: 111111111
def act(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1) #timer per simulare la pressione del pulsante
        GPIO.output(pin,GPIO.LOW)
        return


GPIO.setmode(GPIO.BOARD) # Selettore numeratore PIN raspberry
GPIO.setup(11, GPIO.OUT) # Selezione PIN di output

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'on': #comando di accensione
       bot.sendMessage(chat_id, act(11))
       tus='on'
    elif command =='off': #spegnimento
       bot.sendMessage(chat_id, act(11))
       tus='off'
    if command =='powstat': #stato
       sta1= sta + tus
       bot.sendMessage(chat_id, sta1)

bot = telepot.Bot('lololololololol')
bot.message_loop(handle)
print 'Pronto!'

while 1:
   time.sleep(10)
