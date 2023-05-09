# Define the function
def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and print the result
area = calculate_area(length, width)
print("The area of the rectangle is:", area)
