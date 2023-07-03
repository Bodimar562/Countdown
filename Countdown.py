import time
def countdown(secons):
    while secons > 0:
        minutes,seconds =divmod(secons,60)
        secons -= 1
        print(minutes,"minutes ",seconds,"seconds remained")
        time.sleep(1)

secons=input("kaç saniye kaldı ?")
countdown(int(secons))
print("The time is over!!!")