#!/usr/bin/env python3
"""Generate a phrase dictionary for the 倚天26鍵方案.

The helper mirrors JeffChien/rime-flypyquick5's idea of maintaining a
separate phrase table so that associative candidates stay responsive.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

@dataclass(frozen=True)
class Entry:
    code: str
    weight: int

Dictionary = Dict[str, List[Entry]]


def read_dictionary(path: Path) -> Dictionary:
    mapping: Dictionary = {}
    with path.open("r", encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if line in {"---", "..."} or line.startswith("name:") or line.startswith("version:"):
                continue
            parts = line.split()
            if len(parts) < 3:
                # skip YAML directives, comments, etc.
                continue
            text, code, weight_str = parts[:3]
            try:
                weight = int(weight_str.rstrip("%"))
            except ValueError:
                # Skip malformed weights but warn the caller.
                print(f"[warn] skip entry with non-integer weight: {line}", file=sys.stderr)
                continue
            mapping.setdefault(text, []).append(Entry(code=code, weight=weight))
    for entries in mapping.values():
        entries.sort(key=lambda item: item.weight, reverse=True)
    return mapping


def read_phrases(path: Path) -> List[str]:
    phrases: List[str] = []
    with path.open("r", encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            phrases.append(line)
    return phrases


def choose_codes(phrase: str, mapping: Dictionary) -> Tuple[List[str], List[str]]:
    codes: List[str] = []
    missing: List[str] = []
    for char in phrase:
        entries = mapping.get(char)
        if not entries:
            missing.append(char)
            continue
        codes.append(entries[0].code)
    return codes, missing


def write_dictionary(path: Path, entries: Sequence[Tuple[str, str, int]]) -> None:
    header = """# Rime dictionary
# encoding: utf-8

---
name: Etem26keys_phrase
version: "0.1.0"
sort: by_weight
use_preset_vocabulary: false
columns:
  - text
  - code
  - weight
...
"""
    with path.open("w", encoding="utf-8") as fh:
        fh.write(header)
        for text, code, weight in entries:
            fh.write(f"{text}\t{code}\t{weight}\n")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_dict", type=Path, help="Path to the base Etem26keys dictionary")
    parser.add_argument("phrases", type=Path, help="UTF-8 file that contains one phrase per line")
    parser.add_argument("output", type=Path, help="Where to write the generated phrase table")
    parser.add_argument(
        "--weight-start",
        type=int,
        default=600,
        help="Initial weight assigned to the first phrase entry (default: 600)",
    )
    parser.add_argument(
        "--weight-step",
        type=int,
        default=5,
        help="Decrease applied to the weight of each subsequent phrase (default: 5)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    mapping = read_dictionary(args.base_dict)
    phrases = read_phrases(args.phrases)

    generated: List[Tuple[str, str, int]] = []
    missing_chars: Dict[str, List[str]] = {}

    weight = args.weight_start
    for phrase in phrases:
        codes, missing = choose_codes(phrase, mapping)
        if missing:
            missing_chars[phrase] = missing
            continue
        generated.append((phrase, " ".join(codes), weight))
        weight = max(1, weight - args.weight_step)

    write_dictionary(args.output, generated)

    if missing_chars:
        print(
            "[info] The following phrases were skipped because some characters were not found in the base dictionary:",
            file=sys.stderr,
        )
        for phrase, chars in missing_chars.items():
            print(f"  {phrase}: {' '.join(chars)}", file=sys.stderr)

    print(f"Generated {len(generated)} phrase entries → {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
