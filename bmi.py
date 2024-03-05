def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 20:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Prompt the user for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = calculate_bmi(weight, height)

# Classify the BMI
category = classify_bmi(bmi)

# Display the result to the user
print(f"Your BMI is {bmi:.2f}")
print(f"You are classified as {category}")
