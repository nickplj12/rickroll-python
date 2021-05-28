import subprocess as cmd
import time

print("CD to C:\Program Files\VideoLAN\VLC.")
time.sleep(5)
command = 'vlc https://www.youtube.com/watch?v=dQw4w9WgXcQ'
cmd.run(command, shell=True)