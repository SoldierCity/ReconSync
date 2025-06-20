import os
from datetime import datetime, timedelta
import zipfile
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent.backup import create_backup, prune_backups


def test_create_backup(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    (src / "file.txt").write_text("data")

    backup_dir = tmp_path / "backups"
    path = create_backup(src, backup_dir)

    assert path.exists()
    assert path.parent == backup_dir
    with zipfile.ZipFile(path) as zf:
        assert "file.txt" in zf.namelist()


def test_create_backup_missing_source(tmp_path):
    with pytest.raises(FileNotFoundError):
        create_backup(tmp_path / "missing", tmp_path)


def test_prune_backups(tmp_path):
    backup_dir = tmp_path / "backups"
    backup_dir.mkdir()

    old_file = backup_dir / "old.zip"
    old_file.write_text("old")
    # set modification time to 2 days ago
    old_time = (datetime.utcnow() - timedelta(days=2)).timestamp()
    os.utime(old_file, (old_time, old_time))

    new_file = backup_dir / "new.zip"
    new_file.write_text("new")

    prune_backups(backup_dir, retention_days=1)

    assert not old_file.exists()
    assert new_file.exists()
