import os

from dotenv import load_dotenv

DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "15000"))

load_dotenv()

GITHUB_URL = os.getenv("GITHUB_URL")
TEST_EMAIL_GITHUB = os.getenv("TEST_USERNAME")
TEST_PASSWORD_GITHUB = os.getenv("TEST_PASSWORD")