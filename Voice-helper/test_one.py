import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Скажи что-то ...")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-Ru")
print("Вы сказали " + query.lower())
