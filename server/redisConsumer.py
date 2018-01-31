from twilioCli import sendMessage
from time import sleep
from logger import Logger
import threading
from twilio.rest import Client
from redisworks import Root
import os

logger = Logger()

def sendSMS(number, logger):
    try:
        sendMessage(number)
        logger.debug("Sent sms "+ str(number))
    except Exception as e:
        logger.error("Error occured " + str(e))

def retry(number, logger, sendSMS):
    for i in range(5):
        try:
            logger.error("Retrying... #"+str(i))
            sendSMS(number, logger)
            break
        except:
            logger.error("Sending message failed.")
            continue

def poolRedis(sendSMS, Root, os, logger, retry):
    while True:
        root = Root()
        numbers = root.numbers
        if(numbers == None or numbers == []):
            continue
        for number in numbers:
            try:
                sendSMS(number, logger)
            except:
                logger.error("Sending message failed.")
                retry(number, logger, sendSMS)
        os.system("redis-cli DEL root.numbers")
        root.numbers = []
        sleep(2)

def startConsumer():
    thr = threading.Thread(target=poolRedis, args=(sendSMS, Root, os, logger, retry))
    thr.start()
