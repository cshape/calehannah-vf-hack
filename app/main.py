from flask import Flask, jsonify, request
from googlesearch import search
import openai
import requests
import json
import os, sys

app = Flask(__name__)

prompt_elements = []
database_connection = [] # if long term
environment = "dev"

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        environment = "prod"
        return {}
secrets = read_secrets()
print(environment)

if environment == "dev":
        auth = f"Bearer {secrets['openai_key']}"
else:
        auth = f"Bearer {os.getenv('openai_key')}"

@app.route("/")
def home_view():
        return "<h1>Hi hello Hannah!</h1>"

@app.route("/test")
def test():
        return jsonify({'name': 'cale',
                    'occupation': 'cool guy'})

@app.route("/tosearch")
def to_search():
        search_term = request.args.get("term")

        results = []
        results.extend(search(search_term, advanced="True"))

        return f"{results}"        
        # takes some text as a param then searches google. returns google response as JSON

@app.route("/openaisearch")
def openai():
        text = request.args.get("text")
        prompt = text + "\nEND OF TEXT.\n From the above text, think of a google search string you would use to learn more relevant information.\nGoogle Search Term:"
        config = {
             "model": "text-davinci-003",
             "prompt": prompt,
             "temperature": 0.7,
             "max_tokens": 512
           }
        print(auth)
        openairesponse = requests.post("https://api.openai.com/v1/completions", 
                headers={"Content-Type": "application/json", "Authorization": auth},
                json = config)
        jsonresponse = openairesponse.json()
        return jsonresponse["choices"][0]["text"]
        # takes some text as a param then sends to gpt-3. returns gpt-3 response as JSON
        pass

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response as JSON
        pass