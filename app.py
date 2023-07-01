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
    return render_template("index.html", polls=polls_df)

@app.route("/polls/<id>")
def polls(id):
    # Retrieve a specific poll based on the given ID
    poll = polls_df.loc[int(id)]
    return render_template("show_poll.html", poll=poll)

@app.route("/polls", methods=["GET", "POST"])
def create_poll():
    if request.method == "GET":
        # Display the form to create a new poll
        return render_template("new_poll.html")
    elif request.method == "POST":
        # Retrieve the form data submitted to create a new poll
        poll = request.form["poll"]
        option1 = request.form["option1"]
        option2 = request.form["option2"]
        option3 = request.form["option3"]
        
        # Add the new poll to the polls DataFrame
        polls_df.loc[max(polls_df.index.values) + 1] = [poll, option1, option2, option3, 0, 0, 0]
        
        # Save the updated polls DataFrame to a CSV file
        polls_df.to_csv("polls.csv")
        
        # Redirect the user to the index page
        return redirect(url_for("index"))


@app.route("/vote/<id>/<option>")
def vote(id, option):
    if request.cookies.get(f"vote_{id}_cookie") is None:
        # Check if the user has already voted for this poll
        # If not, update the vote count for the selected option
        polls_df.at[int(id), "votes" + str(option)] += 1
        
        # Save the updated polls DataFrame to a CSV file
        polls_df.to_csv("polls.csv")
        
        # Create a response object and set a cookie to indicate that the user has voted
        response = make_response(redirect(url_for("polls", id=id)))
        response.set_cookie(f"vote_{id}_cookie", str(option))
        
        return response
    else:
        # If the user has already voted, return an error message
        return "Cannot vote more than once!"


if __name__ == "__main__":
    # Run the Flask app on localhost in debug mode
    app.run(host="localhost", debug=True)
