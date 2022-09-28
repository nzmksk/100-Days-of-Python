def bmi(w, h):
    bmi_score = w / (h ** 2)
    if bmi_score <= 18.5:
        return "Underweight"
    elif bmi_score <= 25.0:
        return "Normal"
    elif bmi_score <= 30.0:
        return "Overweight"
    else:
        return "Obese"


try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    print(bmi(weight, height))
except (ValueError, ZeroDivisionError):
    print("Please enter valid inputs.")