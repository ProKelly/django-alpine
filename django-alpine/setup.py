import os
import shutil
import requests
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation script to download Alpine.js."""

    def run(self):
        super().run()

        # Define paths
        static_dir = os.path.join(os.getcwd(), "static", "js")
        packaged_alpine_path = os.path.join(os.path.dirname(__file__), "django_alpine", "static", "js", "alpine.js")
        alpine_js_path = os.path.join(static_dir, "alpine.js")
        os.makedirs(static_dir, exist_ok=True)

        # Copy the pre-packaged Alpine.js file
        self.copy_packaged_alpine(packaged_alpine_path, alpine_js_path)

        # Attempt to download the latest Alpine.js
        self.download_alpine(alpine_js_path)

    @staticmethod
    def copy_packaged_alpine(source_path, destination_path):
        try:
            shutil.copy(source_path, destination_path)
            print(f"Packaged Alpine.js installed to {destination_path}.")
        except Exception as e:
            print(f"Failed to copy packaged Alpine.js: {e}")

    @staticmethod
    def download_alpine(file_path):
        url = "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"
        try:
            print("Attempting to download latest version of Alpine.js...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Alpine.js successfully downloaded to {file_path}.")
        except requests.RequestException as e:
            print(f"Failed to download Alpine.js: {e}. Using the pre-packaged version.")

# Parse requirements
def parse_requirements(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    return []

setup(
    name="django-alpine",
    version="0.1.1",
    description="A Django app for integrating Alpine.js into your project.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Anye Prince Kelly",
    author_email="firstanye@gmail.com",
    url="https://github.com/ProKelly/django-alpine.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.1.3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        "install": PostInstallCommand,
    },
)
