def fact(n):
    if n<0:
        return "Not defined"
    a=1
    for i in range(1, n+1):
        a*=i
    return a

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def fib(n):
    p=0
    q=1
    for i in range(n-1):
        c=p + q
        p=q
        q=c
    return p
def sum(n):
    s=0
    for d in str(abs(n)):
        s=s+int(d)
    return s
def rev_num(n):
    r=str(abs(n))[::-1]
    if n < 0:
        return-int(r)
    return int(r)
def armstrong(n):
    temp=abs(n)
    power=len(str(temp))
    s=0
    for d in str(temp):
        s=s+int(d) ** power
    return s==n
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
def lcm(a,b):
    return abs(a*b) // gcd(a,b)
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n
while True:
    print("1 Factorial")
    print("2 Prime")
    print("3 Fibonacci")
    print("4 Sum digits")
    print("5 Reverse number")
    print("6 Armstrong")
    print("7 GCD")
    print("8 LCM")
    print("9 Perfect number")
    choice=input("Enter choice:")
    n1=int(input("Enter number:"))
    if choice=="1":
        print("Result:",fact(n1))
    elif choice=="2":
        if prime(n1):
            print("Prime number")
        else:
            print("Not prime")
    elif choice=="3":
        print("Fibonacci:", fib(n1))
    elif choice=="4":
        print("Sum:", sum(n1))
    elif choice=="5":
        print("Reverse:", rev_num(n1))
    elif choice=="6":
        print("Armstrong:", armstrong(n1))
    elif choice=="7":
        n2=int(input("Second number: "))
        print("GCD:", gcd(n1, n2))
    elif choice=="8":
        n2=int(input("Second number: "))
        print("LCM:", lcm(n1, n2))
    elif choice=="9":
        print("Perfect number:", perfect(n1))
    else:
        print("Invalid choice")