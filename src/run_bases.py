# src/run_bases.py
from pathlib import Path
from typing import Optional

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.utils.logger import log_event
from src.relatorios.r_bases import mover_para_bases_keepname

# Arquivos esperados (prefixo do nome)
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

if __name__ == "__main__":
    ensure_dirs()
    for prefix in EXPECTED:
        f = pick_latest_by_prefix(TMP_DOWNLOADS, prefix)
        if f is None:
            log_event("MISS", f"{prefix}*", "Downloads")
            continue
        mover_para_bases_keepname(f)  # log BASES é feito dentro da função
