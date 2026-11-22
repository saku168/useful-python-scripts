"""Validate and format a JSON file using only the standard library."""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python json_pretty.py path/to/file.json")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"File not found: {path}")
        raise SystemExit(1)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}")
        raise SystemExit(1)
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
