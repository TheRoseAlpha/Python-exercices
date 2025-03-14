import time

'''create a function to take time in seconds and print it out in a formatted string'''


def time_sec(seconds):
    
    hour = int(seconds/3600)
    rest_1 = seconds % 3600
    minutes = int(rest_1/60)
    rest_2 = rest_1 % 60
    seconds = rest_2

    print(f"{hour}h {minutes}m {seconds}s")

seconds_user = int(input("Insert the seconds for your timer: "))


for i in range(seconds_user):
    time_sec(seconds_user)
    time.sleep(1)
    seconds_user -= 1
print("Time's up!🔔")




