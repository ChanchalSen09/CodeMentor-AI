# CodeMentor-AI

> AI-powered DSA learning platform - Production-grade full-stack application

## 🚀 Features

- **Backend**: Django + DRF + PostgreSQL + Redis + Celery
- **Frontend**: React + TypeScript + Vite + Tailwind + Zustand
- **DevOps**: Docker + Docker Compose + GitHub Actions CI/CD
- **Authentication**: JWT-based authentication
- **Architecture**: Service layer pattern, feature-based frontend structure
- **Code Quality**: Pre-commit hooks, linting, formatting, type checking

## 📋 Prerequisites

- Docker & Docker Compose (recommended)
- OR:
  - Python 3.11+
  - Node.js 18+
  - PostgreSQL 15+
  - Redis 7+

## 🏃 Quick Start with Docker

The easiest way to run the entire stack:

```bash
# Clone the repository
git clone https://github.com/ChanchalSen09/CodeMentor-AI.git
cd CodeMentor-AI

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

The application will be available at:
- Frontend: http://localhost (port 80)
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin
- API Documentation: http://localhost:8000/api/docs/

## 🛠️ Local Development Setup

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/dev.txt

# Copy environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env

# Run development server
npm run dev
```

## 📁 Project Structure

```
CodeMentor-AI/
├── backend/
│   ├── apps/                    # Django applications
│   │   ├── users/              # User management & authentication
│   │   └── problems/           # DSA problems & submissions
│   ├── config/                 # Django settings & configuration
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   ├── core/                   # Core utilities & middleware
│   ├── requirements/           # Python dependencies
│   ├── tests/                  # Test suite
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── app/               # App configuration & store
│   │   ├── features/          # Feature-based modules
│   │   │   ├── home/
│   │   │   ├── auth/
│   │   │   └── problems/
│   │   ├── shared/            # Shared components
│   │   ├── services/          # API services
│   │   ├── hooks/             # Custom React hooks
│   │   └── types/             # TypeScript types
│   ├── index.html
│   ├── vite.config.ts
│   └── package.json
├── .github/
│   └── workflows/             # GitHub Actions CI/CD
│       ├── backend-ci.yml
│       └── frontend-ci.yml
├── docker-compose.yml
├── Makefile
├── .pre-commit-config.yaml
└── README.md
```

## 🧪 Testing

### Run All Tests

```bash
make test
```

### Backend Tests

```bash
cd backend
pytest
pytest --cov=. --cov-report=html  # With coverage
```

### Frontend Tests

```bash
cd frontend
npm run build  # Type checking and build
npm run type-check
```

## 🎨 Code Quality

### Linting

```bash
# Lint all
make lint

# Backend only
make lint-backend

# Frontend only
make lint-frontend
```

### Formatting

```bash
# Format all
make format

# Backend only
make format-backend

# Frontend only
make format-frontend
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check code quality:

```bash
make setup-precommit
```

## 📊 Available Make Commands

```bash
make help                 # Show all available commands
make install             # Install all dependencies
make run-dev             # Run development servers
make docker-up           # Start Docker services
make docker-down         # Stop Docker services
make test                # Run all tests
make lint                # Run all linters
make format              # Format all code
make migrate             # Run database migrations
make clean               # Clean build artifacts
```

## 🔐 Environment Variables

### Backend (.env)

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ENV=dev
POSTGRES_DB=codementor
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
REDIS_URL=redis://redis:6379/1
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend (.env)

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

## 🏗️ Architecture

### Backend Architecture

- **Service Layer Pattern**: Business logic separated from views
- **Django REST Framework**: RESTful API
- **JWT Authentication**: Secure token-based auth
- **PostgreSQL**: Primary database
- **Redis**: Caching & Celery broker
- **Celery**: Async task processing

### Frontend Architecture

- **Feature-based Structure**: Organized by features, not file types
- **Zustand**: Lightweight state management
- **Axios**: HTTP client with interceptors
- **TypeScript**: Strict type checking
- **Tailwind CSS**: Utility-first styling

## 🚀 Deployment

### Production Checklist

- [ ] Set strong `DJANGO_SECRET_KEY`
- [ ] Set `DJANGO_ENV=prod`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper `CORS_ALLOWED_ORIGINS`
- [ ] Use production database credentials
- [ ] Enable SSL/HTTPS
- [ ] Set up monitoring (Sentry)
- [ ] Configure proper logging
- [ ] Set up backups
- [ ] Use production-grade web server (Gunicorn + Nginx)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make test && make lint`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 API Documentation

API documentation is available at:
- Swagger UI: http://localhost:8000/api/docs/
- OpenAPI Schema: http://localhost:8000/api/schema/

### Key Endpoints

- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/login/` - User login
- `GET /api/v1/auth/profile/` - Get user profile
- `GET /api/v1/problems/` - List problems
- `GET /api/v1/problems/{slug}/` - Get problem details
- `POST /api/v1/problems/submit/` - Submit solution
- `GET /api/v1/health/` - Health check

## 🔧 Troubleshooting

### Docker Issues

```bash
# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Database Issues

```bash
# Reset database
docker-compose down -v
docker-compose up -d
```

### Port Conflicts

If ports are already in use, modify the port mappings in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Backend
  - "8080:80"    # Frontend
```

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- ChanchalSen09

## 🙏 Acknowledgments

- Built with Django, React, and modern DevOps practices
- Designed for scalability and maintainability
- Production-ready architecture

---

Made with ❤️ for developers learning DSA
