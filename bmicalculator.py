#BMI Calculator

height = float(input("what is your height in m") )
weight = float(input("what is your weight in kg:"))

#BMI = weight (kg) / (height (m))²

height_square = (height)**2
bmi = weight/height_square
print("your bmi is :",bmi)

