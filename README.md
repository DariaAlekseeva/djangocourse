# Article Management System

A Django-based web application for managing and tracking articles with their publishing status, word count, and social media integration.

## Features

- Article management with CRUD operations (Create, Read, Update, Delete)
- Automatic word count calculation for articles
- Article status tracking (Draft, In Progress, Published)
- Twitter post integration
- User authentication and authorization
- Modern and responsive web interface

## Tech Stack

- Python 3.12
- Django 5.0.7
- Poetry for dependency management
- Docker support
- Black for code formatting
- Pylint for code linting
- Django Debug Toolbar for development

## Prerequisites

- Python 3.12 or higher
- Poetry package manager
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-startup
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

## Docker Deployment

To run the application using Docker:

```bash
docker build -t article-management .
docker run -p 8005:8000 article-management
```

## Project Structure

- `app/` - Main Django application
  - `models.py` - Data models for Articles and User profiles
  - `views.py` - Class-based views for article operations
  - `admin.py` - Admin interface configuration
- `templates/app/` - HTML templates for the web interface
- `djangocourse/` - Project configuration
- `migrations/` - Database migration files

## Features in Detail

### Article Management
- Create new articles with title, content, and status
- Update existing articles
- Delete articles
- View all articles in a list format
- Automatic word count calculation

### Article Status
Articles can have one of three statuses:
- Draft
- In Progress
- Published

### Social Media Integration
- Twitter post field for social media content
- Separate content management for web and social media

## Development

The project uses several development tools:
- Black for code formatting (line length: 119)
- Pylint for code quality
- isort for import sorting
- pytest for testing
- Django Debug Toolbar for development insights

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]
