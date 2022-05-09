from yaspin import yaspin
import os
import time


@yaspin(text="please be patient ..")
def waiting(waiting_time):
    time.sleep(waiting_time)

def screen_wipe():
    os.system('clear')
    print("Your process has been completed")
