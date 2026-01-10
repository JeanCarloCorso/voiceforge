import os
import uuid
import subprocess
from app.services.emotion_segmenter import split_by_emotion
from app.services.voice_presets import get_voice_preset
from app.services.audio_postprocess import postprocess_audio


def generate_tts_pipeline(
    tts_model,
    texto,
    speaker_wav,
    output_dir
):
    segments = split_by_emotion(texto)
    temp_files = []

    for seg in segments:
        temp_path = os.path.join(
            output_dir, f"_seg_{uuid.uuid4()}.wav"
        )

        preset = get_voice_preset(seg["emotion"])

        tts_model.tts_to_file(
            text=seg["text"],
            speaker_wav=speaker_wav,
            file_path=temp_path,
            language="pt",
            enable_text_splitting=False,
            **preset
        )

        temp_files.append(temp_path)

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
