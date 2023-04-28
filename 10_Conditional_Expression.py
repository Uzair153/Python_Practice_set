a = int(input("Enter the 1st no : "))
b = int(input("Enter the 2nd no : "))
c = int(input("Enter the 3rd no : "))
d = int(input("Enter the 4th no : "))

if a > b:
    large1 = a
else:
    large1 = b

if c > d:
    large2 = c
else:
    large2 = d

if large1 > large2:
    print("The biggest number is", large1 )
else:
    print("The biggest number is", large2 )





