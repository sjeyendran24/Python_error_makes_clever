a = []
sum = 0
n = int(input())
for i in range(n):
    num=int(input("Enter the num:"+str(i+1)+"="))
    a.append(num)
    sum +=num
print("Sum is", sum)
print("list of a is:", a)