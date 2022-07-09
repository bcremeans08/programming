height = float(input("What's your height?"))
weight = float(input("What's your weight"))
bmi = (weight * 703) / (height ** 2)
if bmi <= float(18.5):
    print('UNDERWEIGHT')
if bmi >= float(25):
    print('OVERWEIGHT')
if bmi >= float(18.5) and bmi <= float(25):
    print('NORMAL')