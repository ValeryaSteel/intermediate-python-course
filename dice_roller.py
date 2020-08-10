import random
def main():
  diceRolls = 2
  dice_sum = 0
  for i in range(0, diceRolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum+ roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')



if __name__== "__main__":
  main()