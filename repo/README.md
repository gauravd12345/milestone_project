# StudyBuddy – Milestone 2

StudyBuddy is a lightweight Flask application that helps students set, track, and complete weekly academic goals. Unlike traditional LMS tools that focus on grades and content delivery, StudyBuddy emphasizes habit-building, weekly goal-setting, and personal accountability. This M2 prototype implements the majority of the MVP feature set, including authentication, goal management, course tagging, and progress tracking.

## Tech Stack

- Flask (web framework)
- Flask-Login (authentication/session handling)
- Flask-WTF / WTForms (form handling + validation)
- SQLAlchemy + SQLite (database persistence)
- Pytest (unit testing)

## Implemented Features (Milestone 2)
### Core MVP Features (8/12 completed)

- User registration and login
- Create weekly study goals
- Edit and update existing goals
- Tag goals with course identifiers (e.g., "CMPE 131")
- Mark goals as completed (via status field)
- View all goals in a styled dashboard
- View completed goals history
- View profile summary (total goals, completed goals, and course tags)

### Planned for Milestone 3

- Study group membership
- Viewing peer/group members
- Posting progress updates on goals
- Sending nudges to peers

## Project Structure
```repo/
  app/
    auth/          # login, logout, registration
    main/          # homepage, profile page
    tasks/         # create/edit/delete goals
    static/        # global stylesheets
    templates/     # shared + page templates
    models.py      # User, Task models
    forms.py       # WTForms classes
    config.py
    __init__.py
  tests/
    conftest.py
    test_auth.py
    test_goals.py
    test_profile.py
  run.py
  requirements.txt
  README.md
```

## Running the App (Development)
```python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py                 # or: flask run """ 
```

The app will be available at: ```http://127.0.0.1:5000/```

If your browser shows a 403 error due to caching, open localhost in an incognito window.

## Running Tests
```Run the following command in milestone1/repo/: pytest -v``` 

The included test suite verifies:
- Registration and login functionality
- Goal creation and database persistence
- Completed goals display
- Profile summaries and course tracking

All tests pass successfully in M2:

<img width="609" height="255" alt="Screenshot 2025-12-08 at 7 18 15 PM" src="https://github.com/user-attachments/assets/c5a828b5-2321-4bd4-9439-e275f1e79392" />


## Screenshots
#### Home Page

<img width="1722" height="660" alt="Screenshot 2025-12-08 at 6 50 03 PM" src="https://github.com/user-attachments/assets/46034450-a2eb-4fe5-8a63-11c97c84118c" />


#### Goals Dashboard

<img width="1727" height="747" alt="Screenshot 2025-12-08 at 6 50 45 PM" src="https://github.com/user-attachments/assets/aaa07b18-c01e-4776-b1b1-bb3f03a05219" />


#### Edit Goal Page

<img width="1728" height="774" alt="Screenshot 2025-12-08 at 6 51 17 PM" src="https://github.com/user-attachments/assets/81f9eca3-770b-4e4d-94b7-31bc2984c56b" />


#### Completed Goals

<img width="1728" height="511" alt="Screenshot 2025-12-08 at 6 51 26 PM" src="https://github.com/user-attachments/assets/66a68cf3-2c1d-444d-997d-d6fffd8d515c" />


## Milestone 2 Summary

Compared to M1, this milestone introduces:
- Fully functional authentication system
- SQLAlchemy-backed models and persistence
- Goal creation, editing, completion, and tagging
- Profile and completed-goals pages
- Consistent UI styling with shared templates
- Working pytest suite with isolated temporary databases

This milestone delivers a functional early version of StudyBuddy, covering over 60–70% of planned MVP features.

## Roles:
Gaurav: Responsible for backend development, including Flask routing, SQLAlchemy models, authentication, and goal management logic.
Brenda: Responsible for frontend design, including UI styling, templates, layout, and improving overall user experience across the app.
