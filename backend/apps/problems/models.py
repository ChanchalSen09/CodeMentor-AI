"""
Problem models.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Problem(models.Model):
    """DSA Problem model."""

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    tags = models.JSONField(default=list)
    examples = models.JSONField(default=list)
    constraints = models.TextField()
    starter_code = models.TextField()
    solution = models.TextField(blank=True)
    hints = models.JSONField(default=list)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems_created")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "problems"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Submission(models.Model):
    """User submission for a problem."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("wrong_answer", "Wrong Answer"),
        ("error", "Error"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="submissions")
    code = models.TextField()
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    runtime = models.IntegerField(null=True, blank=True)
    memory = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "submissions"
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"
