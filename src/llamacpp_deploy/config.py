from dotenv import load_dotenv
from importlib.metadata import version, PackageNotFoundError
import os, socket


load_dotenv()

try:
    VERSION = version("llamacpp-deploy")
except PackageNotFoundError:
    VERSION = "unknown"

MODELNAME = os.getenv("MODELNAME", "unknown")
HOSTNAME = socket.gethostname()
