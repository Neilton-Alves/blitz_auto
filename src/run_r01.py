# src/run_r01.py
from pathlib import Path
import sys
from typing import Optional

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.utils.logger import log_event
from src.relatorios.r01 import processar_relatorio_01

def pick_latest_01(downloads: Path) -> Optional[Path]:
    """Mais recente em Downloads cujo nome começa com '01'."""
    if not downloads.exists():
        return None
    cand = sorted(
        [p for p in downloads.iterdir() if p.is_file() and p.name.startswith("01")],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return cand[0] if cand else None

def run() -> dict:
    """
    Executa o fluxo do 01.
    Retorna {"ok": 1|0, "miss": 1|0}
    """
    ensure_dirs()
    # arquivo via argumento opcional
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else pick_latest_01(TMP_DOWNLOADS)
    if not arquivo or not arquivo.exists():
        log_event("MISS", "01 -*", "Downloads")
        return {"ok": 0, "miss": 1}
    try:
        processar_relatorio_01(arquivo)
        return {"ok": 1, "miss": 0}
    except Exception:
        # registra erro simples e segue
        log_event("ERROR", "01 process", "organizador")
        return {"ok": 0, "miss": 1}

if __name__ == "__main__":
    out = run()
    print("R01:", out)
