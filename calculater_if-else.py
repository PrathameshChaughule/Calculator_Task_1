#Title
print("*** Simple Calculater ***\n")

#Operation Choice
print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus\n")



while True:
    #Input 2 Numbers
    A= float(input("\nEnter first number: "))
    B= float(input("Enter second number: "))
    ch= input("Enter choice (1-5): ")
    
    if ch=='1':
          print("\nAddition: ",A,"+",B,"=", A+B)
    elif ch=='2':
          print("\nSubtraction: ",A,"-",B,"=", A-B)
    elif ch=='3':
          print("\nMultiplication: ",A,"*",B,"=", A*B)
    elif ch=='4':
          print("\nDivision: ",A,"/",B,"=", A/B)
    elif ch=='5':
          print("\nModulus: ",A,"%",B,"=", A%B)

      #Another Calculation
    new_cal=input("\nLet's do another calculation? (y/n): ")
    if new_cal=="n":
          break
    elif new_cal=="y":
          continue
    else:
          print("Invalid Input")
          break



    
