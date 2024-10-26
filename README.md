# Flask Application Overview

This project is a Flask application that implements a user registration form with dropdown options and displays success messages upon form submission. It utilizes Tailwind CSS for styling and organizes the application using Blueprints.

## Project Structure


## Features

1. **Virtual Environment**: 
   - Created using `python -m venv venv`.

2. **Profile Folder**:
   - Contains two files:
     - **`reader.py`**: 
       - Manages the following functions:
         - Populating dropdown options for the user form.
         - Handling user data save on form submission.
     - **`router.py`**: 
       - Manages all routes available in the application:
         - Uses Flask Blueprints to link routes with the application.
         - **Home Route**: Displays the initial homepage using a GET method.
         - **Submit Route**: Handles form submission using data from the request with a POST method. 
           - On empty form submission, the user is redirected to the homepage with a flash message.

3. **Application Initialization**: 
   - **`app.py`**: Responsible for initializing the Flask app.

4. **Tailwind CSS Integration**: 
   - Integrated using CDN for styling the application.

5. **Templates**:
   - Contains two files:
     - **`homepage.html`**: Displays the form for user submission and handles flash messages and template tags.
     - **`success.html`**: Rendered upon successful submission of the user form.

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. install all requirements
   ```bash
   pip install -r requirements.txt
   ```  
5. start application
   ```bash
    python app.py
   ```

