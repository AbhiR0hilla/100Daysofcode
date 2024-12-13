import random
import time
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
def cards():                        #random card assignment
    cards=[1,2,3,4,5,6,7,8,9,10,10,11]
    return random.sample(cards,2)

gameover=False
human=cards()
computer=cards()
def calculate(score,comscore):
    if score > 22:                  #calculating who won the game
        time.sleep(0.3)
        return 'you lose,by overdraw'
    elif comscore>21:
        return 'you win because dealer overdrew'
    elif score > comscore:
        time.sleep(0.3)
        return 'you win!!'
    elif comscore>score:
        return 'you lose'
    elif score==comscore:
        return ' its a draw'
    return 0
def blackjackgame():
    choice1 = input(color.BOLD + "Do you want to play BLACKJACK? (yes/no): " + color.END).lower()
    if choice1 in ('y', ""):
        # Initialize hands
        human = [random.choice(cards()), random.choice(cards())]
        computer = [random.choice(cards()), random.choice(cards())]
        print("Your cards:", human)
        print("Computer's visible card:", computer[0],",??")
        score = sum(human)
        comscore = sum(computer)
        while True and score<22:
            if score == 21 and len(human) == 2:
                print(color.BOLD+'YOU GOT THE BLACKJACK!!'+color.END)
                break
            choice = input(color.BOLD + "Do you want to hit or stand? " + color.END).lower()
            if choice == "hit":
                human.append(random.choice(cards()))        # Player draws a card
                score = sum(human)
                print("Your cards:", human, "Current score:", score)
                print("Dealer visible cards are: ",random.sample(computer, 2))
                if score<22:
                    continue
                elif comscore < 18:
                    computer.append(random.choice(cards()))
                    print("Dealers hand is: ", random.sample(computer, 2))
                    comscore = sum(computer)
            elif choice == "stand":
                while comscore < 18:
                    computer.append(random.choice(cards()))
                    comscore = sum(computer)
                    print("Your cards are:", human, "Dealer's cards:", random.sample(computer,2))
                print(calculate(score,comscore))
                # After the dealer's turn, calculate the result
                break
            else:
                print("Invalid choice! Please choose 'hit' or 'stand'.")
        else:
            print('You lost,Better luck next time!')
    else:
        print("Better luck next time!")

blackjackgame()
