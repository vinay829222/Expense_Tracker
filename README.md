💰 Expense Tracker (Django)

A simple and clean Django-based Expense Tracker that allows users to record, manage, and monitor their daily expenses.
Built using Django, SQLite, and basic HTML templates, this project provides an easy way to track and review daily spending.

✨ Features

➕ Add and save daily expenses
📋 View and manage existing expenses
📅 Track spending using dates
💾 Stores data in SQLite database
🧭 Simple and user-friendly UI

📁 Project Structure

ExpenceTracker/
│
├── expensetracker/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── expensetracker/        # Main Django project (settings, urls, wsgi)
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── tracker/               # Expense management app
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       ├── views.py
│       └── templates/
│
└── env/                       # Virtual environment (do NOT upload to GitHub)

🚀 Installation & Setup

1️⃣ Clone the Repository

```bash
git clone https://github.com/vinay829222/Expence_Tracker.git
cd ExpenceTracker/expensetracker
```

2️⃣ Create & Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate     # Windows
source env/bin/activate  # Linux / Mac
```

3️⃣ Install Dependencies

```bash
pip install django
```

4️⃣ Apply Migrations

```bash
python manage.py migrate
```

5️⃣ Start the Server

```bash
python manage.py runserver
```

Now open your browser and visit:
👉 http://127.0.0.1:8000/

📸 Screenshots

(Add screenshots here — optional)

🔮 Future Enhancements

   *👥 Add multiple user accounts
   *📉 Expense charts and visual reports
   *📤 Export data to CSV / PDF 
   *📱 Fully responsive UI

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss the update.

📜 License

This project is open-source and free to use.

👨‍💻 Author

Vinay Kumar
Feel free to connect or suggest improvements!
