nums= int(input("How many numbers? "))
sum=0
for i in range(nums):
    n= int(input("Enter number: "))
    sum= sum+n
    if i==0:
        max=n
        min=n
    else:
        if n>max:
            max=n
        if n<min:
            min=n
avg= sum/nums
print("Sum =", sum)
print("Average =", avg)
print("Maximum =", max)
print("Minimum =", min)