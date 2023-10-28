import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from enums import MAX_SCORE, NAME, student
load_dotenv()

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/name")
def my_name():
    return render_template("my_name.html")


@app.route("/birthday_date")
def  my_birthday_date():
    return render_template("my_birthday_date.html")

@app.route("/age")
def my_age():
    return render_template("my_age.html")

@app.route("/base")
def base():
    return render_template("base.html", title="Python cours")


@app.route("/context")
def context():
    context_dict = {
        "title": "Python Course",
        "name": NAME,
        "max_score": MAX_SCORE,
        "students": student
    }
    return render_template("context.html", **context_dict)


@app.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        user = request.form.get("name")
        return "Method POST"
    else:
        user = request.args.get("name")
        return f'Method GET, user is {user}'

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
