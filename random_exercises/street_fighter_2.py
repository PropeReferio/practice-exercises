# From codewars.com Street Fighter 2 - Character selection. Other more elegant solutions on the discussion page.
# A nice struggle with this kata. Notes below:

def street_fighter_selection(fighters, init_pos, moves):
    fighter_pos = {(0,0) : fighters[0][0], #Assigns values from list within list
                  (1,0) : fighters[0][1], #Key is position of character, a tuple because lists can't be keys
                  (2,0) : fighters[0][2],
                  (3,0) : fighters[0][3],
                  (4,0) : fighters[0][4],
                  (5,0) : fighters[0][5],
                  (0,1) : fighters[1][0], 
                  (1,1) : fighters[1][1],
                  (2,1) : fighters[1][2],
                  (3,1) : fighters[1][3],
                  (4,1) : fighters[1][4],
                  (5,1) : fighters[1][5],
                  }
    pos = [init_pos[0], init_pos[1]] #Converts init_pos (a tuple) into a list, so it can be mutated
    n = [] 
    for move in moves:
        if move == 'right':
            if pos[0] == 5: #If at far right of menu, right takes you to left side...
                pos[0] = 0 #Others: cur_pos[1] = (cur_pos[1] + 1) % 6
            else:
                pos[0] += 1
            n.append(fighter_pos[(pos[0], pos[1])]) #Uses indices from pos (a list) to create a tuple key from dictionary, and add fighters name to list
        elif move == 'left':
            if pos[0] == 0: #And vice versa
                pos[0] = 5 #Others used this: cur_pos[1] = (cur_pos[1] - 1) % 6
            else:
                pos[0] -= 1
            n.append(fighter_pos[(pos[0], pos[1])])
        elif move == 'up':
            pos[1] = 0
            n.append(fighter_pos[(pos[0], pos[1])])
        else: # if move == 'down'
            pos[1] = 1
            n.append(fighter_pos[(pos[0], pos[1])])
            #Others: selected_fighters.append(fighters[cur_pos[0]][cur_pos[1]]) Must have y, x rather than x, y
            #Much less code this way
    return n

moves =  ["up","left","down","right"]*2
fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
init_pos = (0,0)

print(street_fighter_selection(fighters, init_pos, moves))
print(-1 % 6)