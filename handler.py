import runpod
from TTS.api import TTS

# Load FastPitch (fast + light)
MODEL = TTS("tts_models/en/ljspeech/fastpitch").to("cuda")

def handler(event):
    text = event.get("text", "")
    if not text:
        return {"error": "text is required"}

    output_path = "/tmp/output.wav"
    MODEL.tts_to_file(text=text, file_path=output_path)

    return runpod.File(path=output_path)

runpod.serverless.start({"handler": handler})

