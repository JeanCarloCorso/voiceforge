import os
import random
import subprocess
import uuid

from app.services.audio_postprocess import postprocess_audio
from app.services.emotion_segmenter import split_by_emotion
from app.services.prosody_enhancer import enhance_text
from app.services.silence import generate_silence, pause_duration
from app.services.text_sanitizer import sanitize_for_tts
from app.services.voice_presets import get_voice_preset


def generate_tts_pipeline(
    tts_model,
    texto,
    speaker_wav,
    output_dir
):
    segments = split_by_emotion(texto)
    temp_files = []

    for i, seg in enumerate(segments):
        temp_path = os.path.join(
            output_dir, f"_seg_{uuid.uuid4()}.wav"
        )

        preset = get_voice_preset(seg["emotion"])

        preset["speed"] *= random.uniform(0.97, 1.03)

        expressive_text = enhance_text(
            seg["text"],
            seg["emotion"]
        )

        expressive_text = enhance_text(seg["text"], seg["emotion"])
        expressive_text = sanitize_for_tts(expressive_text)

        if not expressive_text:
            continue

        tts_model.tts_to_file(
            text=expressive_text,
            speaker_wav=speaker_wav,
            file_path=temp_path,
            language="pt",
            enable_text_splitting=False,
            **preset
        )

        temp_files.append(temp_path)

        # ⏸️ pausa real (exceto último)
        if i < len(segments) - 1:
            silence = generate_silence(
                pause_duration(seg["emotion"]),
                output_dir
            )
            temp_files.append(silence)

    file_name = f"audio_{uuid.uuid4()}.wav"
    final_path = os.path.join(
        output_dir, file_name
    )

    cmd = ["ffmpeg", "-y"]
    for f in temp_files:
        cmd += ["-i", f]

    cmd += [
        "-filter_complex",
        f"concat=n={len(temp_files)}:v=0:a=1",
        final_path
    ]

    subprocess.run(cmd, check=True)

    for f in temp_files:
        os.remove(f)

    postprocess_audio(final_path)

    return file_name
