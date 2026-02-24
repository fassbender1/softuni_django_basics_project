
# 🎬 CineManager

---

A Django-based web application for managing Movies, Cast & Crew, and Studios.
Built as a final project for the SoftUni Django Basics Regular Exam (February 2026).

---

📌 Project Overview

CineManager is a film production management system that allows users to:

Manage Movies (full CRUD)

Manage Actors, Directors, and Writers (full CRUD)

Manage Studios (full CRUD)

Associate movies with cast, crew, and studios

Filter and sort movie data

View special rankings (Top 5 Highest Budget Movies, Top 5 Highest Paid Actors)

Navigate through a consistent Bootstrap-based UI

View a custom 404 error page

⚠ Authentication is intentionally excluded as per exam requirements.

Movies

Full CRUD operations: Create, Read, Update, Delete movies.

Views: List views, detail views, and delete confirmation pages.

Filtering: Filter movies by Status: Pre-Production, Filming, Post-Production, Released.

Search: Search movies by title.

Top Budget Movies: Display the top 5 highest budget movies.

Actors, Directors, and Writers

Full CRUD operations: Proper forms, data validations, and confirmation before deletion.

Search: Search cast & crew by name.

Top Paid Actors: Display the top 5 highest paid actors based on salary.

Studios

Full CRUD operations: Add, view, edit, and delete studios.

Search: Search studios by name.

General Features

Consistent UI Design: Bootstrap-based templates, reusable cards, lists, and partial templates.

Navigation: Fully linked pages with consistent headers and footers.

Error Handling: Custom 404 error page.

Media Management: Upload and display images for movie posters, studio logos, and person profile images.  
*(The project archive and repository already include media files, that can be used to avoid having to search for images.)*

---

🏗 Project Architecture

The project consists of four Django apps:

1️⃣ common

Home page

Base template

Custom 404 middleware

Shared components and layout (Search Mixin functionality as well as form that are used by the other apps, as well as Movie Genre and Movie Status choices )

2️⃣ movies

Movie model

Full CRUD functionality

Status filtering

Highest Budget Movies page

Many-to-many relations with cast & crew

Many-to-one relation with Studio

3️⃣ people

Actor model

Director model

Writer model

Full CRUD for each

Highest Paid Actors page

4️⃣ studios

Studio model

Full CRUD

Relation with Movies (ForeignKey reverse access)

🗄 Database Design

✔ Models

Movie

Actor

Director

Writer

Studio

✔ Relationships

Many-to-Many

Movie ↔ Actor

Movie ↔ Director

Movie ↔ Writer

Many-to-One

Movie → Studio (ForeignKey)

✔ Additional Features

Slug fields for clean URLs

Status choices using Django TextChoices

Reverse relationship usage in templates

Proper related_name usage

---

🧾 Forms & Validation

The project includes multiple forms with:

Custom labels

Help texts

Placeholder styling

Field exclusions

Read-only/disabled fields (in delete confirmations)

Custom validation messages

Confirmation page before deletion

Forms correctly handle:

GET and POST requests

Validation

Redirects after successful submission

---

📄 Pages & Templates

The application contains more than 10 templates, including:

Core Pages

Home (/)

Movie List (/movies/)

Movie Detail

Movie Create

Movie Edit

Movie Delete

Highest Budget Movies (/movies/highest-budget/)

Actors List

Actors Detail

Actors Create

Actors Edit

Actors Delete

Highest Paid Actors (/cast-and-crew/actors/highest-paid/)

Directors List

Directors Detail

Directors Create

Directors Edit

Directors Delete

Writers List

Writers Detail

Writers Create

Writers Edit

Writers Delete

Studios List

Studios Detail

Studios Create

Studios Edit

Studios Delete


Custom 404 Page

Template Features

Base template (not counted in 10)

Template inheritance

Reusable partials (cards, navigation)

Bootstrap-based design with many additional manual tweaks

Dynamic database rendering

Status filtering dropdown

Navigation links across all pages

Consistent footer

All pages are accessible through navigation.

No orphan routes.

---

🔍 Filtering & Extra Functionality

Movie Filtering

Filter by Status:

Pre-Production

Filming

Post-Production

Released

Other

Rankings

Top 5 Highest Budget Movies

Top 5 Highest Paid Actors

These features demonstrate advanced queryset usage and sorting.

---

⚙️ Installation & Setup

1️⃣ Clone Repository

git clone <your-github-link>

cd softuni_django_basics_project

2️⃣ Create Virtual Environment

python -m venv .venv

source .venv/bin/activate   # macOS/Linux

.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Environment Variables


The full project is available as a downloadable archive in the repository (CineManager.zip).

Create a .env file in the root directory (same level as manage.py).

Example:

SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=softuni_django_basics_project

DB_USER=postgres

DB_PASSWORD=your_password

DB_HOST=127.0.0.1

DB_PORT=5432

⚠ The .env file is not included in the repository for security reasons.

5️⃣ PostgreSQL Setup

Create a PostgreSQL database:

Database name: softuni_django_basics_project

Then run:

python manage.py migrate

python manage.py runserver

Application runs at:

http://127.0.0.1:8000/

---

🧠 OOP & Code Quality

The project follows:

Separation of concerns (apps by responsibility)

CBVs for structured logic

Encapsulation via model methods

TextChoices for abstraction

Reusable mixins

Clean naming conventions

Strong cohesion & loose coupling

---

🔗 Application URLs

Home
- `/`

Movies
- `/movies/`
- `/movies/highest-budget/`
- `/movies/create-movie/`
- `/movies/<slug>/`
- `/movies/<slug>/edit/`
- `/movies/<slug>/delete/`
- `/movies/<slug>/delete/confirm/`

Cast & Crew
- `/cast-and-crew/`

Actors
- `/cast-and-crew/actors/`
- `/cast-and-crew/actors/highest-paid/`
- `/cast-and-crew/actors/create/`
- `/cast-and-crew/actors/<slug>/`
- `/cast-and-crew/actors/<slug>/edit/`
- `/cast-and-crew/actors/<slug>/delete/`

Directors
- `/cast-and-crew/directors/`
- `/cast-and-crew/directors/create/`
- `/cast-and-crew/directors/<slug>/`
- `/cast-and-crew/directors/<slug>/edit/`
- `/cast-and-crew/directors/<slug>/delete/`

Writers
- `/cast-and-crew/writers/`
- `/cast-and-crew/writers/create/`
- `/cast-and-crew/writers/<slug>/`
- `/cast-and-crew/writers/<slug>/edit/`
- `/cast-and-crew/writers/<slug>/delete/`

Studios
- `/studios/`
- `/studios/create/`
- `/studios/<slug>/`
- `/studios/<slug>/edit/`
- `/studios/<slug>/delete/`

---

🛠 Technologies Used

Python

Django (latest stable version)

PostgreSQL

Bootstrap 5

More in requirements.txt file

Git & GitHub

---

📊 Assessment Criteria Coverage

✔ 3+ Django apps

✔ 3+ models

✔ M2M and FK relationships

✔ 3+ forms with validation

✔ 10+ templates

✔ Full CRUD for multiple models

✔ Filtering & sorting

✔ Custom 404 page

✔ PostgreSQL

✔ GitHub repository

✔ Clean architecture

---

📌 Notes

Authentication intentionally excluded as required.

No AI-generated backend logic.

Original project concept and implementation.

