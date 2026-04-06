import json
import sys

with open("requirements.json", "r") as f:
    requirements = json.load(f)

with open("test_cases.json", "r") as f:
    test_cases = json.load(f)

test_case_requirements = {tc["requirement_id"] for tc in test_cases}
missing = []

for req in requirements:
    req_id = req["requirement_id"]
    if req_id not in test_case_requirements:
        missing.append(req_id)

if missing:
    print("Verification failed.")
    print("Missing test cases for:")
    for m in missing:
        print(m)
    sys.exit(1)

print("Verification passed.")
