# django_alpine/apps.py
import os
import requests
from django.apps import AppConfig
from django.conf import settings
import shutil


class AlpineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_alpine'
    label = 'alpine'

    def ready(self):
        """Ensure Alpine.js is available in the static folder on app initialization."""
        static_dir = os.path.join(settings.BASE_DIR, "static", "js")
        packaged_alpine_path = os.path.join(os.path.dirname(__file__), "static", "js", "alpine.js")
        alpine_js_path = os.path.join(static_dir, "alpine.js")
        os.makedirs(static_dir, exist_ok=True)

        # Copy the pre-packaged Alpine.js file
        self.copy_packaged_alpine(packaged_alpine_path, alpine_js_path)

        # Attempt to download and override with the latest Alpine.js from the CDN
        self.download_alpine(alpine_js_path)

    @staticmethod
    def copy_packaged_alpine(source_path, destination_path):
        """Copy the pre-packaged Alpine.js file to the static directory."""
        try:
            shutil.copy(source_path, destination_path)
            print(f"Packaged Alpine.js installed to {destination_path}.")
        except Exception as e:
            print(f"Failed to download packaged Alpine.js: {e}")

    @staticmethod
    def download_alpine(file_path):
        """Attempt to download Alpine.js from the CDN and override the pre-packaged file."""
        url = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"
        try:
            print("Attempting to download latest version of Alpine.js...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Alpine.js successfully downloaded in {file_path}.")
        except requests.RequestException as e:
            print(f"Failed to download Alpine.js: {e}. Using the pre-packaged version.")
