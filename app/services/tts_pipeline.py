import os
import uuid
import subprocess
from app.services.preprocess_text import preprocess_text
from app.services.text_splitter import split_text
from app.services.voice_presets import get_voice_preset
from app.services.audio_postprocess import postprocess_audio


def generate_tts_pipeline(
    tts_model,
    texto,
    speaker_wav,
    output_dir,
    mode="natural"
):
    texto = preprocess_text(texto)
    chunks = split_text(texto)

    preset = get_voice_preset(mode)
    temp_files = []

    for chunk in chunks:
        temp_path = os.path.join(
            output_dir, f"_chunk_{uuid.uuid4()}.wav"
        )

        tts_model.tts_to_file(
            text=chunk,
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

    concat_cmd = ["ffmpeg", "-y"]
    for f in temp_files:
        concat_cmd += ["-i", f]

    concat_cmd += [
        "-filter_complex",
        f"concat=n={len(temp_files)}:v=0:a=1",
        final_path
    ]

    subprocess.run(concat_cmd, check=True)

    for f in temp_files:
        os.remove(f)

    postprocess_audio(final_path)

    return file_name
