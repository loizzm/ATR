import json
from flask import Flask, jsonify, request
import mariadb
from datetime import datetime
from decimal import *
import os

app = Flask(__name__)

def init_db():
    config = {
        'host': os.environ.get('HOST'),
        'port' : int(os.environ.get('PORT')),
        'user' : os.environ.get('USER'),
        'password': os.environ.get('PASSWORD'),
        'database' : os.environ.get('DATABASE')
    }
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Canis")
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    canis=[]
    for result in rv:
        canis.append(dict(zip(row_headers,result)))
    return canis

def convert_date(date):
    date_object = datetime.strptime(date, "%d/%m/%Y")
    day_of_week = date_object.weekday()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[day_of_week]

def calculate_price(week_day, n_big, n_small, dic):
    getcontext().prec=12
    if(week_day ==  "Saturday" or week_day ==  "Sunday"):
        small_price = dic['small_dog_we']
        big_price = dic['big_dog_we']
        total_price = (small_price*Decimal(n_small))+(big_price*Decimal(n_big))
        return round(total_price,2)
    small_price = dic['small_dog_wd']
    big_price = dic['big_dog_wd']
    total_price = (small_price*Decimal(n_small))+(big_price*Decimal(n_big))
    return round(total_price,2)
    

@app.route('/canil', methods=['GET'])
def get_melhor_canil():
    canis=init_db()
    big = request.args.get('big')
    small = request.args.get('small')
    date = request.args.get('date')
    week_day = convert_date(date)
    best_price = Decimal(0.00)
    canil_name = str()
    for canil in canis:
        price=calculate_price(week_day,big,small,canil)
        if(best_price == 0.00):
            best_price=price
            canil_name = canil['name']
        elif(price < best_price):
            best_price = price
            canil_name = canil['name']
    
    return jsonify({'melhor canil': canil_name, 'preco': best_price}), 200

if __name__ == '__main__':
    app.run(host="flaskapp", port=5000)