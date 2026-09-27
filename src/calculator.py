class HealthCalculator:
    @staticmethod
    def calculate_bmi(weight_kg: float, height_cm: float) -> float:
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)

    @staticmethod
    def get_bmi_category(bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25.0 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"