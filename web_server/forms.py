from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed   #上传图片或者文件
from flask_login import current_user
from wtforms import StringField ,PasswordField ,SubmitField ,BooleanField ,TextAreaField
#校验
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from web_server.models import User

class RegistrationForm(FlaskForm):
	username = StringField("用户名/昵称",validators = [DataRequired(message="请填入用户名"),Length(min=2,max=25,message="用户名在2-25长度范围内")])
	email = StringField("邮箱",validators = [DataRequired(message="请填入邮箱"),Email(message="邮箱格式错误")])
	password = PasswordField("密码",validators = [DataRequired(message="请填入密码")])
	confirm_password = PasswordField("确认密码",validators = [DataRequired(message="请再次填入密码"),EqualTo("password",message="两次密码不一致")])
	submit = SubmitField("注册")

	def validate_username(self,username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError("用户名已经注册，请更换用户名注册")
	def validate_email(self,email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError("邮箱已经注册，请更换伊妹儿注册")

class UpdateAccountForm(FlaskForm):
	username = StringField("用户名/昵称",validators = [DataRequired(message="请填入用户名"),Length(min=2,max=25,message="用户名在2-25长度范围内")])
	email = StringField("邮箱",validators = [DataRequired(message="请填入邮箱"),Email(message="邮箱格式错误")])
	submit = SubmitField("更新个人信息")
	picture = FileField("点我上传头像",validators = [FileAllowed(["jpg","png"],message="当前仅支持jpg，png格式哦")])

	def validate_username(self,username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError("用户名已经注册，请更换用户名注册")
	def validate_email(self,email):
		if email.data != current_user.email:
			user = User.query.filter_by(email = email.data).first()
			if user:
				raise ValidationError("邮箱已经注册，请更换伊妹儿注册")


class LoginForm(FlaskForm):
	email = StringField("邮箱",validators = [DataRequired(),Email(message="邮箱格式不正确")])
	password = PasswordField("密码",validators = [DataRequired()])
	remember = BooleanField("记住密码")
	submit = SubmitField("登录")

#OWASP 网络攻防
#XSS  DDOS Attack Definitions


class PostForm(FlaskForm):
	title = StringField("文章标题",validators=[DataRequired(message="文章标题不能为空")])
	thing = TextAreaField("文章内容",validators=[DataRequired(message="文章内容不能为空")])
	submit = SubmitField("发表文章")



class RequestResetForm(FlaskForm):
	email = StringField("邮箱",validators = [DataRequired(message="请填入邮箱"),Email(message="邮箱格式错误")])
	submit = SubmitField("点我找回密码")
	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('email未查询到，如果未注册，请先注册账号')


class PasswordResetForm(FlaskForm):
	password = PasswordField("密码",validators = [DataRequired(message="请填入密码")])
	confirm_password = PasswordField("确认密码",validators = [DataRequired(message="请再次填入密码"),EqualTo("password",message="两次密码不一致")])
	submit = SubmitField("点击重置密码")
		


