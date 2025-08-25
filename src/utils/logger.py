from datetime import datetime
from .paths import LOG_PATH

def log_event(action: str, filename: str, folder: str) -> None:
    """
    Linha simples (append-only):
    YYYY-MM-DD HH:MM:SS | ACTION | filename | folder
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} | {action} | {filename} | {folder}\n"
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line)
