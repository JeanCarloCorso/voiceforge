import threading
import queue
from app.services.tts_service import gerar_audio
from app.core.task_store import tasks

task_queue = queue.Queue()
_worker_started = threading.Event()

def worker():
    while True:
        task_id = task_queue.get()
        task = tasks.get(task_id)

        if not task:
            task_queue.task_done()
            continue

        try:
            task.status = "processing"
            print(f"🎙️ Processando task {task.id}")

            audio = gerar_audio(
                texto=task.texto,
                speaker=task.speaker
            )

            task.audio_file = audio
            task.status = "done"
            print(f"✅ Task {task.id} finalizada")

        except Exception as e:
            task.status = "error"
            task.error = str(e)
            print(f"❌ Task {task.id} erro: {e}")

        finally:
            task_queue.task_done()

def start_worker():
    if _worker_started.is_set():
        return

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    _worker_started.set()
