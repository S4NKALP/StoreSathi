# StoreSathi

A Django project folder structure is generated with [djinitx/djinit/dj](https://github.com/S4NKALP/djinit).

## Features

- Modern project structure with environment-specific settings
- Pre-configured REST API with JWT authentication
- Essential dependencies and utilities
- Production-ready configuration

## Setup

### Using Just (Recommended)

1. Set environment variables in `.env` file

2. Run setup (installs dependencies, runs migrations, creates superuser):

   ```bash
   just setup
   ```

3. Start development server:
   ```bash
   just dev
   ```

### Traditional Method

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables in `.env` file

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Create superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Start development server:
   ```bash
   python manage.py runserver
   ```

## Available Commands

Run `just` to see all available commands, including:

- `just dev` - Run development server
- `just migrate` - Run migrations
- `just makemigrations` - Create migrations
- `just createsuperuser` - Create superuser
- `just test` - Run tests
- `just lint` - Lint code
- `just format` - Format code
- `just shell` - Django shell
- `just clean` - Clean cache files
- `just install <package>` - Install package
- `just remove <package>` - Remove package
- `just server` - Run production server
- `just ci` - Run all linting and checks
- `just test-coverage` - Run tests with coverage

## Project Structure

```
config/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── admin/
│   ├── api/              # API endpoints organized by model
│   │   ├── user/         # Example: if you have a User model
│   │   │   ├── views.py
│   │   │   ├── serializers.py
│   │   │   └── urls.py
│   │   └── urls.py
│   ├── models/           # Django models
│   ├── tests/
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .env.sample
└── README.md

**Note:** For the single folder layout, organize your API endpoints by model name under the `api/` directory.
For example, if you have a `User` model in `models/user.py`, create:
- `api/user/views.py` - API views for User
- `api/user/serializers.py` - Serializers for User
- `api/user/urls.py` - URL patterns for User endpoints

See the README files in `api/` and `models/` directories for more details.
```

## API Documentation

When running in development mode, API documentation is available at:

- Swagger UI: http://localhost:8000/docs/
- Schema: http://localhost:8000/schema/
