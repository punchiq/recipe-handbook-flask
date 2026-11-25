import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "data" / "recipes.json"


def recipes():
    return json.loads(DATA.read_text(encoding="utf-8"))

