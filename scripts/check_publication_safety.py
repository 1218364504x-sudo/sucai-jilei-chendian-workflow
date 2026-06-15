#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = [
    ("OpenAI/DeepSeek style key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")),
    ("Feishu base URL", re.compile(r"https?://[^\s)]+\.feishu\.cn/base/[^\s)]+")),
    ("Feishu wiki URL", re.compile(r"https?://[^\s)]+\.feishu\.cn/wiki/[^\s)]+")),
    ("macOS user path", re.compile(r"/Users/[^/\s]+")),
    ("Linux home path", re.compile(r"/home/[^/\s]+")),
    ("Windows user path", re.compile(r"[A-Za-z]:\\\\Users\\\\")),
    ("app secret", re.compile(r"(?i)(app_secret|client_secret|api_secret)\s*[:=]\s*[^\\s]+")),
    ("api key assignment", re.compile(r"(?i)(api_key|apikey|token)\s*[:=]\s*[^\\s]+")),
]

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".js",
    ".ts",
    ".json",
    ".yaml",
    ".yml",
    ".env",
    ".example",
    ".gitignore",
}


def is_text_file(path: Path) -> bool:
    if path.name in {".gitignore"}:
        return True
    return path.suffix in TEXT_SUFFIXES or ".env" in path.name


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == Path(__file__).name:
            continue
        if not path.is_file() or not is_text_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if "your_" in line:
                continue
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append((path.relative_to(root), line_no, label, line.strip()))

    if findings:
        print("Potential sensitive content found:")
        for rel, line_no, label, line in findings:
            print(f"- {rel}:{line_no} [{label}] {line[:160]}")
        return 1

    print("No obvious sensitive content found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
