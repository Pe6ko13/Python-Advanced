import config
import snake
import food
import score


def end_screen():
    background(600)
    fill(255)
    textSize(64)
    text("GAME OVER", config.WIN_WIDTH / 4, config.WIN_HEIGHT / 2)


def setup():
    size(config.WIN_WIDTH, config.WIN_HEIGHT)
    frameRate(4)
    if os.path.exists(config.HIGHSCORE_FILE_PATH):
        with open(config.HIGHSCORE_FILE_PATH, 'r') as file:
            score.high_score = int(file.read())
    
    food.food_img = loadImage('Pictures/apple.png')
    snake.head_img = loadImage('Pictures/snake_head.png')
    
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.draw_food()
    score.show()
    
    if snake.touch_food():
        snake.eat_food()
        food.reset()
        score.scr += 1
        
    if snake.eats_self():
        print("GAME OVER")
        end_screen()
        score.set_high_score()
        noLoop()
                
        
def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != 'down':
        config.CURRENT_DIR = 'up'
    elif keyCode == DOWN and config.CURRENT_DIR != 'up':
        config.CURRENT_DIR = 'down'
    elif keyCode == RIGHT and config.CURRENT_DIR != 'left':
        config.CURRENT_DIR = 'right'
    elif keyCode == LEFT and config.CURRENT_DIR != 'right':
        config.CURRENT_DIR = 'left'



    
