# Get the input number A and B , then print the number inbetween the two numbers
a = int(input("A :"))
b = int(input("B :"))
c = 0
j = 0
for i in range(a+1, b+1):
    if i % 2 == 0:
        j +=1
    else:
        print(i)
        c +=1
print("Count Even Number:",j)
print("Count of Odd Number:",c)