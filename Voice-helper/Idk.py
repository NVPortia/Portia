import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


opts = {
    "names": ('бальдр', 'больдр', 'бесчувственный'),
    "tbr": ('скажи', 'покажи', 'расскажи', 'произнеси', 'повтори', 'сколько'),
    "commands": {
        "ctime": ('текущее время', 'время сейчас', 'который час', 'сейчас времени'),
        "radio": ('включи музыку'),
        "function_one": ('расскажи анекдот', 'хочу стать счастливым', 'давай шутку', 'завози кринжа', 'кринж в студию')
    }

}
# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_gogle(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["names"]):
            # обращение к Богу
            commands = voice

            for x in opts['names']:
                commands = commands.replace(x, "").strip()

            for x in opts['tbr']:
                commands = commands.replace(x, "").strip()

            # распознание и выполнение команды
            commands = recognizer_cmd(commands)
            execute_cmd(commands['commands'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка!")


def recognizer_cmd(commands):
    RC = {'commands': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(commands, x)
            if vrt > RC['percent']:
                RC['commands'] = c
                RC['percent'] = vrt
    return RC


def execute_cmd(commands):
    if commands == 'ctime':
        # время
        now = datetime.datetime.now()

        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif commands == 'radio':
        pass
    elif commands == 'function_one':
        speak("Нет не буду")
    else:
        print('Команда не распознана, либо её не существует')


# запуск
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

speak("Привет, создатель")
speak("Бальдр в внимание")

stop_listening = r.listen_in_background(mic, callback)
while True: time.sleep(0.1)