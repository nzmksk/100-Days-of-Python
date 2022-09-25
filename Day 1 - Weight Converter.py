# Create a weight converter that converts kilogram to pound, and vice versa
def convert(weight, unit):
    if unit == 'l':
        # 1 pound = 1 kg / 2.205
        output = str(weight / 2.205) + " kg"
        return f'Your weight is {output}.'
    elif unit == 'k':
        # 1 kilogram = 1 lbs * 2.205
        output = str(weight * 2.205) + " lbs"
        return f'Your weight is {output}.'
    else:
        return "Syntax Error!"


try:
    weight = float(input("Input your weight in pounds or kilogram: "))
    # .lower() so both lower and upper cases can be accepted as input
    unit = input("Enter 'L' for pounds or 'K' for kilogram: ").lower()
    print(convert(weight, unit))
# Raise error if the weight entered is not a digit or decimal
except ValueError:
    print("You may only enter digits and decimals!")
