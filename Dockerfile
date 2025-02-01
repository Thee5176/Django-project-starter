# Pull base image
FROM python:3.12.3-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt
RUN apt-get update && apt-get install -y gettext

# Copy project
COPY . .