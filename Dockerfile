# Use Python 3.12 with Debian Bullseye as the base image
FROM python:3.12-bullseye

# Prevents Python from buffering stdout and stderr (good for logging)
ENV PYTHONUNBUFFERED=1

# Disable Poetry's virtualenv creation
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VIRTUALENVS_IN_PROJECT=false

RUN apt update
RUN apt install gettext -y

# Create a directory for our application
RUN mkdir /code

# Set the working directory
WORKDIR /code

# Install poetry for dependency management
RUN pip install poetry

# Copy only dependency files first (good practice for layer caching)
COPY pyproject.toml poetry.lock ./

# # Keep container running indefinitely for debugging
# CMD ["tail", "-f", "/dev/null"]

# Copy the rest of the application code
COPY . .

# Install project dependencies
RUN poetry install --no-root

# Expose port 8000 (note: this is just documentation)
EXPOSE 8000

# Start the Django development server
ENTRYPOINT [ "poetry",  "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]