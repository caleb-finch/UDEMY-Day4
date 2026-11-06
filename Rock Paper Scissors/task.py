import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
player = int(input("What do you play? 0 = rock, 1 = paper, or 2 = scissors: "))
cpu = random.randint(0,2)

print(images[player])
print("Computer chose:")
print(images[cpu])

if player == cpu:
    print("It's a draw LAMEEEEEE")

elif player == 0 and cpu == 2:
    print("Player won!")

elif player == 2 and cpu == 0:
    print("Computer won!")

elif player > cpu:
    print("Player won!")

elif player < cpu:
    print("Computer won!")

# if player == 1:
#     print(rock)
#
#     if cpu == 1:
#         print("Computer chose:")
#         print(rock)
#         print("It's a draw!")
#
#     if cpu == 2:
#         print("Computer chose:")
#         print(paper)
#         print("Computer won!")
#
#     if cpu == 3:
#         print("Computer chose:")
#         print(scissors)
#         print("You won!")
#
# elif player == 2:
#     print(paper)
#
#     if cpu == 1:
#         print("Computer chose:")
#         print(rock)
#         print("you wom!")
#
#     if cpu == 2:
#         print("Computer chose:")
#         print(paper)
#         print("It's a draw!")
#
#     if cpu == 3:
#         print("Computer chose:")
#         print(rock)
#         print("Computer won!")
#
# elif player == 2:
#     print(paper)
#
#     if cpu == 1:
#         print("Computer chose:")
#         print(rock)
#         print("you wom!")
#
#     if cpu == 2:
#         print("Computer chose:")
#         print(paper)
#         print("It's a draw!")
#
#     if cpu == 3:
#         print("Computer chose:")
#         print(rock)
#         print("Computer won!")