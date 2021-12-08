import config

x = (random(config.WIN_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
y = (random(config.WIN_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
food_pos = [x, y]
food_img = None

def draw_food():
    fill(0, 255, 0)
    image(food_img, food_pos[0], food_pos[1], config.SCALE, config.SCALE)
    
    
def reset():
    x = (random(config.WIN_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
    y = (random(config.WIN_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
    food_pos[0] = x
    food_pos[1] = y
