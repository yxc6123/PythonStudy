from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)

#创建bootstrap对象
bootstrap = Bootstrap(app)

#测试根目录
#localhost:5000
@app.route('/')
def index():
	return render_template('index.html')

#测试添加参数
#<name>为浏览器传入的参数
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	manager.run()


