from pathlib import Path
import sys

from src.utils.paths import TMP_DOWNLOADS, ensure_dirs
from src.relatorios.r01 import processar_relatorio_01

def pick_latest_01(downloads: Path) -> Path:
    # pega o arquivo mais recente na pasta de downloads cujo nome começa com "01"
    cand = sorted(
        [p for p in downloads.iterdir() if p.is_file() and p.name.startswith("01")],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not cand:
        raise FileNotFoundError("Nenhum arquivo começando com '01' encontrado em Downloads.")
    return cand[0]

if __name__ == "__main__":
    ensure_dirs()
    # Se passar o caminho do arquivo via argumento, usa ele; senão pega o mais recente que começa com "01"
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else pick_latest_01(TMP_DOWNLOADS)
    out = processar_relatorio_01(arquivo)
    print("OK:", {k: str(v) for k, v in out.items()})