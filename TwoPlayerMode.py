import os

class TwoPlayerMode:
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def start(self):
        print("Starting two player game...")

        person1 = input("Player 1, choose rock ('r'), paper ('p'), or scissors ('s'): ")
        self.clear()
        input("\nPass to Player 2, press ENTER when ready...")

        person2 = input("Player 2, choose rock ('r'), paper ('p'), or scissors ('s'): ")
        self.clear()

        if person1 == 'r' and person2 == 's':
            print("Person 1 Wins!")
        elif person1 == 's' and person2 == 'p':
            print("Person 1 Wins!")
        elif person1 == 'p' and person2 == 'r':
            print("Person 1 Wins!")
        elif person2 == 'r' and person1 == 's':
            print("Person 2 Wins!")
        elif person2 == 's' and person1 == 'p':
            print("Person 2 Wins!")
        elif person2 == 'p' and person1 == 'r':
            print("Person 2 Wins!")
        elif person1 == person2:
            print("It's a tie!")
        else:
            print("Wrong Input!")
