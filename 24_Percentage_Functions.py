# Write the function
def percentage(marks,totalmarks):
    per=(marks/totalmarks)*100
    return per

subjects=["Math", "Physics","Computer","History","English","Urdu"]
marks=[]
for i in range(6):
    a=int(input(f"Enter the Marks of {subjects[i]}:"))
    marks.append(a)


totalmarks=int(input("Totals MArks are :"))
sum = sum(marks)
# call the function
percentage1=percentage(sum, totalmarks)
print(f"The percentage of given marks are {percentage1}")
