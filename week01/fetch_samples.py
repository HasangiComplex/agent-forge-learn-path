# fetch_samples.py
import json, httpx
from pathlib import Path

out = Path("week01/data"); out.mkdir(parents=True, exist_ok=True)
for i in range(1, 21):
    r = httpx.get(f"https://jsonplaceholder.typicode.com/posts/{i}")
    r.raise_for_status()
    (out / f"post_{i:02d}.json").write_text(json.dumps(r.json(), indent=2))
