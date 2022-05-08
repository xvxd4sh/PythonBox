from yaspin import yaspin
import time


@yaspin(text="please be patient ..")
def waiting(waiting_time):
    time.sleep(waiting_time)
