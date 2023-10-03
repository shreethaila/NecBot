from chatbot import english_bot,tamil_bot
from flask import Flask, render_template, request,session,logging,url_for,redirect,flash
from flask_recaptcha import ReCaptcha
import mysql.connector
from langdetect import detect
import os
import speech_recognition as sr
ffmpeg_path = 'C:\\ffmpeg\\bin'
import os
os.environ["PATH"] += os.pathsep + ffmpeg_path
from pydub import AudioSegment
from pydub.utils import mediainfo
from speech_recognition import AudioFile, Recognizer, UnknownValueError, RequestError
import tempfile
import io
AudioSegment.converter = ffmpeg_path

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.secret_key=os.urandom(24)
app.static_folder = 'static'


app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY = "6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
))

recaptcha=ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'

import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='thaila',
    db='register'
)
cur=conn.cursor()

def get_user_language(user_input):
    try:
        language = detect(user_input)
        return language
    except:
        # Default to English if language detection fails
        return 'en'

# Google recaptcha - site key : 6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L
# Google recaptcha - secret key : 6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cur.fetchall()
    if len(users)>0:
        session['id']=users[0][0]
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')

@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('name') 
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cur.fetchall()
    flash('You have successfully registered!')
    session['id']=myuser[0][0]
    return redirect('/index')

@app.route('/add_user',methods=['POST'])
def register():
    if recaptcha.verify():
        flash('New User Added Successfully')
        return redirect('/register')
    else:
        flash('Error Recaptcha') 
        return redirect('/register')


@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')


@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    print(request.args)
    print(request.args.get("msg"))

    userText = request.args.get('msg')
    user_language = get_user_language(userText)
    print(english_bot)
    
    if user_language == 'en':
        print("english")
        return str(english_bot.get_response(userText))
    elif user_language == 'ta':
        return str(tamil_bot.get_response(userText))
    else:
        print("inga pore")
        return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
