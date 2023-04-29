from flask import Flask, jsonify
 
app = Flask(__name__)

prompt_elements = []
database_connection = [] # if long term
 
@app.route("/")
def home_view():
        return "<h1>Hi Hannah!</h1><p>I wonder what we should name the project...</p><ul><li>Lift the Veil</li><li>Mary Maker</li></ul>
        "

@app.route("/test")
def test():
        return jsonify({'name': 'cale',
                    'occupation': 'cool guy'})

@app.route("/search")
def search():
        # takes some text as a param then searches google. returns google response

@app.route("/openai")
def openai():
        # takes some text as a param then sends to gpt-3. returns gpt-3 response

@app.route("/voiceflow")
def voiceflow():
        # takes some text as a param then sends a request to voiceflow. returns voiceflow response