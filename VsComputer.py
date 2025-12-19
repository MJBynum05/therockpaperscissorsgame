import random


class VsComputer:
    def start(self):
        print ("Starting game vs computer...")
        self.person = person 

        person = input("Choose rock ('r'), paper ('p'), or scissors ('s'): ")
        computer = random.choice(['r', 'p', 's'])

        print("Computer chose: " + computer)

        if computer == 'r' and person == 's':
            print("You Lose!")
        elif computer == 's' and person == 'p':
            print("You Lose!")
        elif computer == 'p' and person == 'r':
            print("You Lose!")
        elif computer == 's' and person == 'r':
            print("You Win!")
        elif computer == 'p' and person == 's':
            print("You Win!")
        elif computer == 'r' and person == 'p':
            print("You Win!")
        elif computer == person:
            print("It's a tie!")
        else:
            print("Wrong Input!")

