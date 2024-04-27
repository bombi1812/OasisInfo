import math

def classify(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi >= 16 and bmi < 17:
        return "Moderate Thinness"
    elif bmi >= 17 and bmi < 18.5:
        return "Mild Thinness"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    elif bmi >= 30 and bmi < 35:
        return "Obese Class I"
    elif bmi >= 35 and bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

def getWeight():
    wt=float(input("Please enter your weight in kg:"))
    return wt

def getHeight():
    s=input("Enter your height in feet and inches(eg: 5'8\"):")
    a= s.split("'")
    feet=float(a[0])
    inches=float(a[1].strip('"'))
    ht=(feet*12)+inches
    return ht

def calcBMI(wt,ht):
    #convert height (inches)to meters
    meters= ht*0.0254

    print("Your Height in Meters is:",meters)

    bmi= wt/(meters*meters)
    
    return bmi

if __name__=="__main__":
    print("WELCOME TO THE BMI CALCULATOR :")

    wt=getWeight()
    ht=getHeight()

    bmi=calcBMI(wt,ht)
    print(f"Your final BMI is :{round(bmi,2)}")
    
    classification = classify(bmi)
    print(f"Based on your BMI, you are classified as: {classification}")
