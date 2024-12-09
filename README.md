# Library Management System

A simple web-based Library Management System built with **Flask** and **SQLAlchemy**. This application allows users to manage a collection of books, including adding, editing, deleting, and searching books by title.

---

## Table of Contents
1. [How to Run the Project](#how-to-run-the-project)
2. [Design Choices Made](#design-choices-made)
3. [Assumptions and Limitations](#assumptions-and-limitations)

---

## How to Run the Project

### Prerequisites
- Python 3.7 or higher
- Virtual Environment (optional but recommended)
- Installed dependencies (listed in `requirements.txt`)

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/library-management-system.git
   cd library-management-system
2.**Set Up a Virtual Environment**:

    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3.**Install Dependencies**:

      pip install -r requirements.txt

4. **Initialize the Database**:

  Open a Python shell:
  
      python
  Run the following commands:
  
      python
      from app import db
      db.create_all()
      exit()
5. **Run the Application**:

On Linux/macOS:

    export FLASK_APP=app.py
    flask run
On Windows Command Prompt:cmd

    set FLASK_APP=app.py
    flask run
On Windows PowerShell:

    $env:FLASK_APP="app.py"
    flask run
6. **Access the Application-Open your browser and visit**:

        http://127.0.0.1:5000
## Design Choices Made

### Framework and Libraries
- Flask: Chosen for its lightweight and modular nature, making it ideal for small to medium-sized projects.
- SQLAlchemy: Used as the ORM for database management, simplifying database interactions.
- Flask-WTF: Integrated to handle form validation in an elegant and structured way.
### Project Structure
  **Separation of Concerns**:
  
 - app.py: Contains the routes and main application logic.
 - models.py: Handles database models using SQLAlchemy.
 - forms.py: Encapsulates form logic for book-related operations.
 - templates/: Contains all HTML files, organized for reusability and clarity.
### Front-End Design

- Bootstrap: Used for responsive and clean styling.
- Template inheritance with base.html ensures consistent layout and reduces redundancy.

## Assumptions and Limitations
### Assumptions
- A Book is defined with the following attributes:
    - title: String, maximum 150 characters.
    - author: String, maximum 100 characters.
    - year: Integer, representing the publication year.
- The title of a book does not have to be unique.
- The application is primarily for local, single-user access.
### Limitations
- No Authentication: The application does not include user authentication or role-based access control.
- Limited Search Functionality: Search is only by title, and it performs a case-insensitive partial match.
- Basic Validation: The form validations (e.g., publication year) are minimal.
- Scalability: The application is designed for small datasets and may require optimizations for larger datasets or multi-user environments.
- Static Deployment: Currently intended to be run locally; deployment to a production environment (e.g., using Docker or Heroku) would require additional setup.
