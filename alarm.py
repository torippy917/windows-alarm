import threading
import multiprocessing
from playsound import playsound
import datetime
import time

time_alarm = datetime.time(20, 40, 0, 0)
# time_stop = datetime.time(20, 45, 0, 0)
time_stop = datetime.time(23, 59, 0, 0)

def playMusic():
    # while True:
    #     t = threading.Thread(target = playsound, args = ("hotaru.mp3", ))
    #     t.start()
    #     t.join()
    #     time.sleep(0.01)
    while True:
        playsound("ding.wav")
        time.sleep(0.01)

def playVoice():
    pass

def main():
    while datetime.datetime.now().time() <= time_alarm:
        time.sleep(1)

    proc = multiprocessing.Process(name = "hotaru_music", target = playMusic)
    proc.start()
    try:
        while datetime.datetime.now().time() <= time_stop:
            time.sleep(1)
            pass
    finally:
        proc.terminate()

if __name__ == "__main__":
    main()