from flask import Flask, jsonify, request
from googlesearch import search
import openai
import requests
import json
import os, sys
import smtplib, ssl
from email.message import EmailMessage
from langchain.llms import OpenAI


app = Flask(__name__)

prompt_elements = []
database_connection = [] # if long term

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            global environment
            environment = "dev"
            return json.loads(f.read())
    except (FileNotFoundError) as error:
        print(error)
        environment = "prod"
    else:
        environment = "prod"   
secrets = read_secrets()
print(secrets)
print(environment)

if environment == "dev":
        auth = f"Bearer {secrets['openai_key']}"
        email_auth = secrets['email_key']
        os.environ["OPENAI_API_KEY"] = secrets['openai_key']
else:
        auth = f"Bearer {os.getenv('openai_key')}"
        email_auth = os.getenv('email_key')


@app.route("/")
def home_view():
        return "<h1>Hi hello Hannah!</h1>"

@app.route("/langchainGoog")
def langchainGoog():
        try:
           text = request.args.get("text")
           prompt = text + "\nEND OF TEXT.\n From the above text, think of a simple five or six word string you would use to find some relevant information on wedding venues using Google. Make sure to include the location\n Search Term:"
           llm = OpenAI(temperature=0.7)
           response = llm(prompt)
           print(response)
           return response
        except Exception as e:
           print(e)
           return "something went wrong"
        
@app.route("/openaisearch")
def openai():
        text = request.args.get("text")
        prompt = text + "\nEND OF TEXT.\n From the above text, think of a simple five or six word string you would use to find some relevant information on wedding venues using Google. Make sure to include the location\n Search Term:"
        config = {
             "model": "text-davinci-003",
             "prompt": prompt,
             "temperature": 0.7,
             "max_tokens": 1024
           }
        print(auth)
        openairesponse = requests.post("https://api.openai.com/v1/completions", 
                headers={"Content-Type": "application/json", "Authorization": auth},
                json = config)
        jsonresponse = openairesponse.json()
        formattedresponse = {
                'searchterm': jsonresponse["choices"][0]["text"]
        }
        return formattedresponse
        # takes some text as a param then sends to gpt-3. returns gpt-3 response as JSON
        pass

@app.route("/test")
def test():
        return jsonify({'name': 'cale',
                    'occupation': 'cool guy'})

@app.route("/tosearch")
def to_search():
        search_term = request.args.get("term")

        results = []
        try:
                results.extend(search(search_term, advanced="True"))
                return {
                'results': f'{results}'
                }  
        except:
                return {
                'results': "I was having some trouble searching the internet right now. Maybe you could let me know if you have specific venues, vendors or ideas you're thinking about in the meantime."
                }    
        
        # takes some text as a param then searches google. returns google response as JSON

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response as JSON
        pass

@app.route("/email")
def email():
        email = EmailMessage()
        print(email_auth)

        email["from"] = "Mary Maker"
        email["to"] = "caleandhannah@gmail.com"
        email["subject"] = "T-t-test 221321!"

        email.set_content("You can send this!")

        try:
                with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login("marymakerapp@gmail.com", email_auth)
                        smtp.send_message(email)
                        print("It's been sent!")
                        return "Email sent"
        except:
                return "Status of send unclear"

