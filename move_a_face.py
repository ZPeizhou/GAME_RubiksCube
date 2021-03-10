from rotate_a_face import rotate_the_face_CW
from rotate_a_face import rotate_the_face_ACW

def move_the_right_face_CW(RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR):
    RIGHT_COLOR=rotate_the_face_CW(RIGHT_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[i][2]
        FRONT_COLOR[i][2]=DOWN_COLOR[i][2]
        DOWN_COLOR[i][2]=BACK_COLOR[2-i][0]
        BACK_COLOR[2-i][0]=UP_COLOR[i][2]
        UP_COLOR[i][2]=temp[i]
    return RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR

def move_the_right_face_ACW(RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR):
    RIGHT_COLOR=rotate_the_face_ACW(RIGHT_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[i][2]
        FRONT_COLOR[i][2]=UP_COLOR[i][2]
        UP_COLOR[i][2]=BACK_COLOR[2-i][0]
        BACK_COLOR[2-i][0]=DOWN_COLOR[i][2]
        DOWN_COLOR[i][2]=temp[i]
    return RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR

def move_the_left_face_CW(FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR):
    FRONT_COLOR=rotate_the_face_CW(FRONT_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=LEFT_COLOR[i][2]
        LEFT_COLOR[i][2]=DOWN_COLOR[0][i]
        DOWN_COLOR[0][i]=RIGHT_COLOR[2-i][0]
        RIGHT_COLOR[2-i][0]=UP_COLOR[2][2-i]
        UP_COLOR[2][2-i]=temp[i]
    return FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR

def move_the_left_face_ACW(FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR):
    FRONT_COLOR=rotate_the_face_ACW(FRONT_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=LEFT_COLOR[i][2]
        LEFT_COLOR[i][2]=UP_COLOR[2][2-i]
        UP_COLOR[2][2-i]=RIGHT_COLOR[2-i][0]
        RIGHT_COLOR[2-i][0]=DOWN_COLOR[0][i]
        DOWN_COLOR[0][i]=temp[i]
    return FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR

def move_the_up_face_CW(UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    UP_COLOR=rotate_the_face_CW(UP_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[0][i]
        FRONT_COLOR[0][i]=RIGHT_COLOR[0][i]
        RIGHT_COLOR[0][i]=BACK_COLOR[0][i]
        BACK_COLOR[0][i]=LEFT_COLOR[0][i]
        LEFT_COLOR[0][i]=temp[i]
    return UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR

def move_the_up_face_ACW(UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    UP_COLOR=rotate_the_face_ACW(UP_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[0][i]
        FRONT_COLOR[0][i]=LEFT_COLOR[0][i]
        LEFT_COLOR[0][i]=BACK_COLOR[0][i]
        BACK_COLOR[0][i]=RIGHT_COLOR[0][i]
        RIGHT_COLOR[0][i]=temp[i]
    return UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR

def move_the_down_face_CW(DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    DOWN_COLOR=rotate_the_face_CW(DOWN_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[2][i]
        FRONT_COLOR[2][i]=LEFT_COLOR[2][i]
        LEFT_COLOR[2][i]=BACK_COLOR[2][i]
        BACK_COLOR[2][i]=RIGHT_COLOR[2][i]
        RIGHT_COLOR[2][i]=temp[i]
    return DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR

def move_the_down_face_ACW(DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    DOWN_COLOR=rotate_the_face_ACW(DOWN_COLOR)
    temp=[' ',' ',' ']
    for i in range (3):
        temp[i]=FRONT_COLOR[2][i]
        FRONT_COLOR[2][i]=RIGHT_COLOR[2][i]
        RIGHT_COLOR[2][i]=BACK_COLOR[2][i]
        BACK_COLOR[2][i]=LEFT_COLOR[2][i]
        LEFT_COLOR[2][i]=temp[i]
    return DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR
