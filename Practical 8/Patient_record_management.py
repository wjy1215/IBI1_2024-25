class patients:
    def __init__(self, name, age, latest_admission, medical_history):
        self.name = name
        self.age = age
        self.latest_admission = latest_admission
        self.medical_history = medical_history
    def display(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, Latest Admission: {self.latest_admission}, Medical History: {self.medical_history}")
# Example usage
patient1 = patients("Lrving", 33, "2025-3-27", "ACL surgery")
patient1.display()
'''
patient2 = patients("John Doe", 45, "2025-3-28", "Diabetes")
patient2.display()
'''
# input if needed
'''
patient_name = input("Enter patient's name: ")
patient_age = int(input("Enter patient's age: "))
patient_latest_admission = input("Enter patient's latest admission date (YYYY-MM-DD): ")
patient_medical_history = input("Enter patient's medical history: ")
'''
