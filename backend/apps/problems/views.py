"""
Problem views - API endpoints.
"""

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Problem
from .serializers import ProblemSerializer, SubmissionSerializer
from .services.problem_service import ProblemService


class ProblemListView(generics.ListAPIView):
    """List all problems."""

    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filters = {}
        if self.request.query_params.get("difficulty"):
            filters["difficulty"] = self.request.query_params.get("difficulty")
        if self.request.query_params.get("tags"):
            filters["tags"] = self.request.query_params.get("tags")

        return ProblemService.get_problems_list(filters)


class ProblemDetailView(generics.RetrieveAPIView):
    """Get problem details by slug."""

    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    queryset = Problem.objects.all()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_solution(request):
    """Submit solution for a problem."""
    problem_id = request.data.get("problem_id")
    code = request.data.get("code")
    language = request.data.get("language", "python")

    if not problem_id or not code:
        return Response(
            {"error": "problem_id and code are required"}, status=status.HTTP_400_BAD_REQUEST
        )

    submission = ProblemService.create_submission(request.user, problem_id, code, language)

    if submission:
        return Response(SubmissionSerializer(submission).data, status=status.HTTP_201_CREATED)

    return Response({"error": "Problem not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_submissions(request):
    """Get all submissions for current user."""
    submissions = ProblemService.get_user_submissions(request.user.id)
    serializer = SubmissionSerializer(submissions, many=True)
    return Response(serializer.data)
