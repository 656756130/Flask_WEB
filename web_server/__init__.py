import os
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#153
app = Flask(__name__)  #初始化

#secrets库
app.config["SECRET_KEY"]="'42f59bb7395724b434706d673659201d'"

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'  #相同路径下建立数据库

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_message_category = 'danger'
login_manager.login_message = u"这位小伙伴，请登录后查看个人界面呀"
login_manager.login_view='login'


app.config['MAIL_SERVER']='smtp.163.com'
#25为非安全协议  SSL：465 994
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "aazz13569235274@163.com"#os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = "IBYSKLUONIYFWQIC"#os.environ.get('EMAIL_PASS')
#app.config['EMAIL_HOST_PASSWORD'] ='IBYSKLUONIYFWQIC'

mail = Mail(app)

from web_server import routes




#关于加密补充：1）明文储存---不需要破解
#             2）对称加密---需要key来破解（对key要绝对保密）
#             3）Hash算法---暴力破解（通过彩虹表或者碰撞，单项，或者salt）
#			  4）BCrypt---挺难


#BCrypt:1)saltRounds:正数 相当于次数
#      2)myPassword:明文密码
#      3)salt:128bit，22字符
#      4)myHash:循环加salt进行hash的结果



