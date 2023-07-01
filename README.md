
# Polls Flask Project

The Polls Flask project is a web application that allows users to create and participate in polls. It is built using the Flask framework and provides basic functionality such as creating new polls, viewing poll details, and voting on poll options.

## Features

- **Create Polls:** Users can create new polls by providing a poll text and multiple options.

- **View Polls:** The application displays a list of available polls, allowing users to view the details of each poll.

- **Vote on Poll Options:** Users can vote on the available options for each poll. The vote count is updated accordingly.

- **Prevent Duplicate Voting:** The application prevents users from voting more than once for the same poll.

## Project Structure

The project has the following structure:

```
├── app.py                    # Main Flask application file
├── polls.csv                 # CSV file to store poll data
├── templates
│   ├── index.html            # Template for displaying the list of polls
│   ├── new_poll.html         # Template for creating a new poll
│   ├── show_poll.html        # Template for displaying poll details and voting
└── README.md                 # Project README file
```

- The `app.py` file contains the Flask application code, including route definitions, handling poll creation and voting, and rendering HTML templates.

- The `polls.csv` file serves as a data storage mechanism, storing the poll data in a CSV format.

- The `templates` directory contains HTML templates for different views, such as displaying the list of polls, creating a new poll, and showing poll details with voting options.

## Setup and Usage

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Flask application:

```
python app.py
```

4. Access the application in a web browser:

```
http://localhost:5000
```

## Dependencies

The project has the following dependencies:

- Flask: A micro web framework for Python.
- Pandas: A library for data manipulation and analysis (used for storing and retrieving poll data in CSV format).

## License

This project is licensed under the [MIT License](LICENSE).

```

Feel free to modify the above template as per your specific project requirements and add any additional information that might be relevant.
