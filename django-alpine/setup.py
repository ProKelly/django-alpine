import os
from setuptools import setup, find_packages

# Read requirements from the requirements.txt file
def parse_requirements(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    print("No requirements found")
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
)
