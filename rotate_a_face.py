def rotate_the_face_CW(FACE):
    temp1=FACE[0][0]
    FACE[0][0]=FACE[2][0]
    FACE[2][0]=FACE[2][2]
    FACE[2][2]=FACE[0][2]
    FACE[0][2]=temp1

    temp2=FACE[0][1]
    FACE[0][1]=FACE[1][0]
    FACE[1][0]=FACE[2][1]
    FACE[2][1]=FACE[1][2]
    FACE[1][2]=temp2

    return FACE

def rotate_the_face_ACW(FACE):
    temp=FACE[0][0]
    FACE[0][0]=FACE[0][2]
    FACE[0][2]=FACE[2][2]
    FACE[2][2]=FACE[2][0]
    FACE[2][0]=temp

    temp2=FACE[0][1]
    FACE[0][1]=FACE[1][2]
    FACE[1][2]=FACE[2][1]
    FACE[2][1]=FACE[1][0]
    FACE[1][0]=temp2

    return FACE
