import time, subprocess, vlc
timecount = 5	
while timecount > 0:
	print(timecount)
	time.sleep(1)
	timecount -=1

p = vlc.MediaPlayer("/Users/davidguo/Documents/Pythom/alarm.wav")
p.play()