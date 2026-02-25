from flask import Flask
from messages import team_message

app = Flask(__name__)


@app.route("/team/<team>")
def team(team):
    return team_message(team)


@app.route("/")
def home():
    return "Welcome to Vendrigen 🚀"


if __name__ == "___main___":
    app.run(debug=True)
