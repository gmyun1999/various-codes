import random

def change_choice():
    door = ['a', 'b', 'c']
    car = random.choice(door)
    dict = {}
    dict[car] = 'car'
    for i in range(len(door)):
        if door[i] is not car:
            dict[door[i]] = 'goat'
    participant = random.choice(door)

    door.remove(participant)
    if participant == car:
        opendoor = random.choice(door)
        door.remove(opendoor)
    else:
        if dict[door[0]] == 'car':
            opendoor = door[1]
            door.remove(opendoor)
        else:
            opendoor = door[0]
            door.remove(opendoor)

    if dict[door[0]] == 'car':
        return 1
    else:
        return 0

n = int(input())
cnt = 0
for i in range(n):
    cnt += change_choice()
print(cnt)
