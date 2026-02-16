"""
Problem service layer - handles business logic.
"""

from django.core.cache import cache

from ..models import Problem, Submission


class ProblemService:
    """Service for problem-related operations."""

    @staticmethod
    def get_problems_list(filters=None):
        """Get list of problems with optional filters."""
        queryset = Problem.objects.all()

        if filters:
            if "difficulty" in filters:
                queryset = queryset.filter(difficulty=filters["difficulty"])
            if "tags" in filters:
                queryset = queryset.filter(tags__contains=filters["tags"])

        return queryset

    @staticmethod
    def get_problem_by_slug(slug):
        """Get problem by slug with caching."""
        cache_key = f"problem_{slug}"
        problem = cache.get(cache_key)

        if not problem:
            try:
                problem = Problem.objects.get(slug=slug)
                cache.set(cache_key, problem, 600)  # Cache for 10 minutes
            except Problem.DoesNotExist:
                return None

        return problem

    @staticmethod
    def create_submission(user, problem_id, code, language):
        """Create a new submission."""
        try:
            problem = Problem.objects.get(id=problem_id)
            submission = Submission.objects.create(
                user=user, problem=problem, code=code, language=language, status="pending"
            )
            # In production, trigger async task to evaluate submission
            return submission
        except Problem.DoesNotExist:
            return None

    @staticmethod
    def get_user_submissions(user_id):
        """Get all submissions for a user."""
        return Submission.objects.filter(user_id=user_id)
