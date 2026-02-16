"""
Custom middleware for CodeMentor-AI.
"""

import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LoggingMiddleware(MiddlewareMixin):
    """Log all requests with timing information."""

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, "start_time"):
            duration = time.time() - request.start_time
            logger.info(
                f"{request.method} {request.path} - {response.status_code} - {duration:.2f}s"
            )
        return response
