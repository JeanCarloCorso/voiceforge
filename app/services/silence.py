import os
import subprocess
import uuid

SAMPLE_RATE = 22050


def generate_silence(duration: float, output_dir: str) -> str:
    """
    Gera um wav de silêncio real.
    """
    path = os.path.join(output_dir, f"_silence_{uuid.uuid4()}.wav")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
        "-t", str(duration),
        path
    ]

    subprocess.run(cmd, check=True)
    return path


def pause_duration(emotion: str) -> float:
    """
    Duração de pausa por emoção.
    """
    return {
        "calm": 0.35,
        "sad": 0.40,
        "neutral": 0.25,
        "happy": 0.15,
        "angry": 0.10,
        "anxious": 0.20,
    }.get(emotion, 0.25)
