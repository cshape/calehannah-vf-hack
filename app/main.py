from flask import Flask, jsonify
from googlesearch import search

app = Flask(__name__)

prompt_elements = []
database_connection = [] # if long term

@app.route("/")
def home_view():
        return "<h1>Hi Hannah!</h1>"

@app.route("/test")
def test():
        return jsonify({'name': 'cale',
                    'occupation': 'cool guy'})

@app.route("/search")
def search():
        pass
        # takes some text as a param then searches google. returns google response as JSON
        # hi this is cale trying to push

@app.route("/openai")
def openai():
        # takes some text as a param then sends to gpt-3. returns gpt-3 response as JSON
        pass

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response as JSON
        pass