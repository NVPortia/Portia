import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'
put_accent = True
put_yoo = True
device = torch.device('cpu')
text = "Привет"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)

audio = model.apply_tts(text=text,
                        speaker=speaker,
                        sapmle_rate=sample_rate,
                        put_accent=put_accent,
                        put_yoo=put_yoo)

# вопроизведение
print(text)

sd.play(audio, sample_rate)
time.sleep(len(audio) / sample_rate)
sd.stop()