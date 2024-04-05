i = int(input("The number to find Factorial:"))
n=i
fact = 1
while i > 0:
    fact = fact * i
    i = i - 1
    
print("Factorial of", n, "is", fact)