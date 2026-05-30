import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

MODEL_NAME = "gemini-2.5-flash"

SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".java",
    ".go",
    ".cs"
]

EXCLUDED_DIRS = [
    "node_modules",
    ".git",
    "dist",
    "build",
    ".venv",
    "__pycache__"
]