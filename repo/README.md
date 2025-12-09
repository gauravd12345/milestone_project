# StudyBuddy – Milestone 2

StudyBuddy is a lightweight Flask application that helps students set, track, and complete weekly academic goals. Unlike traditional LMS tools that focus on grades and content delivery, StudyBuddy emphasizes habit-building, weekly goal-setting, and personal accountability. This M2 prototype implements the majority of the MVP feature set, including authentication, goal management, course tagging, and progress tracking.

## Tech Stack

- Flask (web framework)
- Flask-Login (authentication/session handling)
- Flask-WTF / WTForms (form handling + validation)
- SQLAlchemy + SQLite (database persistence)
- Pytest (unit testing)

## Implemented Features (Milestone 2)
### Core MVP Features (9/12 completed)

- User registration and login using Flask-Login
- Create weekly study goals
- View goals dashboard
- Edit and update goals
- Mark goals as completed using status field
- Tag goals by course (course_code field)
- Completed goals page showing all finished tasks
- Profile page summarizing total goals, completed goals, and course tags
- Posting progress updates


### Planned for Milestone 3

- Study group membership
- Viewing other group members
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

StudyBuddy includes <b>7 meaningful unit test cases</b> covering authentication, goal creation, editing, completion history, profile logic, and model defaults. All tests pass successfully in M2:

<img width="612" height="323" alt="Screenshot 2025-12-08 at 8 37 05 PM" src="https://github.com/user-attachments/assets/0af68177-cdef-48f1-acc5-690b1bb82ff7" />


## Screenshots
#### Home Page

<img width="1684" height="882" alt="Screenshot 2025-12-08 at 8 30 33 PM" src="https://github.com/user-attachments/assets/a01648ea-92e1-4ddd-97aa-cdd0a835a81b" />


#### Goals Dashboard

<img width="1685" height="829" alt="Screenshot 2025-12-08 at 8 30 43 PM" src="https://github.com/user-attachments/assets/e6e81fdc-650a-46e8-8301-bb0e3955a7f8" />


#### Edit Goal Page

<img width="1676" height="781" alt="Screenshot 2025-12-08 at 8 30 58 PM" src="https://github.com/user-attachments/assets/2eea45b2-444c-478b-a272-3cc8c8b3d3b3" />


#### Completed Goals

<img width="1684" height="751" alt="Screenshot 2025-12-08 at 8 31 16 PM" src="https://github.com/user-attachments/assets/40ccdb98-f686-4edc-8eb7-d4af72c047d3" />

## Milestone 2 Summary

Compared to M1, this milestone introduces:
- Fully functional authentication system
- SQLAlchemy-backed models and persistence
- Goal creation, editing, completion, and tagging
- Profile and completed-goals pages
- Consistent UI styling with shared templates
- Working pytest suite with isolated temporary databases

This milestone delivers a functional early version of StudyBuddy, covering 75% of planned MVP features.

## Roles:
Gaurav: Responsible for backend development, including Flask routing, SQLAlchemy models, authentication, and goal management logic.
Brenda: Responsible for frontend design, including UI styling, templates, layout, and improving overall user experience across the app.
