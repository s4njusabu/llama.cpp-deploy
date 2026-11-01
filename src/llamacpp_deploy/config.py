import os
import socket
from importlib.metadata import PackageNotFoundError, version

from dotenv import load_dotenv

load_dotenv()

try:
    VERSION = version("llamacpp-deploy")
except PackageNotFoundError:
    VERSION = "unknown"

MODELNAME = os.getenv("MODELNAME", "unknown")
HOSTNAME = socket.gethostname()
