import random
number = random.randint(1, 6)
print(number)


def Dice_Roll():
    roll = random.randint(1, 6)
    return roll




def player_turn():




    turn_score = 0
    while True:


        decision = input("to roll press 'r' to hold press 'q'")
        if decision == "r":
            result = Dice_Roll()
            if result == 1:
                print("you rolled a 1")
                turn_score = 0 
                
                return turn_score
            else:
                
                print("you rolled ", result )
                turn_score = turn_score + result


        else:
            print("you got ", turn_score,  " points this turn")
            return turn_score

def pc_turn():
    turn_score = 0
    while True:
        result = Dice_Roll()
        if result == 1:
            turn_score = 0

            return turn_score

        else:
            turn_score = turn_score + result









player_score = 0


while player_score < 50:
    player_score = player_turn() + player_score
    print("you have ", player_score, "points in total")
