from time import sleep
for c in range(0, 51, 2):
    if c % 2 == 0:
        print(c, end=' ')
        sleep(1)
print('fim')

