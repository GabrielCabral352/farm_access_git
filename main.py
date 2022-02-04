from random import randint
import os

for i in range(50):
    with open("commiter.txt", "a") as file:
        file.write(str(randint(1,200000)))
        os.system("git add *")
        os.system(f'git commit -m "a{randint(1,200000)}ds"')
        os.system("git push origin main")
        file.close()

