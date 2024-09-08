# Civil Litigation Website

## Project Overview

This project is a comprehensive civil litigation website built using Django as the backend framework, with HTML and CSS for the frontend. The website provides information about civil litigation services, lawyer details, and includes a search functionality. It also features a chatbot to answer website-based questions.

## Features

- **Responsive Design**: The website is fully responsive, ensuring a seamless experience across various devices and screen sizes.
- **Navigation Bar**: Easy navigation through various pages of the website.
- **Lawyer Details**: Comprehensive information about lawyers specializing in civil litigation.
- **Search Functionality**: Allows users to search for specific information or lawyers.
- **Database Integration**: All data is stored and retrieved from a database for efficient management.
- **Authentication System**: Secure login and registration system for users and administrators.
- **Chatbot**: An AI-powered chatbot using Dialogflow to answer website-related questions.

## Technology Stack

- Backend: Django (Python)
- Frontend: HTML, CSS
- Database: Sqlite
- Chatbot: Dialogflow

## Setup and Installation

1. Clone the repository:
   ```
   git clone [https://github.com/sohailshk/Civil-Litigation-Website]
   ```

2. Navigate to the project directory:
   ```
   cd civil-litigation-website
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the website at `http://localhost:8000`

## Configuration

1. Dialogflow Chatbot:
   - Set up a Dialogflow agent and integrate it with the website.
   - Update the necessary credentials in the project settings.

2. Database:
   - Configure your database settings in `settings.py`.

3. Static Files:
   - Collect static files using `python manage.py collectstatic`.

##Screenshots
![image](https://github.com/user-attachments/assets/5afa8f47-466d-415d-8470-21f1a04e7c43)
