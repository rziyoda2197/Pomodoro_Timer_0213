import os
import platform

def beep():
    system = platform.system()

    if system == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        os.system("printf '\a'")
