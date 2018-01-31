import MySQLdb
import sys, os
from redisworks import Root
import datetime
from logger import Logger
logger = Logger()
try:
    now = datetime.datetime.now()
    if now.hour > 23 or now.hour < 7:
        raise ValueError("He is Sleeping!")
    root = Root()
    db = MySQLdb.connect(host="localhost", user="root", passwd="indicadls02", db="aviral")
    cur = db.cursor()
    cur.execute("SELECT name, phone FROM data limit 1")
    data = cur.fetchone()
    name  = data[0]
    phone = data[1]
    numbers = root.numbers
    if(numbers == None):
        numbers = []
    numbers.append(phone)
    root.numbers = numbers
    logger.access("Cron: Pushed to redis " + str(phone))
except Exception as e:
    logger.error("Cron: an error occured "+ str(e))
