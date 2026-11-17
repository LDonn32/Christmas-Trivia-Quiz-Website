# Christmas Trivia Quiz Website

A festive, browser-based Christmas trivia quiz built with Flask, HTML, CSS, and Jinja templates. The app presents multiple-choice questions, tracks the player's score in a Flask session, and shows a themed result message at the end of the quiz.

## Current Features

- Flask routes for the home page, quiz, and results page
- In-memory Christmas trivia questions
- Multiple-choice answers rendered with Jinja
- Session-based question position and score tracking
- Four score-based result messages
- Christmas-themed responsive styling
- Snowfall and twinkling-light effects
- Progress-bar markup and final-score display
- Gunicorn support for deployment
- Render deployment configuration

## Project Structure

```text
Christmas-Trivia-Quiz-Website/
|-- app.py                    # Flask application and routes
|-- questions.py              # Trivia questions and answers
|-- static/
|   |-- style.css             # Layout, animation, and responsive styles
|   `-- images/
|       `-- ELF Movie Image.jpeg
|-- templates/
|   |-- index.html            # Landing page
|   |-- quiz.html             # Question and answer page
|   |-- results.html          # Final score and result message
|   `-- snowflake.html        # Standalone snowflake markup
|-- requirments.txt           # Python dependencies
|-- render.yaml               # Render web-service configuration
`-- README.md
```

## How It Works

1. A player starts a quiz, which resets the session score and question index.
2. `app.py` displays one question at a time from `questions.py`.
3. The submitted answer is compared with the correct answer.
4. The score and question index are stored in the Flask session.
5. After the last question, the player is redirected to the results page.

## Routes

| Route | Methods | Purpose |
| --- | --- | --- |
| `/` | `GET` | Displays the landing page |
| `/start` | `POST` | Resets the quiz and redirects to `/quiz` |
| `/quiz` | `GET`, `POST` | Shows questions and records answers |
| `/results` | `GET` | Displays the score and festive result message |

## Run Locally

### Prerequisites

- Python 3
- `pip`

### Installation

```powershell
cd C:\Users\laura\Documents\GitHub\Christmas-Trivia-Quiz-Website
python -m pip install -r requirments.txt
python app.py
```

Then open `http://127.0.0.1:5000` in a browser.

`app.py` enables Flask debug mode when run directly.

## Dependencies

The project currently declares:

- **Flask** - web server and template rendering
- **gunicorn** - production WSGI server

## Deployment

`render.yaml` defines a Python web service named `christmas-trivia-quiz` using Gunicorn:

```text
gunicorn app:app
```

## Current Project Notes

- `questions.py` currently contains 7 trivia questions, although the quiz and results templates use a `/12` label and a 12-question progress calculation. I need to update the questions to be better and more fun. Basic for nwo
- `templates/index.html` is incomplete and currently does not include a form or link that submits a request to `/start`. I need to add.
- `templates/snowflake.html` is currently standalone markup and is not rendered by a Flask route.
- The static background uses an Unsplash image URL as well as local project assets.
- The app uses a hardcoded Flask secret key, so a deployment-oriented implementation should replace it with an environment variable.

