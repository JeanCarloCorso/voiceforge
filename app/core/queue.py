import threading
import queue
from app.services.tts_service import gerar_audio

task_queue = queue.Queue()
_worker_started = threading.Event()

def worker():
    while True:
        task = task_queue.get()
        try:
            gerar_audio(
                texto=task["texto"],
                speaker=task["speaker"]
            )
        except Exception as e:
            print(f"❌ Erro na geração: {e}")
        finally:
            task_queue.task_done()

def start_worker():
    if _worker_started.is_set():
        print("⚠️ Worker já iniciado, ignorando")
        return

    print("🚀 Subindo worker de geração de áudio")
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    _worker_started.set()
