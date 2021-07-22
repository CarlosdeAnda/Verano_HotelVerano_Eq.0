from flask import Flask
import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)

@app.route('/home')
def ventanaHome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()