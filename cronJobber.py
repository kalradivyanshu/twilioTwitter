import MySQLdb
import sys, os
from redisworks import Root


try:
    root = Root()
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="aviral")
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
    print("Pushed to redis " + str(phone))
except Exception as e:
    print("an error occured"+ str(e))
