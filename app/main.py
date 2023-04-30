from flask import Flask, jsonify, request
from googlesearch import search
import openai
import requests
import json
import smtplib, ssl
from email.message import EmailMessage
import emailsender

app = Flask(__name__)

prompt_elements = []
database_connection = [] # if long term

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
        print(prompt)
        openai.api_key = ""
        config = {
             "model": "text-davinci-003",
             "prompt": prompt,
             "temperature": 0.7,
             "max_tokens": 512
           }
        openairesponse = requests.post("https://api.openai.com/v1/completions", 
                headers={"Content-Type": "application/json", "Authorization": "Bearer "},
                json = config)
        jsonresponse = openairesponse.json()
        return jsonresponse["choices"][0]["text"]
        # takes some text as a param then sends to gpt-3. returns gpt-3 response as JSON
        pass

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response as JSON
        pass

@app.route("/email")
def email():
        return emailsender.sender()
