.PHONY: help install run-dev run-prod test lint format clean docker-up docker-down docker-logs migrate

help:
	@echo "CodeMentor-AI - Makefile Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Install all dependencies"
	@echo "  make install-backend  Install backend dependencies"
	@echo "  make install-frontend Install frontend dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make run-dev          Run development servers (backend + frontend)"
	@echo "  make run-backend      Run backend development server"
	@echo "  make run-frontend     Run frontend development server"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-up        Start all services with Docker Compose"
	@echo "  make docker-down      Stop all Docker services"
	@echo "  make docker-logs      View Docker logs"
	@echo "  make docker-build     Rebuild Docker images"
	@echo ""
	@echo "Testing:"
	@echo "  make test             Run all tests"
	@echo "  make test-backend     Run backend tests"
	@echo "  make test-frontend    Run frontend tests"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             Run all linters"
	@echo "  make lint-backend     Run backend linters"
	@echo "  make lint-frontend    Run frontend linters"
	@echo "  make format           Format all code"
	@echo "  make format-backend   Format backend code"
	@echo "  make format-frontend  Format frontend code"
	@echo ""
	@echo "Database:"
	@echo "  make migrate          Run database migrations"
	@echo "  make makemigrations   Create new migrations"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean            Clean build artifacts"
	@echo "  make setup-precommit  Install pre-commit hooks"

install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements/dev.txt

install-frontend:
	cd frontend && npm install

run-dev:
	@echo "Starting development servers..."
	@make -j2 run-backend run-frontend

run-backend:
	cd backend && python manage.py runserver

run-frontend:
	cd frontend && npm run dev

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-build:
	docker-compose build --no-cache

test: test-backend test-frontend

test-backend:
	cd backend && pytest

test-frontend:
	cd frontend && npm run build

lint: lint-backend lint-frontend

lint-backend:
	cd backend && ruff check .
	cd backend && flake8 .
	cd backend && black --check .
	cd backend && isort --check-only .

lint-frontend:
	cd frontend && npm run lint
	cd frontend && npm run type-check

format: format-backend format-frontend

format-backend:
	cd backend && black .
	cd backend && isort .

format-frontend:
	cd frontend && npm run format

migrate:
	cd backend && python manage.py migrate

makemigrations:
	cd backend && python manage.py makemigrations

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	cd frontend && rm -rf dist node_modules

setup-precommit:
	pip install pre-commit
	pre-commit install
