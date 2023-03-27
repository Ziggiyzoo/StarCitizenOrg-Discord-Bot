"""
BRVNS Source Module
"""
import os


def _get_firebase_secret_path() -> str:
    if os.name == "nt":
        return os.path.join(os.getenv("APPDATA"), "\\secrets\\firebase_secret.json")

    return os.path.join("/var/secrets/firebase_secret.json")
