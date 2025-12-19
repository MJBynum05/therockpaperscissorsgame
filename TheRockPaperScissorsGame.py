from TwoPlayerMode import TwoPlayerMode
from VsComputer import VsComputer

user = input("Choose your game mode: (1) Vs Computer , (2) Two Player Game   ")

if user == '1':
    game = VsComputer()
    game.start()
elif user == '2':
    game = TwoPlayerMode()
    game.start()
else:
    print("Invalid input. Please choose 1 or 2.")

