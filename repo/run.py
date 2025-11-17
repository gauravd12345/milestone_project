from app import create_app

app = create_app()

if __name__ == "__main__":
    # For local dev convenience
    app.run(debug=True)
