print("press 0 for Enter manually :")
print("press 1 for using default values :")
a = int(input())

if a == 0:
    fruit = input("Enter the Name of Fruit :")
    print(f" The {fruit} has  {len(fruit)} characters.")
else:
    fruit = ['Banana', 'Grapes', 'Mango', 'Kiwi', 'Apple', 'Orange', 'Pineapple', 'Peach', 'Pear', 'Strawberry']
    i = 0
    while i < len(fruit):
        print(f" The {fruit[i]} has  {len(fruit[i])} characters.")
        i = i + 1
