# src/relatorios/r01.py
from pathlib import Path
import shutil

from ..utils.paths import RELATORIOS_HIST, BASES_COMUNS, MAIS_ATUAL
from ..utils.naming import ddmmaa, proximo_indice_diario, nome_historico, nome_mais_atual
from ..utils.logger import log_event

# Nome oficial do relatório 01
NOME_REL = "01 - DCex - Dados do monitoramento de demandas"
EXT_PADRAO = ".csv"

def mover_para_historico(arquivo_tmp: str | Path) -> Path:
    p_tmp = Path(arquivo_tmp)
    ext = p_tmp.suffix or EXT_PADRAO
    data = ddmmaa()
    x = proximo_indice_diario(RELATORIOS_HIST, NOME_REL, data)
    nome_final = nome_historico(NOME_REL, x, ext, data)
    destino = RELATORIOS_HIST / nome_final
    RELATORIOS_HIST.mkdir(parents=True, exist_ok=True)
    shutil.move(str(p_tmp), str(destino))
    # LOG
    log_event("HIST", destino.name, "01 - historico")
    return destino

def copiar_para_bases_comuns(arquivo_origem: str | Path) -> Path:
    p_src = Path(arquivo_origem)
    ext = p_src.suffix or EXT_PADRAO
    nome_final = f"{NOME_REL}{ext}"  # sem data
    destino = BASES_COMUNS / nome_final
    BASES_COMUNS.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(p_src), str(destino))  # sobrescreve
    # LOG
    log_event("BASES", destino.name, "Bases Comuns SYDLE")
    return destino

def copiar_para_mais_atual(arquivo_origem: str | Path) -> Path:
    p_src = Path(arquivo_origem)
    ext = p_src.suffix or EXT_PADRAO
    data = ddmmaa()
    nome_final = nome_mais_atual(NOME_REL, ext, data)  # com data, 1 por dia
    destino = MAIS_ATUAL / nome_final
    MAIS_ATUAL.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(p_src), str(destino))  # sobrescreve
    # LOG
    log_event("ATUAL", destino.name, "01 - mais atual")
    return destino

def processar_relatorio_01(caminho_baixado: str | Path) -> dict:
    """
    Sequência:
      1) historico  -> "... # dd.mm.aa-x"
      2) bases      -> sobrescreve (sem data)
      3) mais_atual -> sobrescreve ("... # dd.mm.aa")
    """
    hist = mover_para_historico(caminho_baixado)
    bc   = copiar_para_bases_comuns(hist)
    ma   = copiar_para_mais_atual(hist)
    return {"historico": hist, "bases_comuns": bc, "mais_atual": ma}
