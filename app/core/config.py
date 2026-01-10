import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SPEAKERS_DIR = os.path.join(BASE_DIR, "speakers")
OUTPUT_DIR = os.path.join(BASE_DIR, "audios_gerados")

os.makedirs(SPEAKERS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
