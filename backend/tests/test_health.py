"""
Tests for health check endpoint.
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestHealthCheck:
    """Test health check endpoint."""

    def test_health_check_returns_200(self):
        """Test that health check endpoint returns 200."""
        client = APIClient()
        url = reverse("health-check")
        response = client.get(url)

        assert response.status_code == 200
        assert "status" in response.data
        assert response.data["status"] in ["healthy", "unhealthy"]
