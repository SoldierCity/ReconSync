"""Backup utilities for Recon Agent."""

from __future__ import annotations

import os
from datetime import datetime, timedelta
from pathlib import Path
import shutil
from typing import Iterable

__all__ = ["create_backup", "prune_backups"]


def create_backup(source: str | os.PathLike, target_dir: str | os.PathLike,
                  *, retention_days: int | None = None) -> Path:
    """Create a ZIP archive from ``source`` inside ``target_dir``.

    Parameters
    ----------
    source:
        Directory to archive.
    target_dir:
        Directory where the archive will be created.
    retention_days:
        If provided, ``prune_backups`` will be called after creation using this
        value.

    Returns
    -------
    :class:`pathlib.Path`
        Path to the created archive.
    """

    src = Path(source)
    if not src.is_dir():
        raise FileNotFoundError(f"Backup source not found: {src}")

    dst = Path(target_dir)
    dst.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    archive = dst / f"backup_{src.name}_{timestamp}.zip"

    shutil.make_archive(str(archive.with_suffix("")), "zip", str(src))

    if retention_days is not None:
        prune_backups(dst, retention_days)

    return archive


def prune_backups(directory: str | os.PathLike, retention_days: int) -> None:
    """Remove backup archives older than ``retention_days``.

    Parameters
    ----------
    directory:
        The directory containing backup archives.
    retention_days:
        Age threshold in days. Files older than this will be deleted.
    """

    cutoff = datetime.utcnow() - timedelta(days=retention_days)
    dir_path = Path(directory)

    for path in _iter_archives(dir_path):
        if path.stat().st_mtime < cutoff.timestamp():
            path.unlink(missing_ok=True)


def _iter_archives(directory: Path) -> Iterable[Path]:
    """Yield ``.zip`` files within ``directory``."""

    for child in directory.iterdir():
        if child.suffix == ".zip" and child.is_file():
            yield child
