from config import APP_NAME, VERSION
from src.calculator import HealthCalculator
from src.diet_engine import DietEngine

def main():
    print(f"========================================")
    print(f"   {APP_NAME} (v{VERSION})")
    print(f"========================================\n")

    try:
        weight = float(input("Enter Weight (kg): "))
        height = float(input("Enter Height (cm): "))

        # Perform basic calculations
        bmi = HealthCalculator.calculate_bmi(weight, height)
        category = HealthCalculator.get_bmi_category(bmi)
        tip = DietEngine.get_diet_tip(category)

        # Output results
        print("\n---------------- RESULTS ----------------")
        print(f"Your BMI: {bmi}")
        print(f"Category: {category}")
        print(f"Dietary Tip: {tip}")
        print("-----------------------------------------")

    except ValueError:
        print("\n[Error] Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    main()