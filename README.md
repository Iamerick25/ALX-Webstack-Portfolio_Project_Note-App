<div align="center">
  
![ALX-Banner](https://github.com/Iamerick25/ALX_project_logos/blob/main/alx.png)
</div>

<p align="center">
<h2 align="center"><img align="center" src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" alt="footer" width="150"  height="150"/></h2>

<div align="center">
  
# ALX WEB-Stack Portfolio: `Note App🗒️`
</div>

Welcome to my ALX Final Portfolio! This portfolio showcases the development of a **Note-App**, which is a web-based application developed as part of the ALX-Africa Software Engineering programme. Below, you'll find detailed information about the project, its components, and how to set it up.

## Table of Contents

- [Overview](#overview)
- [Technologies-Used](#technologies-used)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

<div align="center">
  
![unnamed](https://github.com/Iamerick25/ALX_project_logos/blob/main/alx%20note%20pic.png)
</div>

---

## Overview

The **Note-App** is a web-based application designed to allow users to create, view, and delete notes. It's built using the Flask web framework and incorporates features such as user authentication, database storage, and dynamic rendering of content. The project demonstrates proficiency in backend development and serves as a showcase of Full Stack Software Engineering skills.

---

## Technologies-Used
The Note-App project utilizes the following technologies and tools:

* **Flask:** A lightweight web application framework for Python.
* **Object-Oriented Programming (OOP)**: Utilized for efficient code organization and maintainability.
* **SQLite:** A relational database management system used for storing user data and notes.
* **Flask-Login:** A Flask extension for managing user sessions and authentication.
* **Bootstrap:** A front-end framework for designing responsive and mobile-first websites.
* **Jinja:** The most popular template engine for Python projects.
* **JavaScript:** Used for client-side scripting and dynamic interactions.
* **jQuery:** A fast, small, and feature-rich JavaScript library for simplifying client-side scripting.
* **HTML:** The standard markup language for creating web pages and applications.
* **CSS:** Cascading Style Sheets for styling HTML elements and enhancing the visual presentation.
* **Git:** A version control system for tracking changes in the project codebase.
* **GitHub:** A platform for hosting and collaborating on Git repositories.

These technologies collectively enable the development of a robust and user-friendly web application for managing notes effectively.

---

## Components

The project consists of the following components:

- `Src/` - The main directory containing the application source code.
  - `instance/` - Directory containing the SQLite database file (`database.db`).
  - `website/` - Directory containing the Flask application code.
    - `static/` - Directory containing static files such as CSS and JavaScript.
      - `index.js` - JavaScript file containing client-side functionality.
    - `templates/` - Directory containing HTML templates.
      - `base.html`, `home.html`, `login.html`, `sign_up.html` - HTML templates for different pages.
    - `__init__.py`, `auth.py`, `models.py`, `views.py` - Python modules containing application logic.
- `main.py` - Main Python script to run the Flask application.
- `requirements.txt` - File containing dependencies required to run the application.

---

## Installation

To install and run the Note App on your local machine, follow these steps:

1. Clone the repository:

   ```groovy
   $ git clone https://github.com/your-username/note-app.git
   ```

2. Navigate to the project directory:

   ```groovy
   $ cd ALX-Webstack-Portfolio_Project_Note-App
   ```

3. Create a virtual environment (optional but recommended):

   ```groovy
   $ python3 -m venv venv
   ```

4. Activate the virtual environment:
    * On Windows:

   ```groovy
   $ venv\Scripts\activate
   ```
   * On macOS and Linux:

   ```groovy
   $ source venv/bin/activate
   ```

5. Install dependencies:

   ```groovy
   $ pip install -r requirements.txt
   ```

6. Run the Flask application:

   ```groovy
   $ python3 main.py
   ```
7. Access the application in your web browser at `http://localhost:5000`.

---

## Usage
Once the application is running, you can access it in your web browser. Here are some key features:

* **Home Page**: View existing notes and add new ones.
* **Login Page**: Authenticate with your email and password.
* **Sign-Up Page**: Create a new account.
* **Logout**: Log out of the application.

---

## Structure
Here is the `Structure` of the **Note-App🗒️**:
```groovy
root@ERICK:~/ALX-Webstack-Portfolio_Project_Note-App# ls
AUTHORS  LICENSE  README.md  Src  requirements.txt  venv
root@ERICK:~/ALX-Webstack-Portfolio_Project_Note-App# tree -I venv
.
├── AUTHORS
├── LICENSE
├── README.md
├── Src
│   ├── instance
│   │   └── database.db
│   ├── main.py
│   └── website
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── __init__.cpython-38.pyc
│       │   ├── auth.cpython-312.pyc
│       │   ├── auth.cpython-38.pyc
│       │   ├── models.cpython-312.pyc
│       │   ├── models.cpython-38.pyc
│       │   ├── views.cpython-312.pyc
│       │   └── views.cpython-38.pyc
│       ├── auth.py
│       ├── models.py
│       ├── static
│       │   └── index.js
│       ├── templates
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── login.html
│       │   └── sign_up.html
│       └── views.py
└── requirements.txt

6 directories, 23 files
root@ERICK:~/ALX-Webstack-Portfolio_Project_Note-App#
```

---

## Contributing
Contributions to the Note-App project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

---
