
import os
import json
import paralleldots
import string
from flask import Flask, request
from flask import render_template, send_from_directory
from pythonosc import osc_message_builder, udp_client

API_KEY = os.environ["API_KEY"]
OSC_CLIENTS = os.environ["OSC_CLIENTS"].split(",")

# creates a Flask application, named app
app = Flask(__name__, static_url_path='')
paralleldots.set_api_key(API_KEY)
clients = [udp_client.SimpleUDPClient(c[0], int(c[1])) for c in [u.split(":") for u in OSC_CLIENTS]]


def send_osc(result, clients):
    """ Send the detected emotions to each OSC client.
    """
    emotions = [
        str(result["emotion"]["Excited"]),
        str(result["emotion"]["Bored"]),
        str(result["emotion"]["Happy"]),
        str(result["emotion"]["Fear"]),
        str(result["emotion"]["Angry"]),
        str(result["emotion"]["Sad"]),
    ]
    sentiment = " ".join(emotions)
    result["nw"] = [ sum([i.strip(string.punctuation).isalpha() for i in result["text"].split()]) ]
    result["wl"] = [ len(i) for i in result["text"].split() ]
    for c in clients:
        c.send_message("/sentiment", sentiment)
        c.send_message("/np", result["nw"])
        c.send_message("/lp", result["wl"])
        c.send_message("/text", result["text"])


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
    return send_from_directory("statics", "index.html")


@app.route("/static/<path:path>")
def send_files(path):
    """ Return static files
    """
    return send_from_directory("statics", path)


@app.route("/get_emotions", methods=["POST"])
def get_emotions():
    """ Endpoint exposed to get emotions from text
    """
    text = request.form["text"]
    lang = request.form["lang"]
    res = analyze_text(text, lang)
    send_osc(res, clients)
    return json.dumps(res, indent=2)

# run web application
if __name__ == "__main__":
    app.run(port=8080, debug=True)


