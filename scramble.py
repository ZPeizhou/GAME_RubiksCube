from move_a_face import move_the_up_face_CW
from move_a_face import move_the_up_face_ACW
from move_a_face import move_the_down_face_CW
from move_a_face import move_the_down_face_ACW
from move_a_face import move_the_left_face_CW
from move_a_face import move_the_left_face_ACW
from move_a_face import move_the_right_face_CW
from move_a_face import move_the_right_face_ACW

import random

def scramble(UP_COLOR,DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR):
    scramble_formula=[]
    for i in range (50):
        scramble_formula.append(random.randint(0,7))
        if scramble_formula[i]==0:
            move_the_up_face_CW(UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR)
        elif scramble_formula[i]==1:
            move_the_up_face_ACW(UP_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR)
        elif scramble_formula[i]==2:
            move_the_down_face_CW(DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR)
        elif scramble_formula[i]==3:
            move_the_down_face_ACW(DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR)
        elif scramble_formula[i]==4:
            move_the_left_face_CW(FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR)
        elif scramble_formula[i]==5:
            move_the_left_face_ACW(FRONT_COLOR,UP_COLOR,DOWN_COLOR,RIGHT_COLOR,LEFT_COLOR)
        elif scramble_formula[i]==6:
            move_the_right_face_CW(RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR)
        else :
            move_the_right_face_ACW(RIGHT_COLOR,FRONT_COLOR,BACK_COLOR,UP_COLOR,DOWN_COLOR)
    return UP_COLOR,DOWN_COLOR,FRONT_COLOR,BACK_COLOR,LEFT_COLOR,RIGHT_COLOR
