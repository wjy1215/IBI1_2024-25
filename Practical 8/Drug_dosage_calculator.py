def calculate_dosage(weight_kg, strength_paracetamol):
    recommended_dosage_mg = 15 * weight_kg
    dosage_ml = recommended_dosage_mg / strength_paracetamol*5
    return dosage_ml
weight_kg=int(input("Enter the weight of the child in kg([10,100]): "))
strength_paracetamol=int(input("Enter the strength of paracetamol in mg / 5 ml  (120 or 250): ")) 
# Check if the weight is within the valid range and strength is valid
if weight_kg < 10 or weight_kg > 100:
    print("Weight out of range. Please enter a weight between 10 and 100 kg.")
    exit()
# Check if the strength is valid
if strength_paracetamol not in [120, 250]:
    print("Invalid strength. Please enter either 120 mg/5 ml or 250 mg/5 ml.")
    exit()
# Calculate the dosage
needed_dasage=calculate_dosage(weight_kg, strength_paracetamol)
print(f"The recommended dosage of paracetamol is {needed_dasage} ml.")
# Example usage
weight_kg = 20
strength_paracetamol = 120
dosage_ml = calculate_dosage(weight_kg, strength_paracetamol)
print(f"EXAMPLE: The recommended dosage of paracetamol for a child weighing {weight_kg} kg with a strength of {strength_paracetamol} mg/5 ml is {dosage_ml} ml.")