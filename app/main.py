from flask import Flask, jsonify
 
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
        # takes some text as a param then searches google. returns google response
        pass

@app.route("/openai")
def openai():
        # takes some text as a param then sends to gpt-3. returns gpt-3 response
        pass

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response
        pass