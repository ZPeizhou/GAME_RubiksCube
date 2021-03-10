from rotate_a_face import rotate_the_face_CW
from rotate_a_face import rotate_the_face_ACW

def change_face_right(FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR,UP_COLOR,DOWN_COLOR):
    temp=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range (3):
        for j in range (3):
            temp[i][j]=FRONT_COLOR[i][j]
            FRONT_COLOR[i][j]=RIGHT_COLOR[i][j]
            RIGHT_COLOR[i][j]=BACK_COLOR[i][j]
            BACK_COLOR[i][j]=LEFT_COLOR[i][j]
            LEFT_COLOR[i][j]=temp[i][j]
    rotate_the_face_CW(UP_COLOR)
    rotate_the_face_ACW(DOWN_COLOR)
    return FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR

def change_face_left(FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR,UP_COLOR,DOWN_COLOR):
    temp=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range (3):
        for j in range (3):
            temp[i][j]=FRONT_COLOR[i][j]
            FRONT_COLOR[i][j]=LEFT_COLOR[i][j]
            LEFT_COLOR[i][j]=BACK_COLOR[i][j]
            BACK_COLOR[i][j]=RIGHT_COLOR[i][j]
            RIGHT_COLOR[i][j]=temp[i][j]
    rotate_the_face_ACW(UP_COLOR)
    rotate_the_face_CW(DOWN_COLOR)
    return FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR
