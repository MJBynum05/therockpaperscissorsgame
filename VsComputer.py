import random
import keyboard

class VsComputer:
    def start(self):
        print ("Starting game vs computer...")
        person = input("Choose rock ('r'), paper ('p'), or scissors ('s'):  ")
        computer = random.choice(['r', 'p', 's'])

        print("Computer chose: " + computer)

     
        if computer == 'r' and person == 's':
            print("You Lose! Press t to restart game or 'q' to quit.")
        elif computer == 's' and person == 'p':
            print("You Lose! Press t to restart game or 'q' to quit.")
        elif computer == 'p' and person == 'r':
            print("You Lose! Press t to restart game or 'q' to quit.")
        elif computer == 's' and person == 'r':
            print("You Win! Press t to restart game or 'q' to quit.")
        elif computer == 'p' and person == 's':
            print("You Win! Press t to restart game or 'q' to quit.")
        elif computer == 'r' and person == 'p':
            print("You Win! Press t to restart game or 'q' to quit.")
        elif computer == person:
            print("It's a tie! Press t to restart game or 'q' to quit.")
        else:
            print("Wrong Input! Press t to restart game or 'q' to quit.")
        return

