from flask import Flask, request, render_template
import MySQLdb
from redisConsumer import startConsumer
db = MySQLdb.connect(host="localhost", user="root", passwd="indicadls02", db="aviral")
cur = db.cursor()
app = Flask(__name__)

startConsumer()

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
