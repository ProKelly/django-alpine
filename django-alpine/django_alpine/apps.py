# django_alpine/apps.py
import os
import requests
from django.apps import AppConfig
from django.conf import settings


class AlpineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_alpine'
    label = 'alpine'

    def ready(self):
        """Ensure Alpine.js is downloaded to the static folder on app initialization."""
        static_dir = os.path.join(settings.BASE_DIR, "static", "js")
        alpine_js_path = os.path.join(static_dir, "alpine.js")
        if not os.path.exists(alpine_js_path):
            self.download_alpine(static_dir, alpine_js_path)

    @staticmethod
    def download_alpine(static_dir, file_path):
        """Download Alpine.js to the static directory."""
        url = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"
        os.makedirs(static_dir, exist_ok=True)
        try:
            print("Downloading Alpine.js...")
            response = requests.get(url)
            response.raise_for_status()
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Alpine.js downloaded to {file_path}.")
        except requests.RequestException as e:
            print(f"Failed to download Alpine.js: {e}")
