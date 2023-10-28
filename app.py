import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
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


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
