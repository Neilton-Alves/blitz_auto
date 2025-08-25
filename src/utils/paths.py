from pathlib import Path

# === Caminhos alvo (se mudar a raiz, só ajuste REDE_BASE) ===
REDE_BASE        = Path(r"R:\User\bases\Relatórios sydle")
BASES_COMUNS     = REDE_BASE / "Bases Comuns SYDLE"   # sobrescreve a cada novo download ("{nome} # {dd.mm.aa}{ext}")
MAIS_ATUAL       = REDE_BASE / "01 - mais atual"      # 1 por dia ("{nome} # {dd.mm.aa}{ext}")
RELATORIOS_HIST  = REDE_BASE / "01 - historico"       # histórico ("{nome} # {dd.mm.aa}-x{ext}")
RELATORIOS_2     = REDE_BASE / "Relatórios 2"         # 02..12, 07, 13..15 (overwrite, sem renome)

# Log geral da automação (TXT)
LOG_PATH         = Path(r"R:\User\bases\Logs automação\log sydle.txt")

# Pasta de downloads (Win10)
TMP_DOWNLOADS    = Path(r"C:\Users\Dcex03\Downloads")

def ensure_dirs():
    for p in (
        BASES_COMUNS,
        MAIS_ATUAL,
        RELATORIOS_HIST,
        RELATORIOS_2,
        TMP_DOWNLOADS,
        LOG_PATH.parent,
    ):
        p.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure_dirs()
    print("OK - pastas garantidas")

