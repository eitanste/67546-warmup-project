import os
from flask import Flask, render_template, request

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/uploads'

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    
    # Your backend logic goes here 
    # you can follow the steps in this tutorial: 
    # https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask 
    
    return '', 204

@app.route('/database')
def database():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('database.html', files=files)