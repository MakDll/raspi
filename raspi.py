import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
import MySQLdb

sta = "The device is "
tus = "off" #ultimo stato
#def usr: 111111111
def act(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1) #timer per simulare la pressione del pulsante
        GPIO.output(pin,GPIO.LOW)
        return


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   
def connectionDbWithMessage(msg):
        conn=MySQLdb.connect(host="HOST", user='USERNAME', passwd='PASSWORD', db='DATABASE') #da fixare con i parametri giusti

        cursor=conn.cursor()
        cursor.execute("codice_SQL") # Esegui la query con il parametro "msg"
        #row=cursor.fetchone() che ti frega se devi fare insert nn vedi il valore di ritorno
        #valore1=row[0]#

        cursor.close()
        conn.close()            
        return  
                
GPIO.setmode(GPIO.BOARD) # Selettore numeratore PIN raspberry
GPIO.setup(11, GPIO.OUT) # Selezione PIN di output

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'on': #comando di accensione
           connectionDbWithMessage("on")
           bot.sendMessage(chat_id, act(11))
           tus='on'
    elif command =='off': #spegnimento
           connectionDbWithMessage("on")
           bot.sendMessage(chat_id, act(11))
           tus='off'
    if command =='powstat': #stato
           connectionDbWithMessage("on")
           sta1= sta + tus
           bot.sendMessage(chat_id, sta1)

bot = telepot.Bot('lololololololol')
bot.message_loop(handle)
print 'Pronto!'

while 1:
   time.sleep(10)
