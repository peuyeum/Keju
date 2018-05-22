from flask import Flask,request
import jsonify
from scopus import Authfirst as AUF #memberikan alias dari Autofirst dari package scopus
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih #mengembalikan nilai dari variale gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/scopus/AUTHFIRST/<nama>', methods=['GET'])
def retrn(nama):
    return str(AUF.cari(nama))