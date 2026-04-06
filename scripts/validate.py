import json
import sys

with open("requirements.json", "r") as f:
    requirements = json.load(f)

with open("expected_structure.json", "r") as f:
    expected = json.load(f)

req_ids = {r["requirement_id"] for r in requirements}
missing = []

for parent, suffixes in expected.items():
    for suffix in suffixes:
        full_id = f"{parent}{suffix}"
        if full_id not in req_ids:
            missing.append(full_id)

if missing:
    print("Validation failed.")
    print("Missing expected requirements:")
    for m in missing:
        print(m)
    sys.exit(1)

print("Validation passed.")
