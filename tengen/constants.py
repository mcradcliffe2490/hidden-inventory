import os

from path import Path
from yarl import URL

DEV_MODE = os.getenv("DEV_MODE")
TENGEN_DIR = Path(__file__).parent
ROOT = TENGEN_DIR.parent
BASE_URL = URL("https://tcbscans.me")
GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
DOCKER = os.getenv("DOCKER")
