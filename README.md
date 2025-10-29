# LabSky – Professional Medical Laboratory Website

![LabSky Logo](static/img/logo.png)

> **A trusted medical laboratory with advanced equipment, expert physicians, and a modern online platform.**

A fully responsive **medical laboratory website** built with **Django**, **Bootstrap 5**, full **Persian (RTL)** support, and secure **user authentication**.

---

## Features

| Feature | Status |
|--------|--------|
| Clean, professional & responsive design | Done |
| Full Persian RTL + Vazirmatn font | Done |
| User registration & login system | Done |
| Secure logout with redirect to home | Done |
| Success/error messages (Django Messages) | Done |
| Styled forms with icons & validation | Done |
| Dynamic navbar (login/logout conditional) | Done |
| **No dashboard** (as requested) | Done |
| Mobile & tablet optimized | Done |

---

## Screenshots *(Add later)*

| Page | Preview |
|------|--------|
| Home | `screenshots/home.png` |
| Login | `screenshots/login.png` |
| Register | `screenshots/register.png` |

---

## Project Structure
LabSky/
├── config/                 # Django settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # Authentication app
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/registration/
│       ├── login.html
│       └── register.html
├── main/                   # Main pages
│   ├── views.py
│   └── urls.py
├── templates/
│   └── base.html           # Main layout (navbar, footer, RTL)
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── lib/                # Bootstrap, Owl Carousel, Animate.css
└── manage.py

---

## Requirements

- Python 3.8+
- Django 5.2+
- Bootstrap 5 (CDN or local)
- Font Awesome & Bootstrap Icons

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/labsky.git
cd labsky

2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# or
venv\Scripts\activate           # Windows

3. Install dependencies
bashpip install django
5. (Optional) Create admin user
bashpython manage.py createsuperuser
6. Start the server
bashpython manage.py runserver
Visit: http://127.0.0.1:8000

Usage
Action,URL
Home,/
Login,/accounts/login/
Register,/accounts/register/
Logout,/accounts/logout/

Testing the Flow

Go to Register → create an account
Login with your credentials
Redirected to Home
Navbar shows: Username + Logout
Click Logout → back to home


Customization

Logo: Replace static/img/logo.png
Colors & Styles: Edit static/css/style.css
Add Pages: Extend templates/base.html
Add Dashboard Later: Create dashboard/ view & URL


Contributing

Fork the repo
Create a branch: git checkout -b feature/new-page
Commit: git commit -m "Add new feature"
Push: git push origin feature/new-page
Open a Pull Request


License
MIT License – Free to use, modify, and distribute.

Contact

Developer: [Your Name]
Email: your.email@example.com
Live Demo: labsky.example.com



LabSky – Accuracy. Care. Trust.