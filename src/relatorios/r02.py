# src/relatorios/r02.py
from pathlib import Path
import shutil

from ..utils.paths import RELATORIOS_2
from ..utils.logger import log_event

def mover_para_relatorios2(arquivo_tmp: str | Path) -> Path:
    r"""
    Move para pasta "Relatórios 2" (R:\User\bases\Relatórios sydle\Relatórios 2)
    - mantém o NOME ORIGINAL do arquivo
    - se existir, SOBRESCREVE
    - log: R2
    """
    p_src = Path(arquivo_tmp)
    destino = RELATORIOS_2 / p_src.name
    RELATORIOS_2.mkdir(parents=True, exist_ok=True)

    # overwrite seguro
    if destino.exists():
        try:
            destino.unlink()
        except Exception:
            pass

    try:
        shutil.move(str(p_src), str(destino))
    except Exception:
        # fallback: copia e apaga a origem
        shutil.copy2(str(p_src), str(destino))
        try:
            p_src.unlink()
        except Exception:
            pass

    log_event("R2", destino.name, "Relatórios 2")
    return destino

