import random

total1 = 0
total2 = 0
first = input("Enter player one's name: ")
second = input("Enter player two's name: ")

loop = 0
games = int(input("How many games would you like to play?: "))
while loop < games:
    loop += 1
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)
    print("Player one: " + str(player1) + "  Player two: " + str(player2))
    total1 = total1 + player1
    total2 = total2 + player2

print(first + " total: " + str(total1))
print(second + " total: " + str(total2))
if total1 > total2:
    print(first + " wins")
else:
    print(second + " wins")
    
    
