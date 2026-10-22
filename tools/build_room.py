#!/usr/bin/env python3
"""
Package a room from src/<room>/ into <room>/<room>.tar.gz for players.

The archive keeps each file's real permissions (so a locked folder arrives
locked and hidden files stay hidden) but scrubs everything about the author's
machine: every entry is owned by warden:lockup and stamped with the same
fixed time, and the gzip header carries no filename or timestamp. Building
twice gives byte-identical archives.

Folders the author locked (e.g. chmod 000) are opened briefly so they can be
read, then restored.

Usage: python3 tools/build_room.py escape-room
"""

import gzip
import io
import os
import stat
import sys
import tarfile
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER, GROUP, ID = "warden", "lockup", 1337
MTIME = 946684740  # 1999-12-31 23:59:00 UTC (Y2K eve)


@contextmanager
def readable(path):
    """Temporarily give the owner read/enter rights on a locked directory."""
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode & stat.S_IRUSR and mode & stat.S_IXUSR:
        yield mode
        return
    path.chmod(mode | stat.S_IRWXU)
    try:
        yield mode
    finally:
        path.chmod(mode)


def entries(room_dir):
    """(path, archive name, real mode) for everything in the room, sorted."""
    out = []

    def walk(path, name):
        with readable(path) as mode:
            out.append((path, name, mode))
            for child in sorted(path.iterdir(), key=lambda p: p.name):
                if child.is_dir() and not child.is_symlink():
                    walk(child, f"{name}/{child.name}")
                elif child.is_file() and not child.is_symlink():
                    out.append((child, f"{name}/{child.name}", stat.S_IMODE(child.stat().st_mode)))
                else:
                    sys.exit(f"refusing to package {child}: only plain files and folders allowed")

    walk(room_dir, room_dir.name)
    return out


def build(room):
    src = ROOT / "src" / room
    if not src.is_dir():
        sys.exit(f"no such room: {src}")
    out_dir = ROOT / room
    out_dir.mkdir(exist_ok=True)

    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.GNU_FORMAT) as tar:
        for path, name, mode in entries(src):
            info = tarfile.TarInfo(name)
            info.mode, info.mtime = mode, MTIME
            info.uid = info.gid = ID
            info.uname, info.gname = OWNER, GROUP
            if path.is_dir():
                info.type = tarfile.DIRTYPE
                tar.addfile(info)
            else:
                # Read through the parent's temporary unlock, if any.
                with readable(path.parent):
                    data = path.read_bytes()
                info.size = len(data)
                tar.addfile(info, io.BytesIO(data))

    target = out_dir / f"{room}.tar.gz"
    with open(target, "wb") as f, gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0, compresslevel=9) as gz:
        gz.write(raw.getvalue())
    print(f"built {target.relative_to(ROOT)} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
