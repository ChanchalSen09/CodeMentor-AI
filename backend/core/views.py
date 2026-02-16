"""
Core views for health checks and utilities.
"""

from django.core.cache import cache
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check endpoint to verify service status.
    """
    health_status = {
        "status": "healthy",
        "database": "unknown",
        "cache": "unknown",
    }

    # Check database
    try:
        connection.ensure_connection()
        health_status["database"] = "connected"
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["database"] = f"error: {str(e)}"

    # Check cache
    try:
        cache.set("health_check", "ok", 10)
        if cache.get("health_check") == "ok":
            health_status["cache"] = "connected"
        else:
            health_status["cache"] = "error"
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["cache"] = f"error: {str(e)}"

    return Response(health_status)
