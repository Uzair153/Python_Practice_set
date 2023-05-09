storename = input("Enter the Name of store :")
storecode = int(input("Enter the code of store :"))
item= int(input("How Many items you want to store :"))
products=[]

for i in range(item):
    print(f"Enter the Name of Product {i+1} :")
    pname=input("NAME :")    
    print(f"Enter the code of {pname} :")
    pcode=str(input("CODE :"))
    products.append((pname, pcode))
   

print("*********************************WELCOME**********************************************************")

print(f"Store Name ={storename}")
print(f"Store Code ={storecode}")
print("The Items you added recently are :")
for pname, pcode in products:
    print(pname , pcode)

