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
        if turn_score < 20:
            result = Dice_Roll()
            if result == 1:
                turn_score = 0

                return turn_score

            else:
                turn_score = turn_score + result
        
        else:
            print("the computer got", turn_score, "points this turn")
            return turn_score









player_score = 0
robot_score = 0

while True:
    player_score = player_turn() + player_score
    print("you have ", player_score, "points in total")
    if player_score > 49:
        print("you win")
        break



    robot_score = pc_turn() + robot_score
    print("the robot has ", robot_score, "points in total")
    if robot_score > 49:
        print("the robot won")
        break
