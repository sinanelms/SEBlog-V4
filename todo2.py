import random
from datetime import datetime
from functools import wraps
from flask import Flask, flash, logging, redirect, render_template, request,session, url_for,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, PasswordField, StringField, TextAreaField, validators
from passlib.hash import sha256_crypt

from sqlalchemy import func,distinct

# Kullanıcı Giriş Decorator'ı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın.","danger")
            return redirect(url_for("login"))

    return decorated_function

# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "Lütfen Geçerli Bir Email Adresi Girin...")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Parola Doğrula")
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")

app = Flask(__name__,static_folder='static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key= "seblog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/WeLoo/Desktop/SEBlog-V2/yer.db' #C:/Users/WeLoo/Desktop/SEBlog-V2/yerr.db
db = SQLAlchemy(app)
#denme alanı

#anasayfa
@app.route("/")
def index():
    return render_template("site.html")

#haritalar
@app.route("/maps")
def about():
    return render_template("maps.html")

#iletişim
@app.route("/iletisim")
def iletisim():
    return render_template("call.html")

#resimler
@app.route("/resimler")
def resim():
    return render_template("resim.html")


# bölgeler
@app.route("/adli")
def adli():
    articles = yer.query.all()
    return render_template("adli.html",articles = articles)

if __name__ == "__main__":
    app.run(debug=True)
