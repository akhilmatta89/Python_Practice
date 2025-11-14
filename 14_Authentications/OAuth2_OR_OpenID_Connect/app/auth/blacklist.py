from datetime import datetime, timezone
from typing import Dict

_blacklisted: Dict[str, int] = {}  # tid -> exp_epoch

def _now_epoch() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def is_blacklisted(tid: str) -> bool:
    now = _now_epoch()
    expired = [k for k, v in _blacklisted.items() if v < now]
    for k in expired:
        _blacklisted.pop(k, None)
    return tid in _blacklisted

def add_to_blacklist(tid: str, exp_epoch: int) -> None:
    _blacklisted[tid] = exp_epoch
