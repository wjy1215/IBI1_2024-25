# Purpose: To calculate the BMI of a person and determine if the person is underweight, normal weight or obese. 

a=float(input("Enter your weight in kg: ")) #ask the user to enter their weight in kg
b=float(input("Enter your height in m: ")) #ask the user to enter their height in meters
#calculate the BMI of the person
c=a/(b*b)
#BMI=weight(kg)/height(m)^2
print("the person's BMI is: ",c) #print the BMI of the person
if c<18.5: #if the BMI is less than 18.5
    print("Underweight") #print "Underweight"
elif c>=18.5 and c<30: #if the BMI is greater than or equal to 18.5 and less than 30
    print("Normal weight") #print "Normal weight"
else: #if the BMI is greater than or equal to 30
    print("Obese") #print "Obese"
