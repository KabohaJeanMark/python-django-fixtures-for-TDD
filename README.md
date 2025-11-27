# Django CRUD API with Django Fixtures

📘 Django CRUD API with Fixtures

📌 Overview

This project is a simple Django REST Framework CRUD API that demonstrates how to use Django fixtures to load sample data for development and automated tests.

Fixtures allow you to predefine database records in a JSON file so you can quickly spin up your project with consistent data or run tests without manually creating objects.

The project includes:
	•	A basic Item model
	•	Full CRUD API endpoints
	•	A fixture file (items.json) inside items/fixtures/
	•	Automated API tests that load fixtures before running

⸻

📂 Project Structure
```
django_fixtures/
│
├── items/
│   ├── fixtures/
│   │   └── items.json
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── django_fixtures/
│   └── settings.py
│
├── manage.py
└── README.md
```

⸻

🚀 Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/django_fixtures.git
cd django_fixtures
```

2️⃣ Create and activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate         # macOS / Linux
env\Scripts\activate            # Windows
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run database migrations
```bash
python manage.py migrate
```
5️⃣ Load fixtures (optional)

Load sample items into your database:
```bash
python manage.py loaddata items
```
or:
```bash
python manage.py loaddata items/fixtures/items.json
```

⸻

🧪 Running Tests

The project includes automated tests located in items/tests.py.
These tests use fixtures before each test runs.

Run all tests:
```bash
python manage.py test
```
What the tests check:
	•	GET /items/ returns the 2 fixture items
	•	POST /items/ successfully creates a new item
	•	Item count increases from 2 → 3

Fixture loading is done using:
```
fixtures = ['items.json']
```

Django automatically loads the JSON file from items/fixtures/.

⸻

📁 About Fixtures

Fixtures are JSON files that contain predefined database records.
Example (items.json):
```json
[
  {
    "model": "items.item",
    "pk": 1,
    "fields": {
      "name": "iPhone 16",
      "description": "Latest model",
      "price": 4500000
    }
  },
  {
    "model": "items.item",
    "pk": 2,
    "fields": {
      "name": "Samsung S24",
      "description": "Flagship Android",
      "price": 3800000
    }
  }
]
```

⸻

📡 API Endpoints

Method	Endpoint	Description
GET	/items/	List all items
POST	/items/	Create new item
GET	/items/<id>/	Retrieve single item
PUT	/items/<id>/	Update item
DELETE	/items/<id>/	Delete item


⸻

🛠 Technologies Used
	•	Django
	•	Django REST Framework
	•	Python 3.x
	•	SQLite (default)

⸻

📎 Useful Commands

Export your database to a fixture file:
```bash
python manage.py dumpdata items > items/fixtures/items.json
```
Reload fixtures:
```bash
python manage.py loaddata items
```

⸻

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/KabohaJeanMark/python-django-fixtures-for-TDD/issues/).

- Checkout to a feature branch and make your commits with descriptive messages here and raise a Pull Request
```
git checkout -b <ft-branch-name>
```

## Show your support

Give a ⭐️ if you like this project!

⸻