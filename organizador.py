from pathlib import Path
import shutil
from datetime import datetime
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


PASTA_ORIGEM = Path(r"C:\Users\jovem\Downloads")

MAPEAMENTO = {
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Compactados",
    ".rar": "Compactados",
}


def log(msg):
    with open("organizador.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")


def organizar_arquivo(path: Path):
    if not path.is_file():
        return

    ext = path.suffix.lower()
    if ext not in MAPEAMENTO:
        return

    destino = PASTA_ORIGEM / MAPEAMENTO[ext]
    destino.mkdir(exist_ok=True)

    destino_final = destino / path.name
    contador = 1
    while destino_final.exists():
        destino_final = destino / f"{path.stem}_{contador}{path.suffix}"
        contador += 1

    shutil.move(str(path), str(destino_final))
    log(f"Movido: {path.name}")


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)
            organizar_arquivo(Path(event.src_path))


def start_monitor():
    observer = Observer()
    observer.schedule(Handler(), str(PASTA_ORIGEM), recursive=False)
    observer.start()
    log("Monitoramento iniciado")

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        log("Monitoramento finalizado")

if __name__ == "__main__":
    log("organizador.py executado diretamente")
    start_monitor()