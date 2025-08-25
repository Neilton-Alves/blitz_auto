# src/run_bases.py
from pathlib import Path
from typing import Optional

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.utils.logger import log_event
from src.relatorios.r_bases import mover_para_bases_keepname

EXPECTED = [
    "Painel geral de demandas",
    "Demandas canceladas",
    "Demandas por Empresa e Centro de custo",
    "Painel de demandas não trabalhadas",
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
    Move os 4 arquivos extras p/ Bases Comuns.
    Retorna {"ok": N, "miss": M}
    """
    ensure_dirs()
    ok = miss = 0
    for prefix in EXPECTED:
        f = pick_latest_by_prefix(TMP_DOWNLOADS, prefix)
        if f is None:
            log_event("MISS", f"{prefix}*", "Downloads")
            miss += 1
            continue
        mover_para_bases_keepname(f)  # já loga BASES
        ok += 1
    return {"ok": ok, "miss": miss}

if __name__ == "__main__":
    out = run()
    print("R_BASES:", out)
