import time
import winsound
import sys



duration = int(input("how long do you want to sleep for?"));

time.sleep(duration);
print("WAKE UP");
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
