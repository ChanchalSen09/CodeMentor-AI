"""
Problems URL patterns.
"""

from django.urls import path

from .views import ProblemDetailView, ProblemListView, get_user_submissions, submit_solution

urlpatterns = [
    path("", ProblemListView.as_view(), name="problem-list"),
    path("<slug:slug>/", ProblemDetailView.as_view(), name="problem-detail"),
    path("submit/", submit_solution, name="submit-solution"),
    path("submissions/", get_user_submissions, name="user-submissions"),
]
