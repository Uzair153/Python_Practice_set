# Define Function
def factorial(n):
    product=1
    for i in range(n):
        product=product * (i+1)
    return product

a=int(input("Enter Number :"))
f=factorial(a)
print(f)