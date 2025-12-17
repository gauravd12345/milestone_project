# StudyBuddy

StudyBuddy is a lightweight Flask application that helps students set, track, and complete weekly academic goals. Unlike traditional LMS tools that emphasize grades and content delivery, StudyBuddy focuses on habit-building, weekly goal-setting, accountability, and peer encouragement. The M3 release implements **100% of the MVP feature set**, a redesigned TailwindCSS UI, analytics, study groups with nudges, and a comprehensive test suite with 91% coverage.


## Tech Stack

* **Flask** – backend framework
* **Flask-Login** – authentication + session handling
* **Flask-WTF / WTForms** – form handling + validation
* **SQLAlchemy + SQLite** – ORM and persistent storage
* **TailwindCSS** – full UI design and styling
* **Pytest + pytest-cov** – unit tests, integration tests, coverage reports


# **Implemented Features (Milestone 3)**

## **Core MVP Features (12 / 12 Complete)**

1. User registration
2. User login
3. User logout
4. Create weekly goals
5. Edit/update goals
6. Delete goals
7. View goals dashboard
8. Completed goals page
9. Progress reflections (progress_note)
10. Tag goals by course
11. Profile summary (total goals, completed goals, courses)
12. Authentication-protected routes

## **Additional Required MVP Features (M3)**

* Study group membership
* View other group members
* Send nudges to peers

## **Stretch Goals Achieved**

* Reflection prompts integrated into goal creation/editing
* Study streak tracking
* 7-day activity analytics chart
* Canvas LMS connection (save and open course URL)


# **Project Structure**

```
app/
  auth/              # registration, login, logout  
  main/              # home, profile, analytics  
  tasks/             # goal create/edit/delete  
  groups/            # study groups + nudges  
  templates/         # all HTML templates (Tailwind)  
  static/            # styles.css  
  models.py          # User, Task, StudyGroup, Nudge, etc.  
  forms.py           # WTForms  
  config.py  
  __init__.py  

tests/
  test_auth.py
  test_goals.py
  test_goals_edit.py
  test_profile.py
  test_progress_update.py
  test_integration_auth.py
  test_integration_goals.py
  test_integration_groups.py
  test_permissions.py
  test_404.py

run.py
requirements.txt
README.md
```


# **Running the Application**

```bash
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask run
```

The app will be available at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

If your browser incorrectly caches a 403, try an incognito window.


# **Running Tests**

Run all tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

### 🧾 **Test Suite Summary**

* **16 tests passed**
* **91% total coverage**

  * 95% model coverage
  * 80%+ route coverage
* Tests cover:

  * Authentication
  * Goal CRUD
  * Reflections
  * Profile analytics
  * Study groups
  * Nudges
  * 404 error
  * Unauthorized access


# **Screenshots (Include in your PDF submission)**

Screenshots:


1. Home Page
   
<img width="627" height="330" alt="Screenshot 2025-12-16 at 11 38 31 PM" src="https://github.com/user-attachments/assets/ab330826-fced-4435-8423-bf491e52e0f2" />

2. Goals Dashboard
   
   <img width="623" height="281" alt="Screenshot 2025-12-16 at 11 38 55 PM" src="https://github.com/user-attachments/assets/1e146fe4-532f-4b6c-8aea-993436e4bb76" />

3. Profile Page (streak + activity chart + Canvas link)
   
   <img width="624" height="311" alt="Screenshot 2025-12-16 at 11 39 08 PM" src="https://github.com/user-attachments/assets/ef536689-f1db-4f1e-993f-d97751656176" />

4. Study Group Page (members + nudges)

<img width="627" height="295" alt="Screenshot 2025-12-16 at 11 39 22 PM" src="https://github.com/user-attachments/assets/d2fa77c9-dbf9-4fad-9889-14a664c3f6db" />


# **Milestone 3 Summary**

Compared to Milestone 2, this release adds:

* Complete TailwindCSS UI overhaul
* Study streak tracking
* 7-day activity chart
* Canvas LMS URL integration
* Study groups + member directories
* Peer nudges
* Full integration test suite
* 91% code coverage

StudyBuddy is now a fully functional, data-persistent, well-tested MVP suitable for student goal tracking and habit formation.

# **Roles**

**Gaurav** – Backend development: Flask routing, SQLAlchemy models, authentication, study groups, analytics, integration tests.

**Brenda** – Frontend development: TailwindCSS UI design, templates, layout, UX improvements.

