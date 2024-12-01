# django-alpine

A Django package to easily include [Alpine.js](https://pypi.org/project/django-alpine/) in your Django project.

## Features

- Automatically adds Alpine.js to your Django project.
- Ensures Alpine.js is available in your `static/js` directory.
- Falls back to a pre-packaged version of Alpine.js if CDN download fails.

## Installation

### Requirements

- Python >= 3.10
- Django >= 4.2

### Installation Steps

1. Install the package using pip:

   ```bash
   pip install django-alpine
   ```

2. Add `django_alpine` to your `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # Other apps
       'django_alpine',
   ]
   ```

3. Run the `collectstatic` command to include Alpine.js in your static files:

   ```bash
   python manage.py collectstatic
   ```

## Usage

In your templates, you can load the Alpine.js script using the provided template tag.

### Example:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Django Project</title>
</head>
<body>
    <!-- Include Alpine.js -->
    <script src="{% static 'js/alpine.js' %}" defer></script>

    <!-- Your HTML content -->
</body>
</html>
```

## How It Works

1. On installation, the package:
   - Copies a pre-packaged Alpine.js file to your `static/js` directory.
   - Attempts to download the latest version of Alpine.js from the official CDN.

2. If the CDN is unavailable, the pre-packaged version will be used.

## Development and Contribution

Contributions are welcome! Follow the steps below to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/ProKelly/django-alpine.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make your changes and submit a pull request.

## License

This project is licensed under the BSD License. See the [LICENSE](LICENSE) file for details.

## Author

Created and maintained by **Anye Prince Kelly**.

- Email: [firstanye@gmail.com](mailto:firstanye@gmail.com)
- GitHub: [ProKelly](https://github.com/ProKelly)

## Links

- [Alpine.js Documentation](https://alpinejs.dev/)
- [GitHub Repository](https://github.com/ProKelly/django-alpine)

