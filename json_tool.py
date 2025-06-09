#!/usr/bin/env python3
"""Simple JSON utility for pretty-printing or minifying JSON data."""

import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Pretty-print or minify JSON from a file or stdin"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin,
        help="JSON file to read; defaults to stdin",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--pretty",
        action="store_true",
        help="Output formatted JSON (default)",
    )
    group.add_argument(
        "--minify",
        action="store_true",
        help="Output minified JSON",
    )

    args = parser.parse_args()

    data = json.load(args.file)

    if args.minify:
        json.dump(data, sys.stdout, separators=(",", ":"))
    else:
        json.dump(data, sys.stdout, indent=4, sort_keys=True)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
