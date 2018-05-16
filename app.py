from flask import Flask,request
from scopus import Subjarea as SA
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/frans/<a>')
def house(a):
	return SA.home(a)

@app.route('/Subjarea/<b>')
def serah(b):
	return SA.mendapatkan(b)