FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "./monthly_challenges/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]