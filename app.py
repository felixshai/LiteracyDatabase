from flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///literacy_practices_db'
db = SQLAlchemy(app)

class bopomofo(db.Model):
    qid      = db.Column(db.Integer, primary_key=True)
    quiz     = db.Column(db.String(20))
    sample   = db.Column(db.String(20))
    options  = db.Column(db.String(100))
    solution = db.Column(db.String(20))

class point(db.Model):
    pid        = db.Column(db.Integer, primary_key=True)
    qtable     = db.Column(db.String(50))
    qid        = db.Column(db.Integer, nullable=False)
    point      = db.Column(db.Integer, nullable=False)
    ip         = db.Column(db.String(20))
    time_stamp = db.Column(db.DateTime,default=datetime.now)

class score(db.Model):
    sid        = db.Column(db.Integer, primary_key=True)
    qtable     = db.Column(db.String(50))
    qid        = db.Column(db.Integer, nullable=False)
    score      = db.Column(db.Integer, nullable=False)
    solution   = db.Column(db.String(20))
    ip         = db.Column(db.String(20))
    time_stamp = db.Column(db.DateTime,default=datetime.now)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bopomofo/')
def bopomofo_random_pick():
    id = random.choice([1,2,3,4,5,6,7,8,9,10])
    return redirect('/bopomofo/'+str(id))
    
@app.route('/bopomofo/<int:id>')
def bopomofo_select(id):
    quiz = db.engine.execute("SELECT * FROM bopomofo WHERE qid = " + str(id))
    return jsonify({'result': [dict(row) for row in quiz]})

if __name__ == "__main__":
    app.run()
