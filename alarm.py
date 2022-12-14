from pygame import mixer
import datetime
import time

time_alarm = datetime.time(20, 40, 0, 0)
play_dtime = datetime.timedelta(minutes=5)

def main():
    while datetime.datetime.now().time() <= time_alarm:
        time.sleep(1)
    
    mixer.init()
    sound_music = mixer.Sound("music.mp3")
    sound_voice = mixer.Sound("voice.mp3")

    sound_music.play(-1)
    sound_voice.play()

    time.sleep(play_dtime.seconds)

    mixer.fadeout(5000)

    while mixer.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()