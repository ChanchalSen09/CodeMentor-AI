"""
Problem serializers.
"""
from rest_framework import serializers
from .models import Problem, Submission


class ProblemSerializer(serializers.ModelSerializer):
    """Serializer for Problem model."""
    
    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'slug', 'description', 'difficulty',
            'tags', 'examples', 'constraints', 'starter_code',
            'hints', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class SubmissionSerializer(serializers.ModelSerializer):
    """Serializer for Submission model."""
    problem_title = serializers.CharField(source='problem.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Submission
        fields = [
            'id', 'problem', 'problem_title', 'username', 'code',
            'language', 'status', 'runtime', 'memory',
            'error_message', 'submitted_at'
        ]
        read_only_fields = ['id', 'user', 'status', 'runtime', 'memory', 'error_message', 'submitted_at']
