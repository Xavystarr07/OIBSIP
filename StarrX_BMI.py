
def calculate_bmi(weight, height):
    """
    Calculates BMI and classify it into categories.
    Formula: BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def get_user_input():
    """
    Get user input for weight and height.
    """
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Please enter valid numerical values.")
        return get_user_input()

def main():
    print("BMI Calculator")
    print("-------------------")

    weight, height = get_user_input()
    bmi, category = calculate_bmi(weight, height)

    print(f"\nBMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
