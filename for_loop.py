# Get the input number A and B , then print the number inbetween the two numbers
a = int(input("A :"))
b = int(input("B :"))
c = 0
j = 0
sum = 0
for i in range(a, b+1):
    sum += i
    if i % 3 == 0 and i % 5:
        j+=1

print("Count Number is devied by number 3 & 5:",j)
print("Sum of Number:",sum)