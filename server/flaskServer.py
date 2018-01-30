from flask import Flask, request, render_template
import MySQLdb
from redisworks import Root
import os
import sys
from twilioCli import sendMessage
from time import sleep
sys.path.append("../")
from logger import Logger
import threading
from twilio.rest import Client

logger = Logger()

def sendSMS(number, logger):
    try:
        #twilio here
        sendMessage(number)
        logger.debug("Sent sms "+ str(number))
    except Exception as e:
        logger.error("Error occured in redis check" + str(e))

def poolRedis(sendSMS, Root, os, logger):
    while True:

        root = Root()
        numbers = root.numbers
        if(numbers == None):
            continue
        for number in numbers:
            sendSMS(number, logger)
            #logic here
        os.system("redis-cli DEL root.numbers")
        sleep(2)


thr = threading.Thread(target=poolRedis, args=(sendSMS, Root, os, logger))
thr.start()

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="aviral")
cur = db.cursor()
app = Flask(__name__)

@app.route("/number", methods=['GET'])
def addNum():
    num = request.args.get("number")
    cur.execute("""UPDATE data SET phone = %s WHERE id = 1""" % (num))
    db.commit()
    return "done"

#917007087512
@app.route("/")
def index():
    return render_template("index.html")

app.run(debug = True)
