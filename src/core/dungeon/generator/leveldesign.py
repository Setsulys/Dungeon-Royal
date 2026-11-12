

# level design

## size of maze expand
### 15 + 5* level of character
### limited to 51 of size
## monster about 5% of the maze
##treasure





def compute_element_from_character_level(level):
    # Level design dungeon spread with level but,caped (after level 7)
    raw_size = 15 +(5*level)
    final_size = min(raw_size, 51) if min(raw_size, 51) % 2 == 1 else min(raw_size, 51) + 1
    if final_size < 51:
        M = round(15 + (5 * level) + (2.1 * (level ** 2)))
        T = 15 + (5 * level)
    else:
        T=50
        M=min(250,145+(15*(level-7)))
    return final_size,M,T