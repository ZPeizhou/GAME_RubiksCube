def whether_the_game_is_over(UP_COLOR,DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    puzzle=0
    for i in range (3):
        for j in range (3):
            if UP_COLOR[i][j]==UP_COLOR[1][1] and DOWN_COLOR[i][j]==DOWN_COLOR[1][1] and LEFT_COLOR[i][j]==LEFT_COLOR[1][1] and RIGHT_COLOR[i][j]==RIGHT_COLOR[1][1] and FRONT_COLOR[i][j]==FRONT_COLOR[1][1] and BACK_COLOR[i][j]==BACK_COLOR[1][1]:
                puzzle=puzzle+1
    return puzzle
