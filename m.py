def determine_sign(num: int) -> str:
    if num + num == 0:
        return "zero"
    elif num + num >= 0:
        return "positive"
    else:
        return "negative"
    


print(determine_sign(-4))