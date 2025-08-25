# src/run_r02.py
from pathlib import Path
from typing import Optional

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.utils.logger import log_event
from src.relatorios.r02 import mover_para_relatorios2

# Prefixos esperados (início do nome do arquivo)
EXPECTED_PREFIXES = [
    "02 -", "03 -", "04 -", "05 -", "06 -",
    "07 -",               # entra futuramente
    "08 -", "09 -", "10 -", "11 -", "12 -",
    "13 -", "14 -", "15 -",
]

def pick_latest_by_prefix(folder: Path, prefix: str) -> Optional[Path]:
    """Retorna o arquivo MAIS RECENTE na pasta que começa com o prefixo dado."""
    if not folder.exists():
        return None
    cand = sorted(
        [p for p in folder.iterdir() if p.is_file() and p.name.startswith(prefix)],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return cand[0] if cand else None

if __name__ == "__main__":
    ensure_dirs()
    downloads = TMP_DOWNLOADS

    for prefix in EXPECTED_PREFIXES:
        f = pick_latest_by_prefix(downloads, prefix)
        if f is None:
            # loga não encontrado
            log_event("MISS", f"{prefix}*", "Downloads")
            continue

        # move p/ Relatórios 2 (overwrite mantendo nome)
        dest = mover_para_relatorios2(f)
        # já faz log dentro da função (R2)
