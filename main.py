for i in range(10):
    with open("commiter.txt", "a") as file:
        file.write(str(i))
        file.close()

