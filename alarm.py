import threading
import multiprocessing
from playsound import playsound
import datetime
import time

# time_alarm = datetime.time(20, 40, 0, 0)
time_start = datetime.time(0, 0, 0, 0)
time_stop = datetime.time(20, 45, 0, 0)

def playMusic():
    while True:
        t = threading.Thread(target = playsound, args = ("music.mp3", ))
        t.start()
        t.join()
        time.sleep(0.01)

def playVoice():
    playsound("voice.mp3")

def main():
    while datetime.datetime.now().time() <= time_start:
        time.sleep(1)

    proc_music = multiprocessing.Process(target = playMusic)
    proc_voice = multiprocessing.Process(target = playVoice)

    proc_music.start()
    proc_voice.start()
    
    try:
        while datetime.datetime.now().time() <= time_stop:
            time.sleep(1)
    finally:
        proc_music.terminate()
        proc_voice.terminate()

if __name__ == "__main__":
    main()