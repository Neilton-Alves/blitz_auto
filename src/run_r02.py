# src/run_r02.py
from pathlib import Path
from typing import Optional

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.utils.logger import log_event
from src.relatorios.r02 import mover_para_relatorios2

EXPECTED_PREFIXES = [
    "02 -", "03 -", "04 -", "05 -", "06 -",
    "07 -",  # futuro
    "08 -", "09 -", "10 -", "11 -", "12 -",
    "13 -", "14 -", "15 -",
]

def pick_latest_by_prefix(folder: Path, prefix: str) -> Optional[Path]:
    if not folder.exists():
        return None
    pref = prefix.lower()
    cand = sorted(
        [p for p in folder.iterdir() if p.is_file() and p.name.lower().startswith(pref)],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return cand[0] if cand else None

def run() -> dict:
    """
    Move 02..12, 07, 13..15 p/ Relatórios 2.
    Retorna {"ok": N, "miss": M}
    """
    ensure_dirs()
    ok = miss = 0
    for prefix in EXPECTED_PREFIXES:
        f = pick_latest_by_prefix(TMP_DOWNLOADS, prefix)
        if f is None:
            log_event("MISS", f"{prefix}*", "Downloads")
            miss += 1
            continue
        mover_para_relatorios2(f)  # já loga R2
        ok += 1
    return {"ok": ok, "miss": miss}

if __name__ == "__main__":
    out = run()
    print("R02:", out)
