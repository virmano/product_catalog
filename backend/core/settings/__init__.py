from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')

from .apps import *
from .auth import *
from .base import *
from .database import *
from .localization import *
from .static import *
from .templates import *
