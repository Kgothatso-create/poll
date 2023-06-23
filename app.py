import os.path
import pandas as pd
from flask import Flask, render_template, redirect, request, url_for, make_response

app = Flask(__name__, template_folder="templates")

# Check if the "polls.csv" file exists, if not, create it with the specified structure
if not os.path.exists("polls.csv"):
    structure = {
        "id": [],
        "poll": [],
        "option1": [],
        "option2": [],
        "option3": [],
        "votes1": [],
        "votes2": [],
        "votes3": [],
    }
    
    pd.DataFrame(structure).set_index("id").to_csv("polls.csv")

# Read the polls from the "polls.csv" file and set the index to "id"
polls_df = pd.read_csv("polls.csv").set_index("id")

@app.route("/")
def index():
    return "Hello world"

@app.route("/polls/<id>")
def polls(id):
    # Retrieve a specific poll based on the given ID
    poll = polls_df.loc[int(id)]
    return str(poll)

@app.route("/polls", methods=["GET", "POST"])
def create_poll():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

@app.route("/vote/<id>/<option>")
def vote(id, option):
    pass

if __name__ == "__main__":
    # Run the Flask app on localhost in debug mode
    app.run(host="localhost", debug=True)
