from os import getenv
from pathlib import Path

### ENVIRONMENT

TOKEN = getenv("TOKEN")

MONGO_TOKEN = getenv("MONGO_TOKEN")
MONGO_NAME = getenv("MONGO_NAME")

DEVELOPER_ID = int(getenv("DEVELOPER_ID", 0))


### HANDLERS

# - Variant 1
HANDLERS_ROOT = "src"  
HANDLERS = ["handlers"]

# Examples. Uncomment if you want.
# HANDLERS.append(Path("handlers") / "_example")

# - Variant 2
# HANDLERS_ROOT = "src.handlers"
# HANDLERS = ["general", "misc", "..."]


### DIRECTORIES

BASE_DIR = Path(__file__).parent.parent
PUBLIC_DIR = BASE_DIR / 'public'
