a=float(input("Enter your weight in kg: "))
b=float(input("Enter your height in m: "))
c=a/(b*b)
print("the person's BMI is: ",c)
if c<18.5:
    print("Underweight")
elif c>=18.5 and c<30:
    print("Normal weight")
else:
    print("Obese")
