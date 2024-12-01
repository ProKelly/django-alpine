django-alpine Usage Documentation
=================================

Overview
--------

``django-alpine`` is a Django package that simplifies the integration of Alpine.js into your Django project. It handles the automatic downloading and inclusion of Alpine.js in your Django project's static files, ensuring a smooth setup with minimal configuration.

Features
--------

- Automatically downloads the latest Alpine.js from a CDN into your ``static/js`` directory.
- Ensures Alpine.js is included in your Django templates with a simple template tag.
- Integrates seamlessly with Django's ``INSTALLED_APPS``.

Installation
------------

### Prerequisites

Ensure your environment meets the following requirements:

- **Python**: 3.10 or higher
- **Django**: 5.1.3 or higher

### Steps

1. Install the package via pip:

   .. code-block:: bash

      pip install django-alpine

2. Add ``django_alpine`` to your ``INSTALLED_APPS`` in ``settings.py``:

   .. code-block:: python

      INSTALLED_APPS = [
          ...,
          'django_alpine',
      ]


3. Collect static files to ensure the downloaded ``alpine.js`` is included in your static files directory:

   .. code-block:: bash

      python manage.py collectstatic

Usage
-----

Automatic Alpine.js Download
----------------------------

Once you add ``django_alpine`` to ``INSTALLED_APPS``, the app's ``ready`` method will automatically download the latest version of Alpine.js into your static files directory (``static/js/alpine.js``).

If the file already exists, it won't download it again unless the version has changed. This ensures your static files are kept up-to-date without redundant downloads.

Template Integration
--------------------

Using the Template Tag
----------------------

The package provides a custom template tag to include Alpine.js in your HTML templates. Use the ``{% load alpine_tags %}`` tag to include Alpine.js dynamically.

1. Load the template tags in your HTML file:

   .. code-block:: html

      {% load alpine_tags %}

2. Add the ``include_alpine`` tag in the ``<head>`` or before your closing ``<body>`` tag:

   .. code-block:: html

      {% include_alpine %}

This will inject the following ``<script>`` tag into your HTML:

.. code-block:: html

   <script src="/static/js/alpine.js" defer></script>


Manual Script Inclusion (Optional)
----------------------------------

If you prefer to include the Alpine.js script tag manually, ensure the static files have been collected using ``python manage.py collectstatic``. Then, include it directly:

.. code-block:: html

   <script src="{% static 'js/alpine.js' %}" defer></script>

Updating Alpine.js
------------------

To update Alpine.js to the latest version:

1. Remove the existing file (``static/js/alpine.js``) manually or via a script.
2. Restart your Django server. The ``django_alpine`` app will detect the missing file and download the latest version.

Uninstallation
--------------

To remove ``django-alpine``:

1. Uninstall the package:

   .. code-block:: bash

      pip uninstall django-alpine

2. Remove ``django_alpine`` from your ``INSTALLED_APPS`` in ``settings.py``.

3. (Optional) Delete the ``static/js/alpine.js`` file.

Development and Contribution
----------------------------

Contributions are welcome! Follow these steps to contribute:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/ProKelly/django-alpine.git


2. Create a virtual environment and install dependencies:

   .. code-block:: bash

      python -m venv env
      source env/bin/activate  # On Windows: .\env\Scripts\activate
      pip install -r requirements.txt

3. Test your changes by running the Django project locally.

License
-------
``django-alpine`` is licensed under the **BSD License**. See the ``LICENSE`` file for more details.

Troubleshooting
---------------

Error: Alpine.js Not Found
--------------------------

- Ensure ``python manage.py collectstatic`` has been run.
- Verify that ``django_alpine`` is added to your ``INSTALLED_APPS``.

Error: Static Files Not Loading
-------------------------------

- Confirm your ``STATICFILES_DIRS`` and ``STATIC_ROOT`` settings are correctly configured.
- Ensure the web server serving your application is configured to serve static files.

Contact
-------
For further support, feel free to contact:

- **Name**: Anye Prince Kelly
- **Email**: firstanye@gmail.com
- **Repository**: `GitHub Repository <https://github.com/ProKelly/django-alpine>`_

This documentation ensures you can effectively integrate and use ``django-alpine`` in your projects. Happy coding!
