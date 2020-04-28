#Codewars Kata: 80's Kids #6: Rock 'emm sock 'em robots... instructions online

def fight(robot_1, robot_2, tactics):
    #1: Determine turn order... make sure robot_1 goes first if tied for speed
    #Store fast robot in fast, slow robot in slow...
    if robot_1['speed'] > robot_2['speed']:
        fast, slow = robot_1, robot_2
    elif robot_2['speed'] > robot_1['speed']:
        fast, slow = robot_2, robot_1
    else:
        fast, slow = robot_1, robot_2

    #2: Execute tactics in order, checking for 'health' < 0 after each attack

    while robot_1["health"] > 0 and robot_2["health"] > 0 and (robot_1['tactics'] or robot_2['tactics']):
        if fast['tactics']:
            slow['health'] -= tactics[fast['tactics'][0]]
            del fast['tactics'][0]
            if slow['health'] <= 0:
                break
        if slow['tactics']:
            fast['health'] -= tactics[slow['tactics'][0]]
            del slow['tactics'][0]
            if fast['health'] <= 0:
                break
    
    #3: If they both run out of tactics, you need to break the while loop and return the name
    #of the bot with greater health. Otherwise, you could pop the tactics off, and add
    # and robot_1('tactics') or robot_2('tactics') returns False if neither bot has any moves
    
    #4 Once we've exited the while loop, return winner, or "The fight was a draw."
    if fast['health'] < slow['health']: return f"{slow['name']} has won the fight."
    elif slow['health'] < fast['health']: return f"{fast['name']} has won the fight."
    else: return 'The fight was a draw.'

#Sample Input: 
robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
    