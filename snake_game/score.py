import config

scr = 0
high_score = 0

def show():
    fill(255)
    textSize(25)
    text("Score:" + str(scr), 20, 40)
    text("Highscore:" + str(high_score), 20, 70)


def set_high_score():
    if scr > high_score:
        with open(config.HIGHSCORE_FILE_PATH, 'w') as file:
            file.write(str(scr))
