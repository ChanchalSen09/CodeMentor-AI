"""
Development settings.
"""

from .base import *  # noqa: F403, F401

DEBUG = True

ALLOWED_HOSTS = ["*"]

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
