from datetime import datetime
import time
def task():
    with open("time_log.txt","a") as f:
        f.write(f"script run at : {datetime.now()}\n")
        print(f'task run at :{datetime.now()}')

while True:
    task()
    time.sleep(10)

