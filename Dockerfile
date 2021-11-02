FROM python:3.8

# Export env variables.
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Copy requirements
COPY requirements.txt .

# Installing requirements
RUN pip install -r requirements.txt

# Copy everything
COPY . /app

WORKDIR /app

EXPOSE 5000


