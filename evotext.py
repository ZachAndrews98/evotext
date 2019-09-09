import string
import random
import time
import sys

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:/_'

# if len(sys.argv) >= 2:
#     target = ' '.join(sys.argv[1:])
# else:
#     print("Please enter a target word")
#     sys.exit()

target = str(input("Enter a word: "))

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")
