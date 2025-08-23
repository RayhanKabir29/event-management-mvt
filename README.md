Event Management System – CRUD and Optimized Queries (Django + Tailwind CSS)

A fully functional Event Management System built using Django and styled with Tailwind CSS, demonstrating CRUD operations, optimized database queries using Django ORM, and a responsive, user-friendly interface.

Features
1. Data Models

Event: name, description, date, time, location, category (ForeignKey to Category)

Participant: name, email, ManyToMany relationship with Event

Category: name and description

2. CRUD Operations

Full Create, Read, Update, Delete functionality for Event, Participant, and Category

Form validation to ensure clean data input

3. Optimized Database Queries

select_related to efficiently fetch each event’s category

prefetch_related to fetch participants for events with fewer queries

aggregate query to calculate total number of participants across all events

filter queries:

Display events by category

Display events within a date range

4. Responsive UI with Tailwind CSS

Fully responsive layout for desktop, tablet, and mobile

Event List Page:

Displays events with categories and participant counts

Event Detail Page:

Shows detailed event info and associated participants

Forms to add/update events, participants, and categories with consistent styling

Navigation bar for seamless movement between pages

5. Organizer Dashboard

Stats Grid:

Total participants

Total events

Upcoming events

Past events

Today’s Events Listing under the stats grid

Interactive Stats: Clicking any stat dynamically updates the displayed data below

6. Search Feature

Search events by name or location using request.GET

Case-insensitive matching with icontains

Technologies Used

Backend: Django (Python)

Frontend: Tailwind CSS

Database: SQLite (can be switched to PostgreSQL/MySQL easily)

Template Engine: Django Templates

Installation

Clone the repository:

git clone https://github.com/your-username/event-management-system.git
cd event-management-system


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Create a superuser (optional for admin panel access):

python manage.py createsuperuser


Run the server:

python manage.py runserver


Access the app:
Open http://127.0.0.1:8000
 in your browser.

Project Structure
event-management-system/
│
├── events/                 # Django app with models, views, urls, templates
│   ├── models.py           # Event, Participant, Category models
│   ├── views.py            # CRUD + Dashboard + Search logic
│   ├── urls.py             # Routes for events app
│   └── templates/events/   # HTML templates styled with Tailwind
│
├── event_management/       # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/                 # Tailwind CSS files and assets
├── templates/              # Base templates and shared components
├── manage.py
└── requirements.txt

Key Highlights

Efficient Django ORM queries (select_related, prefetch_related, aggregate)

Clean Tailwind CSS design with full responsiveness

Interactive dashboard for quick event overview

Simple search functionality using query parameters

Future Improvements

Add user authentication for organizers

Add pagination for large event lists

Implement API endpoints with Django REST Framework

License

This project is licensed under the MIT License.
