from flask import Flask, url_for


app = Flask(__name__)


@app.route('/ur')
def index():pass

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/lu')
def nihao():
    return 'hello'

@app.route('/gg')
def jj():
    return 'gdago'

@app.route('/username/<username>')
def user_name(username):
    return 'username%s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post % d' % post_id


if __name__ == '__main__':
    app.run()



