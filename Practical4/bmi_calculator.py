# Purpose: To calculate the BMI of a person and determine if the person is underweight, normal weight or obese. 
a=float(input("Enter your weight in kg: "))
b=float(input("Enter your height in m: "))
c=a/(b*b)
#BMI=weight(kg)/height(m)^2
print("the person's BMI is: ",c)
#   Underweight: BMI < 18.5
#   Normal weight: 18.5 <= BMI < 30    
#   Obese: BMI >= 30
#   If the BMI is less than 18.5, the person is underweight.
if c<18.5:
    print("Underweight")
elif c>=18.5 and c<30:
    print("Normal weight")
else:
    print("Obese")
