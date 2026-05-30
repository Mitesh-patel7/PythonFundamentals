import os
from config import *
# from Pycodes.Code_Doc_Agent.config import (
#     SUPPORTED_EXTENSIONS,
#     EXCLUDED_DIRS
# )

def scan_repository(repo_path):

    files = []

    for root, dirs, filenames in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in filenames:

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                files.append(os.path.join(root, file))

    return files