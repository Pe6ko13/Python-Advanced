import config
from copy import deepcopy
import food

head_img = None
snake_pos = [[0, 0], [config.SCALE, 0], [config.SCALE*2, 0]]


def show():
    
    image(head_img, snake_pos[-1][0], snake_pos[-1][1], config.SCALE, config.SCALE)

    
    for segment in snake_pos[:-1]:
        fill(0, 500, 0)
        rect(segment[0], segment[1], config.SCALE, config.SCALE)
  
              
def check_edges():
    head = snake_pos[-1]
    if head[1] < 0:
        head[1] = config.WIN_HEIGHT
    elif head[1] >= config.WIN_WIDTH:
        head[1] = 0
    elif head[0] < 0:
        head[0] = config.WIN_WIDTH
    elif head[0] >= config.WIN_WIDTH:
        head[0] = 0
    
    
def move():
    current_changes = config.DIRECTIONS[config.CURRENT_DIR]
    snake_copy = deepcopy(snake_pos)
    snake_pos[-1][0] += current_changes[0]
    snake_pos[-1][1] += current_changes[1]
    
    for i in range(len(snake_pos) -2, -1, -1):
        snake_pos[i] = snake_copy[i + 1]
        
    check_edges()
    
def touch_food():
    return snake_pos[-1] == food.food_pos


def eat_food():
    snake_pos.insert(0, snake_pos[0])
    
    
def eats_self():
    head = snake_pos[-1]
    return any(segment == head for segment in snake_pos[:-1])
