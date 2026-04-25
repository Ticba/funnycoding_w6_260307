# 打字機
import sys, time, os

def colortext(color="白", text=""):
    if color=="白":
        return f"\033[37m{text}\033[0m"
    elif color=="天藍":
        return f"\033[36m{text}\033[0m"
#改顏色
"\033[30m黑色字\033[0m"
"\033[31m紅色字\033[0m"
"\033[32m綠色字\033[0m"
"\033[33m黃色字\033[0m"
"\033[34m藍色字\033[0m"
"\033[35m紫色字\033[0m"
"\033[36m天藍字\033[0m"
"\033[37m白色字\033[0m"


def typewriter(text, color="白", delay=0.05):
    for c in text:
        sys.stdout.write(colortext(color,c))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # 換行


if __name__ == "__main__":
    typewriter("helloehlelkjeljke", color="天藍")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    
