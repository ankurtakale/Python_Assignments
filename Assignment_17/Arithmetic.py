def Add(No1, No2):

    Sum = No1 + No2

    return Sum

def Sub(No1, No2):

    if No1 > No2:
        sub = No1 - No2
    else:
        sub = No2 - No1

    return sub

def Mul(No1, No2):

    mul = No1 * No2

    return mul

def Div(No1, No2):

    if No2 == 0:
        print("Division by 0 is not allowed\n")
        return

    div = No1 / No2

    return div