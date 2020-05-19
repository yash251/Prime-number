
n=int(input("Enter a number = "))
factorlist=[]
primefactors=[]

for i in range(1,n+1):
    if (n%i==0):
        factorlist.append(i)

if(len(factorlist)==2):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
print("Factors are" ,factorlist)

for k in factorlist:
    allfactor=[]
    for j in range(1,k+1):
        if (k%j==0):
            allfactor.append(j)
    if(len(allfactor)==2):
        primefactors.append(k)
print("Prime Factors are " ,primefactors)