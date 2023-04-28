name = input("Enter the name of student : ")
a = int(input("Enter the marks of Math : "))
b = int(input("Enter the marks of English: "))
c = int(input("Enter the marks of Physics: "))
d = int(input("Enter the marks of Computer : "))

if (a<33 or b<33 or c<33 or d<33):
    message = "Dear {name}, We are sorry to announce that you are not promoted to the next class."
    message = message.replace("{name}", name)
    print(message)
elif (a+b+c+d)/4 < 40:
    message = "Dear {name}, We are sorry to announce that you are not promoted to the next class."
    message = message.replace("{name}", name)
    print(message)
else:
    message = "Dear {name}, Congratulations! You are promoted to the next class. Keep it up!"
    message = message.replace("{name}", name)
    print(message)
