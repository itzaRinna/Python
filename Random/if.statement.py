is_tall = False
is_male = False

if is_male and not is_tall:
    print("You're a short male")
elif is_male and is_tall:
    print("You're a tall male")
elif not is_male and not is_tall:
    print("You're a short girl")
else:
    print("You're either not tall or not male")