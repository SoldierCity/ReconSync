"""Backup utilities for Recon Agent."""

from pathlib import Path
import shutil


def create_backup(source: str, target_dir: str) -> Path:
    """Create a zip archive of the source directory.

    This is a placeholder implementation used during early development.
    """
    # TODO: add error handling and retention policy
    src = Path(source)
    dst = Path(target_dir)
    dst.mkdir(parents=True, exist_ok=True)
    archive = dst / f"{src.name}.zip"
    shutil.make_archive(str(archive.with_suffix("")), "zip", source)
    return archive