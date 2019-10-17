from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://user1:Password1@cluster0-unazn.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/create" enctype="multipart/form-data">
            <input type="text" name="username">
            <input type="file" name="profile_image">
            <input type="submit">
        </form>
    '''
