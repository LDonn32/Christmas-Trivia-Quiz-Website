from flask import Flask, render_template, request, redirect, session
from questions import questions

app = Flask(__name__)

app.secret_key = "christmas-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():

    session["question_index"] = 0
    session["score"] = 0

    return redirect("/quiz")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    question_index = session.get("question_index", 0)
    score = session.get("score", 0)

    if request.method == "POST":

        selected_answer = request.form.get("answer")

        previous_question = questions[question_index]

        if selected_answer == previous_question["answer"]:
            score += 1

        session["score"] = score

        question_index += 1
        session["question_index"] = question_index

    if question_index >= len(questions):
        return redirect("/results")

    current_question = questions[question_index]

    return render_template(
        "quiz.html",
        question=current_question,
        question_number=question_index + 1
    )


@app.route("/results")
def results():

    score = session.get("score", 0)

    if score >= 10:
        message = "🎅 Christmas Expert!"
    elif score >= 7:
        message = "🎄 Festive Genius!"
    elif score >= 4:
        message = "☃️ Holiday Helper!"
    else:
        message = "🎁 Time to watch a few Christmas movies!"

    return render_template(
        "results.html",
        score=score,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)