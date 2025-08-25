from pathlib import Path
import shutil

from ..utils.paths import BASES_COMUNS
from ..utils.logger import log_event

def mover_para_bases_keepname(arquivo: str | Path) -> Path:
    """
    Move para Bases Comuns SYDLE mantendo o NOME original.
    Overwrite sempre. Registra log como BASES.
    """
    p_src = Path(arquivo)
    destino = BASES_COMUNS / p_src.name
    BASES_COMUNS.mkdir(parents=True, exist_ok=True)

    if destino.exists():
        try:
            destino.unlink()
        except Exception:
            pass

    try:
        shutil.move(str(p_src), str(destino))
    except Exception:
        shutil.copy2(str(p_src), str(destino))
        try:
            p_src.unlink()
        except Exception:
            pass

    log_event("BASES", destino.name, "Bases Comuns SYDLE")
    return destino
