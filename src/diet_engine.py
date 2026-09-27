class DietEngine:
    @staticmethod
    def get_diet_tip(bmi_category: str) -> str:
        if bmi_category == "Underweight":
            return "Include healthy fats, dairy, and protein-rich food in daily meals."
        elif bmi_category == "Normal Weight":
            return "Maintain a balanced diet with proper hydration and regular physical activity."
        elif bmi_category == "Overweight":
            return "Focus on portion control, fresh fruits, vegetables, and daily light workouts."
        else:
            return "Limit processed sugars, eat fiber-rich meals, and consult a nutritionist."