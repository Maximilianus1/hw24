import threading
import time
import random


def create_file():
    time.sleep(1)
    file=open("file.txt","w")
    file.write(str(random.randint(0,100)))
    file.close()
    return "file created"
threads=[]
a=""
if __name__=='__main__':
    timeStart = time.time()
    for i in range(1000):
        local_thread = threading.Thread(target=create_file)
        local_thread.start()
        threads.append(local_thread)
    print(str(threads))
    timeFinish=time.time()
    timeElapsed=timeFinish-timeStart
    print(timeElapsed)
