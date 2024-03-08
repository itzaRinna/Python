#declare which number is the largest number
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("Num1 is the largest")
    elif num2 > num1 and num2 > num3:
        print("Num2 is the largest")
    elif num3 == num2 == num1:
        print("There are no largest number")
    else:
        print("Num3 is the largest")
    
    
max_num(300, 40, 5)
max_num(30, 40, 5)
max_num(30, 40, 50)
max_num(30, 30, 30)