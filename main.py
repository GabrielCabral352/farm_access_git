from random import randint
from multiprocessing import Process
import os




def sendCommit():
    with open("commiter.txt", "a") as file:
        file.write(str(randint(1,200000)))
        os.system("git add *")
        os.system(f'git commit -m "a{randint(1,200000)}ds"')
        os.system("git push origin main")
        file.close()
        
if __name__ == '__main__':
    for i in range(10):
        Process(target=sendCommit).start()
   