from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def survey_home_page():
  """Create home page with the title of the survey along with the instructions."""

  title = satisfaction_survey.title
  instructions = satisfaction_survey.instructions

  return render_template("start.html", title=title, instructions=instructions)

@app.route("/questions/<int:num>")
def ask_question(num):
  """Create individual question page for each question in surveys.py."""

  questions = satisfaction_survey.questions

  """Redirect user if they try to access another page after completing the survey."""

  if len(responses) == len(questions):
    return redirect("/finish")

  """Redirect user if they try to access an invalid question or go out of order."""

  if num != len(responses):
    flash("Invalid question request")
    return redirect(f"/questions/{len(responses)}")

  question = questions[num].question
  choices = questions[num].choices

  return render_template("questions.html", question=question, choices=choices, num=num)

@app.route("/questions/<int:num>", methods=["POST"])
def add_answer(num):
  """Save answers to responses."""

  answer = request.form["answer"]
  responses.append(answer)

  """Redirect user to confirmation page if they have completed the survey."""
  if len(responses) == len(satisfaction_survey.questions):
    return redirect("/finish")
  return redirect(f"/questions/{num + 1}")

@app.route("/finish")
def finish():
  return render_template("thank-you.html")
