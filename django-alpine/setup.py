from setuptools import setup, find_packages

# Read requirements from the requirements.txt file
def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

setup(
    name="django-alpine",
    version="0.1.0",
    description="A Django app for integrating Alpine.js into your project.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Anye Prince Kelly",
    author_email="firstanye@gmail.com",
    url="https://github.com/ProKelly/django-alpine.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Ind ependent",
    ],
)



