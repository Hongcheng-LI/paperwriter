#!/usr/bin/env python3
"""Sync the paperwriter skill (source of truth at repo root) into the DSH plugin bundle.

The repo root is the single source of truth for the skill. This script copies
SKILL.md, references/, scripts/ and assets/ into dsh-plugin/assets/paperwriter/
so that the plugin directory is self-contained (required for git/npm installs).

Usage:
  python scripts/sync_dsh.py           # copy (idempotent, rebuilds the target)
  python scripts/sync_dsh.py --check   # exit 1 if the target drifted from source
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SOURCE_ITEMS = ("SKILL.md", "references", "scripts", "assets")
TARGET_REL = Path("dsh-plugin") / "assets" / "paperwriter"
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def snapshot(base: Path) -> dict[str, bytes]:
    """Collect relative posix path -> bytes for every source item under base."""
    files: dict[str, bytes] = {}
    for item in SOURCE_ITEMS:
        src = base / item
        if not src.exists():
            raise SystemExit(f"missing source item: {src}")
        if src.is_file():
            files[item] = src.read_bytes()
        else:
            for p in sorted(src.rglob("*")):
                if not p.is_file():
                    continue
                if "__pycache__" in p.parts or p.suffix == ".pyc":
                    continue
                files[p.relative_to(base).as_posix()] = p.read_bytes()
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync skill sources into dsh-plugin/assets/paperwriter")
    parser.add_argument("--check", action="store_true", help="verify target matches source; exit 1 on drift")
    args = parser.parse_args()

    root = repo_root()
    target = root / TARGET_REL
    source_files = snapshot(root)

    if args.check:
        if not target.exists():
            print(f"[check] FAIL: target missing: {target}")
            return 1
        target_files = snapshot(target)
        missing = sorted(set(source_files) - set(target_files))
        extra = sorted(set(target_files) - set(source_files))
        changed = sorted(k for k in set(source_files) & set(target_files) if source_files[k] != target_files[k])
        if missing or extra or changed:
            for k in missing:
                print(f"[check] missing: {k}")
            for k in extra:
                print(f"[check] extra: {k}")
            for k in changed:
                print(f"[check] changed: {k}")
            print("[check] FAIL: dsh-plugin assets drifted from source; run scripts/sync_dsh.py")
            return 1
        print(f"[check] OK: {len(source_files)} files in sync")
        return 0

    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    copied = 0
    for item in SOURCE_ITEMS:
        src = root / item
        dst = target / item
        if src.is_file():
            shutil.copy2(src, dst)
            copied += 1
        else:
            shutil.copytree(src, dst, ignore=IGNORE)
            copied += sum(1 for p in dst.rglob("*") if p.is_file())
    print(f"[sync] copied {copied} files -> {TARGET_REL.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
