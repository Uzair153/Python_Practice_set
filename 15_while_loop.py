
fruit = ['Banana', 'Grapes', 'Mango', 'Kiwi']
a = int(input("Enter the number of characters: "))
i = 0
while a >= 0 and i < len(fruit):
    if len(fruit[i]) <= a:
        print(f"Yes, the {fruit[i]} has less then equal to {a} characters.")
    else:
        print(f"The {fruit[i]} has greater than equal to {a} characters")
    i += 1
