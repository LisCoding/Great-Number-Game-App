import random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'number' not in session:
        # new game, no guesses yet
        session['random'] = random.randrange(0,101)
        return render_template("index.html", answer = "")
    else:
        if session['random'] == session['number']:
            answer = "You WON.  Let's play one more time"
            session.pop('number')
            session['random'] = random.randrange(0,101)
            return render_template("win.html", answer = answer)
        elif session['random'] > session['number']:
            answer = "too low"
        elif session['random'] < session['number']:
            answer = "too high"
        return render_template("index.html", answer = answer)

@app.route("/guess", methods=["POST"])
def guess():
    session['number'] = int(request.form["number"])
    return redirect("/")

@app.route("/new", methods=["POST"])
def new_game():
    return redirect("/")
app.run(debug=True)
