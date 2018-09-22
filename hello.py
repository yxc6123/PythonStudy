from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


#测试根目录
#localhost:5000
@app.route('/')
def index():
	return 'Hello World!</h1>'

#测试添加参数
#<name>为浏览器传入的参数
@app.route('/user/<name>')
def user(name):
	return 'Hello, %s' % name


if __name__ == '__main__':
	manager.run()


