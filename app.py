from flask import Flask, session, url_for, request, redirect

from views.account import account_bp
from views.statistic_view import statistic_bp

app = Flask(__name__)
app.config.from_object(obj='settings.DevConfig')
# print(app.config.get('DEBUG'))
# print(app.config.get('SECRET_KEY'))
# 注册蓝图
app.register_blueprint(blueprint=account_bp)
app.register_blueprint(blueprint=statistic_bp)


# 认证
@app.before_request
def auth():
    white_urls = [url_for('account_bp.login'), url_for('hello_world')]
    if request.path in white_urls:
        return None
    if session.get('username'):
        return None

    return redirect(url_for('account_bp.login'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
