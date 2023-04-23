from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>welcome to cale and hannahs hack projjjekt</h1>"

@app.route("/test")
def test():
        return jsonify({'name': 'cale',
                    'occupation': 'cool guy'})