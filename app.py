from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def survey_home_page():
  title = satisfaction_survey.title
  instructions = satisfaction_survey.instructions
  return render_template("start.html", title=title, instructions=instructions)
