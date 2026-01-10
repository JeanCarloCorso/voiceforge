import subprocess
import os

def postprocess_audio(input_wav: str) -> str:
    output_wav = input_wav.replace(".wav", "_final.wav")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_wav,
        "-af",
        (
            "acompressor=threshold=-18dB:ratio=2:attack=5:release=100,"
            "equalizer=f=3000:t=q:w=1:g=3,"
            "loudnorm=I=-14:LRA=7:TP=-1.5"
        ),
        output_wav
    ]

    subprocess.run(cmd, check=True)

    if os.path.exists(output_wav):
        os.replace(output_wav, input_wav)

    return input_wav
