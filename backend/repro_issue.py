import os
import django
from django.conf import settings
from django.db import connections

# Manually configure settings if not already configured
if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

print("DATABASES setting:", settings.DATABASES)

try:
    for alias, settings_dict in connections.settings.items():
        print(f"Checking alias: {alias}")
        print(f"ATOMIC_REQUESTS present? {'ATOMIC_REQUESTS' in settings_dict}")
        val = settings_dict["ATOMIC_REQUESTS"]
        print(f"Value: {val}")
    print("SUCCESS: ATOMIC_REQUESTS key found.")
except KeyError as e:
    print(f"FAILURE: KeyError encountered: {e}")
except Exception as e:
    print(f"FAILURE: Other error: {e}")
