

# Django Blog

A simple blog application built with Django.
**Live Demo:** [https://django-blog-app-743225501073.asia-south1.run.app](https://django-blog-app-743225501073.asia-south1.run.app)

---

## Features

* User authentication (register, login, logout)
* Create, edit, and delete blog posts
* Comment on posts
* Responsive UI using HTML templates
* Admin panel for managing posts and users

---

## Deployment

This application is **dockerized** and deployed on Google Cloud Run for easy, scalable hosting.

* The app runs inside a Docker container using Gunicorn as the production server.
* Static files are collected and served properly inside the container.
* Deployment is automated with Google Cloud Build and Cloud Run for seamless updates.

---

## Setup Instructions (Local Development)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/j-harishankar/django-blog.git
   cd django-blog
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Visit the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

---

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes.
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

---

This way, users understand your app is dockerized and deployed live, but they also have instructions to run it locally.

Want me to help you draft a short Docker usage section too?
