from .base import *
import os

DEBUG = False

ALLOWED_HOSTS += [
    "localhost",
    "127.0.0.1"
]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
