# Crowdfunding Platform

A simple Django-based crowdfunding web application that allows users to create projects, donate to them, and track progress in real-time.

## Features
- **User Authentication**: Sign up, sign in, and manage your account.
- **Project Creation**: Users can create new projects with details such as title, description, target amount, and deadline.
- **Donation System**: Users can donate to projects and see the progress bar update.
- **Responsive UI**: Clean and simple interface with earthy/soft green tones for better user experience.
- **Project Browsing**: Explore all projects and view details of each one.
- **Cancel Project Creation**: Cancel creating a project and return to the home page.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Version Control**: Git & GitHub

## Installation & Setup
1. **Clone the repository**
2. **Create & activate virtual environment**
     python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

3. ** Install dependencies**
    pip install -r requirements.txt

4. **Apply migrations**
     python manage.py migrate
   
6. **Run the development server**  
     python manage.py runserver



Usage
1-Sign up for a new account or sign in if you already have one.

2-Create a project with the desired details.

3-Donate to projects and track their progress.

4-Cancel project creation to return to the home page.

 
