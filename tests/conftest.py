import pytest

from core import hid_gesture


@pytest.fixture(autouse=True)
def _isolate_last_device_cache(tmp_path, monkeypatch):
    """Keep tests that reach _try_connect from reading or overwriting the
    real ~/Library/Application Support/Mouser/last_device.json."""
    monkeypatch.setattr(hid_gesture, "_cache_dir", lambda: str(tmp_path))
