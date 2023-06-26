# Set the base image to Ubuntu
FROM ubuntu:latest

# Update the package list and install PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib

# Create a new user for PostgreSQL
RUN useradd -ms /bin/bash postgres

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies

# Copy the rest of the application code into the container
COPY . .

# Expose the port used by Django
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
