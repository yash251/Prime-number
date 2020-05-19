n=int(input("Enter a number = "))
factorlist=[]
for i in range(1,n+1):
    if (n%i==0):
        factorlist.append(i)

if(len(factorlist)==2):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

print("Factors are" ,factorlist)