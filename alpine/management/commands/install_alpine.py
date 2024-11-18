# alpine/management/commands/install_alpine.py
import os
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Install the latest version of Alpine.js into the Django project"

    def handle(self, *args, **kwargs):
        url = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"
        static_dir = os.path.join("static", "js")
        os.makedirs(static_dir, exist_ok=True)
        file_path = os.path.join(static_dir, "alpine.min.js")
        
        self.stdout.write("Downloading the latest version of Alpine.js...")
        response = requests.get(url)
        response.raise_for_status()  # Raise error if download fails
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        self.stdout.write(f"Alpine.js has been downloaded to {file_path}.")
