import time

def decorator(func):
    def wwrapper():
        print("FUNCTION START ALERT!!!")
        time1 = time.time()
        temp = func()
        time2 = time.time()
        print(f"{time2 - time1}")
        print("FUNCTION END ALERT!!!")
        return f"RETURN is: {temp}"
    return wwrapper

@decorator
def paris():
    print("ya v paxije")
    return "Masik"

print(paris(), "\n\n")
paris()