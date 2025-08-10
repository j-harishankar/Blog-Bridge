FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files before collectstatic
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "django_blog.wsgi:application", "--bind", "0.0.0.0:8080"]
