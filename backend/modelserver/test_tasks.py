from celery_app import app

from tts_modules import normalize_multiline_text
from TTS.TTS.utils.synthesizer import Synthesizer

print('synthesizer start!')
synthesizer = Synthesizer(
    f"./voice_model/glow-tts/5/5g_checkpoint_30000.pth.tar",
    f"./voice_model/glow-tts/5/5g_config.json",
    None,
    f"./voice_model/hifigan-v2/5/5h_checkpoint_305000.pth.tar",
    f"./voice_model/hifigan-v2/5/5h_config.json",
    None,
    None,
    False,)
symbol = synthesizer.tts_config.characters.characters  # normalize_text가 호출될 때 필요한 변수
print('synthesizer finished!')

@app.task(name="test")
def test(id, txt):
    count = 0
    for text in normalize_multiline_text(txt, symbol):
        wav = synthesizer.tts(text, None, None)
        synthesizer.save_wav(wav, f'./{id}_sample_{count}.wav')   # change wav to .wav file
        count+=1

