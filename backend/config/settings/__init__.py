"""
Django settings initialization.
"""

import os

environment = os.getenv("DJANGO_ENV", "dev")

if environment == "prod":
    from .prod import *  # noqa: F403, F401
else:
    from .dev import *  # noqa: F403, F401
