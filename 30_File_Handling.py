f = open('31_poem.txt',"r")
data = f.read()
if 'sunset' in data:
    print("Yes, The Word sunset is present")
else:
    print("No, The Word sunset is not present")

f.close()