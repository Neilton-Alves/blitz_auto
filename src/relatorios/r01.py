from pathlib import Path
import shutil

from ..utils.paths import RELATORIOS_HIST
from ..utils.naming import ddmmaa, proximo_indice_diario, nome_historico

# Nome oficial do relatório 01
NOME_REL = "01 - DCex - Dados do monitoramento de demandas"
EXT_PADRAO = ".csv"

def mover_para_historico(arquivo_tmp: str | Path) -> Path:
    """
    Move o arquivo baixado para:
      R:\User\bases\Relatórios sydle\01 - historico
    usando o padrão: "{nome} # {dd.mm.aa}-{x}{ext}"
    - não sobrescreve; x é o próximo índice do dia.
    """
    p_tmp = Path(arquivo_tmp)
    ext = p_tmp.suffix or EXT_PADRAO
    data = ddmmaa()
    x = proximo_indice_diario(RELATORIOS_HIST, NOME_REL, data)
    nome_final = nome_historico(NOME_REL, x, ext, data)
    destino = RELATORIOS_HIST / nome_final
    RELATORIOS_HIST.mkdir(parents=True, exist_ok=True)
    shutil.move(str(p_tmp), str(destino))
    return destino
