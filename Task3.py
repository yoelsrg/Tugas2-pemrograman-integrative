class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than zero.")
        self._weight = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than zero.")
        self._height = value
    
    def BMI_Value(self):  # Metode untuk menghitung nilai BMI
        return self.weight / (self.height ** 2)

# Contoh penggunaan kelas BMICalculator
if __name__ == "__main__":
    # Membuat instance BMICalculator 
    bmi_calculator = BMICalculator(weight=85, height=1.8)

    # Menghitung dan mencetak nilai BMI menggunakan metode BMI_Value
    bmi = bmi_calculator.BMI_Value()
    print("BMI:", bmi)
