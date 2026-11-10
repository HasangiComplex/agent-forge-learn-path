# validate.py
import json, csv
from collections import Counter
from pathlib import Path
from pydantic import ValidationError
from models import Post

rows = []
for f in sorted(Path("week01/data").glob("*.json")):
    try:
        Post.model_validate(json.loads(f.read_text()))
    except ValidationError as e:
        for err in e.errors():
            rows.append({
                "file": f.name,
                "field": ".".join(str(p) for p in err["loc"]),
                "type": err["type"],
                "message": err["msg"],
            })


with open("week01/errors.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["file", "field", "type", "message"])
    w.writeheader()
    w.writerows(rows)

print(Counter(r["type"] for r in rows))
