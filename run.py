# run.py
from DebtCollectionApp.wsgi import application  # Assuming your project's WSGI application is named 'application'

if __name__ == "__main__":
    application.run()