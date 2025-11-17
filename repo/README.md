
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
