from flask import Flask, jsonify, render_template, request, flash
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'help!'

CORS(app)  # Enable CORS

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

# ---------- MESSAGES ------------
@app.route('/api', methods=['GET'])
def greet():
    response = {
        "greeting": "Hello Jeff From Flask",
        "message": "This is your custom message"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode
