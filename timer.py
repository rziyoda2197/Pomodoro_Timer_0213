import time
from sound import beep


def countdown(minutes, label):
    seconds = minutes * 60

    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"\r{label} {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1

    print()
    beep()
