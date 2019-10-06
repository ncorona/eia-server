
import os
import json
import paralleldots
import string
from flask import Flask, request
from flask import render_template, send_from_directory

API_KEY = os.environ["API_KEY"]
OSC_CLIENTS = os.environ["OSC_CLIENTS"].split(",")

# creates a Flask application, named app
app = Flask(__name__, static_url_path='')

def analyze_text(text, lang):
    """
    Returns the results for emotion detection analysis.
    Clean text removing puntuaction characters.
    """
    res = paralleldots.emotion(text, lang)
    clean_text = text
    for txt in string.punctuation:
        clean_text = clean_text.replace(txt, " ")
    res["text"] = clean_text
    return res


@app.route("/")
def index():
    """ Return the main index page
    """
    return send_from_directory('statics', 'index.html')


@app.route('/static/<path:path>')
def send_files(path):
    """ Return static files
    """
    return send_from_directory('statics', path)


@app.route("/get_emotions", methods=["POST"])
def get_emotions():
    """ Endpoint exposed to get emotions from text
    """
    text = request.form["text"]
    lang = request.form.get("lang", "it")
    res = analyze_text(text, lang)
    return json.dumps(res, indent=2)

# run web application
if __name__ == "__main__":
    app.run(port=8080, debug=True)
