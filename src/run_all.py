# src/run_all.py
from src.run_r01 import run as run_r01
from src.run_r02 import run as run_r02
from src.run_bases import run as run_bases
from src.utils.logger import log_event

if __name__ == "__main__":
    log_event("START", "organizador", "-")

    r1 = run_r01()
    r2 = run_r02()
    rb = run_bases()

    total_ok = r1["ok"] + r2["ok"] + rb["ok"]
    total_miss = r1["miss"] + r2["miss"] + rb["miss"]

    log_event("DONE", f"ok={total_ok}; miss={total_miss}", "-")
    print({"ok": total_ok, "miss": total_miss})
