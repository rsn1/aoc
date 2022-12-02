

SHAPESCORE = {'X': 1, 'Y': 2, 'Z': 3}
SHAPESCORE_OPP = {'A' : 1, 'B': 2, 'C': 3}
win_dict = {1:2,2:3,3:1}
lose_dict = {1:3,2:1,3:2}
def solve2(input):
    total_score = 0
    with open(input) as f:
        for line in f:
            game = line.split()
            opp_score = SHAPESCORE_OPP[game[0]]
            game_outcome = game[-1]
            if game_outcome == 'X': #lose:
                total_score += lose_dict[opp_score]
            elif game_outcome == 'Y': #draw
                total_score += 3 + opp_score
            else: #win
                total_score += 6 + win_dict[opp_score]
    return total_score

def solve1(input):
    total_score = 0
    with open(input) as f:
        for line in f:
            game = line.split()
            opp_score = SHAPESCORE_OPP[game[0]]
            my_score = SHAPESCORE[game[-1]]  
            score_diff = my_score-opp_score
            if score_diff == 0: #draw
                total_score += 3 + my_score
            elif score_diff == 1 or score_diff == -2: #win 
                total_score += 6 + my_score
            else: #lost
                total_score += my_score
    return total_score

if __name__ == "__main__":
    output = solve1('input.txt')
    print(output)
    output = solve2('input.txt')
    print(output)