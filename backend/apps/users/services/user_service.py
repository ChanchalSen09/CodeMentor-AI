"""
User service layer - handles business logic.
"""

from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()


class UserService:
    """Service for user-related operations."""

    @staticmethod
    def get_user_profile(user_id):
        """Get user profile with caching."""
        cache_key = f"user_profile_{user_id}"
        profile = cache.get(cache_key)

        if not profile:
            try:
                user = User.objects.get(id=user_id)
                profile = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "bio": user.bio,
                    "avatar_url": user.avatar_url,
                }
                cache.set(cache_key, profile, 300)  # Cache for 5 minutes
            except User.DoesNotExist:
                return None

        return profile

    @staticmethod
    def update_user_profile(user_id, data):
        """Update user profile and invalidate cache."""
        try:
            user = User.objects.get(id=user_id)
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            user.save()

            # Invalidate cache
            cache_key = f"user_profile_{user_id}"
            cache.delete(cache_key)

            return user
        except User.DoesNotExist:
            return None
