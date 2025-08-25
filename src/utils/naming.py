from pathlib import Path
from datetime import datetime
import re

def ddmmaa(dt: datetime | None = None) -> str:
    dt = dt or datetime.now()
    return dt.strftime("%d.%m.%y")

def _ensure_dot(ext: str) -> str:
    ext = (ext or "").strip()
    return ext if (ext.startswith(".") or ext == "") else f".{ext}"

def nome_mais_atual(nome: str, ext: str, data: str | None = None) -> str:
    """
    "{nome} # {dd.mm.aa}{ext}"
    """
    data = data or ddmmaa()
    ext = _ensure_dot(ext)
    return f"{nome} # {data}{ext}"

def nome_historico(nome: str, x: int, ext: str, data: str | None = None) -> str:
    """
    "{nome} # {dd.mm.aa}-{x}{ext}"
    """
    data = data or ddmmaa()
    ext = _ensure_dot(ext)
    return f"{nome} # {data}-{x}{ext}"

def proximo_indice_diario(pasta: Path | str, base_nome: str, data_ddmmaa: str) -> int:
    """
    Varre a pasta e retorna o próximo x para o padrão:
    "{base_nome} # {dd.mm.aa}-{x}{ext}"
    """
    pasta = Path(pasta)
    if not pasta.exists():
        return 1

    patt = re.compile(
        re.escape(base_nome) + r"\s*#\s*" + re.escape(data_ddmmaa) + r"-(\d+)$",
        re.IGNORECASE
    )

    max_x = 0
    for p in pasta.iterdir():
        if not p.is_file():
            continue
        m = patt.search(p.stem)  # usa o nome sem extensão
        if m:
            try:
                x = int(m.group(1))
                if x > max_x:
                    max_x = x
            except ValueError:
                pass
    return max_x + 1
