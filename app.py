from flask import Flask
from messages import team_message


@app.route("/team/<team>")
def team(team):
    return team_message(team)


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Vendrigen 🚀"


if __name__ == "__main__":
    app.run(debug=True)
