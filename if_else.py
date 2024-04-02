salary=int(input("Salray_Details:"))
age=int(input("What_is_the_Age:"))
loan = 0
if (salary >= 20000 or age <= 25):
    loan=int(input("how_loan_need:"))
    if (loan <=50000):
        print( "Maxium are elgible for the loan: 50000")
    else:
        print("you\'re not elgible amount for your age is 50000 but you\'re are aking %d.", loan)
else:
    print("Your not elgible for the loan")
    
