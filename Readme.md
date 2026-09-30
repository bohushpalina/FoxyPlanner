# FoxyPlanner

A web-based event planning and task management application built with Django, HTML, and CSS.

---

## Features

* **User Authentication:** Restricted access to personal event dashboards using Django authentication.
* **Event Management (CRUD):**
  * Create, view, update, and delete events.
  * User-specific event filtering ensuring users only access their own created schedules.
* **Responsive Web Interface:** Built-in HTML templates (`create_event.html`, `detail_view.html`, `delete_event.html`, `events_home.html`) located inside `events/templates/` and `main/templates/`.
* **Database Integration:** SQLite database backend pre-configured for rapid development.

---

## Project Structure

* `main/` — Application entry and general site pages (index, about, layout configuration).
* `events/` — Event management module:
  * `models.py` — `Articles` model storing event title, description, publication date, and foreign key to `User`.
  * `views.py` — Class-based views (`DetailView`, `UpdateView`, `DeleteView`) and functional view handles (`events_home`, `create_event`).
  * `forms.py` — Django form mapping for event creation and modification.
  * `urls.py` — URL routing configuration for event routes.
  * `templates/events/` — HTML rendering templates for event management pages.
* `notes/` — Auxiliary notes or planning module.

---

## Tech Stack

* **Backend Framework:** Django (Python 3.x)
* **Frontend:** HTML5, CSS3, Django Template Language (DTL)
* **Database:** SQLite3

---

## Getting Started

### Prerequisites

Ensure Python 3.8+ and `pip` are installed on your system.

### Installation & Setup

1. **Clone the repository:**
   ```
   git clone [https://github.com/bohushpalina/FoxyPlanner.git](https://github.com/bohushpalina/FoxyPlanner.git)
   cd FoxyPlanner
   ```


2. **Create and activate a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

3. **Install dependencies:**
```
pip install django

```

4. **Apply database migrations:**
```
python manage.py makemigrations
python manage.py migrate

```

5. **Create a superuser (optional, for Django admin access):**
```
python manage.py createsuperuser

```

6. **Run the development server:**
```
python manage.py runserver

```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Author

**Palina Bohush**

