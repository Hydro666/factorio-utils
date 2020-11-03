import os.path

REDIS_PORT = 6379
RAW_URL = (
    "https://gist.githubusercontent.com/Bilka2/6b8a6a9e4a4ec779573ad703d03c1ae7/raw"
)
f = os.path.dirname
ROOT_DIR = f(f(os.path.abspath(__file__)))
JSON_OUT = os.path.join(ROOT_DIR, "data/data_json.json")
