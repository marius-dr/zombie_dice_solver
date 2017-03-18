import random

red_dice = 3
yellow_dice = 4
green_dice = 6
green = 1/6 #["3B", "2F", "1S"] 50% good, 1/6 bad
yellow = 1/3 #["2B", "2F", "2S"] 1/3 good, 1/3 bad
red = 1/2 #["1B", "2F", "3S"] 1/6 good, 50% bad
dice_hand = []
result = []
brain_pool = []
shotgun_pool = []


def prob_shotgun():
    return (green_dice * green + yellow_dice * yellow + red_dice * red) / (green_dice + yellow_dice + red_dice)


def fill_dice(current_nr=0):
    temp_g_pool = green_dice
    temp_y_pool = yellow_dice
    temp_r_pool = red_dice
    while current_nr < 3:
        remaining_dice = temp_g_pool + temp_y_pool + temp_r_pool
        pick = int(random.randint(1, remaining_dice + 1))
        if red_dice > 0:
            if pick in (1, temp_r_pool):
                dice_hand.append("R")
                current_nr = len(dice_hand)
                temp_r_pool -= 1
                continue
        if yellow_dice > 0:
            if pick in (red_dice + 1, temp_r_pool + temp_y_pool):
                dice_hand.append("Y")
                current_nr = len(dice_hand)
                temp_y_pool -= 1
                continue
        dice_hand.append("G")
        temp_g_pool -= 1
        current_nr = len(dice_hand)


def roll_green():
    roll = int(random.randint(1, 6))
    if roll in [1, 2, 3]:
        return "B"
    if roll in [4,5]:
        return "F"
    return "S"


def roll_yellow():
    roll = int(random.randint(1, 6))
    if roll in [1, 2]:
        return "B"
    if roll in [4,5]:
        return "F"
    return "S"


def roll_red():
    roll = int(random.randint(1, 6))
    if roll in [1]:
        return "B"
    if roll in [4, 5]:
        return "F"
    return "S"


while len(shotgun_pool) < 3 and len(brain_pool) < 13:
    print("Probability 1S before drawing the hand: " + str(round(prob_shotgun() * 100, 2)))
    if len(shotgun_pool) == 0:
        prob_to_die = prob_shotgun() * prob_shotgun() * prob_shotgun() * 100
    elif len(shotgun_pool) == 1:
        prob_to_die = prob_shotgun() * prob_shotgun() * 100
    else:
        prob_to_die = prob_shotgun() * 100
    print("Probability to die before drawing the hand: " + str(round(prob_to_die, 2)))
    fill_dice(len(dice_hand))
    print("Hand:" + str(dice_hand))
    new_hand = []
    for each_die in dice_hand:
        if each_die == "G":
            temp = roll_green()
            if temp != "F":
                green_dice -= 1
                if temp == "S":
                    shotgun_pool.append(each_die)
                else:
                    brain_pool.append(each_die)
            else:
                new_hand.append(each_die)
            result.append(temp)
        elif each_die == "Y":
            temp = roll_yellow()
            if temp != "F":
                yellow_dice -= 1
                if temp == "S":
                    shotgun_pool.append(each_die)
                else:
                    brain_pool.append(each_die)
            else:
                new_hand.append(each_die)
            result.append(temp)
        elif each_die == "R":
            temp = roll_red()
            if temp != "F":
                red_dice -= 1
                if temp == "S":
                    shotgun_pool.append(each_die)
                else:
                    brain_pool.append(each_die)
            else:
                new_hand.append(each_die)
            result.append(temp)

    print("Result" + str(result))
    result = []
    print("Brains: " + str(len(brain_pool)) + "\nShots: " + str(len(shotgun_pool)))


    dice_hand = new_hand
