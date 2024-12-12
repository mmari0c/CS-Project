from app import app as application  # Replace 'app' with your main Flask module name if different.

import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.append(project_dir)

# The WSGI server uses the `application` object to run the app.
