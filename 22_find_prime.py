N= int(input("Enter the Number :"))
prime=True
for i in range(2 ,N):
    if(N%i == 0):
        prime=False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")