import random

def gamewin(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='si':
            return False 
    elif comp=='p':
        if you=='s':
            return False
        elif you=='si':
            return True 
    elif comp=='si':
        if you=='s':
            return True
        elif you=='p':
            return False 
            
print("computer Turn : Stone(s) Paper(p) Sissoe(si)")
randNo=random.randint(1, 3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='si'
print("Computer Select there choice!!!")
you = input("your Turn : Stone(s) Paper(p) Sissoe(si) : ")
print(f"Computer Select :{comp}")
print(f"you Select :{you}")

a=gamewin(comp, you)
if a==None:
    print("Game is Tie")
elif a:
    print("You are the Winner!!!")
else:
    print("You are the Loser!!!")
