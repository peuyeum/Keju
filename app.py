from flask import Flask,request
from scopus import afiliasi as afl
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

@app.route('/scopus/AFFIL/<a>', methods=['GET']) #penggunaan method GET untuk menampilkan data dalam bentuk tag HTML
def home(a):
	return afl.hom(a)