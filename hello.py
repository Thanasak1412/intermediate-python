# run
# FLASK_APP=<filename.py> flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return "About"

@app.route("/name/<name>")
def get_name(name):
    return render_template("name.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)