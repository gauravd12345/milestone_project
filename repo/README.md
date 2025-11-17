
# LMS Minimal Prototype (Flask Stubs)

A non-functional architectural stub demonstrating Flask + SQLAlchemy (SQLite), Flask-Login wiring, and WTForms. Pages render HTML stubs; POST on `/auth/login` validates and flashes "Not implemented".

## Stack

- Flask
- SQLAlchemy with SQLite
- Flask-Login (wired)
- WTForms via Flask-WTF (CSRF + validation)

## Run (Dev)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py              # or: flask run (set FLASK_APP=run.py)
```

Home Page:
<img width="1712" height="605" alt="Screenshot 2025-11-16 at 10 27 58 PM" src="https://github.com/user-attachments/assets/e618dbd3-ea85-4201-96c1-34752cdc745e" />

Login Page:
<img width="1697" height="648" alt="Screenshot 2025-11-16 at 10 33 01 PM" src="https://github.com/user-attachments/assets/229ebfcd-56d8-4708-930c-790f91387bf3" />

