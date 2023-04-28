
text = input("Enter the text : ")

if ("earn money" in text):
    spam = True
elif("buy online" in text): 
    spam = True
elif("get paid" in text): 
    spam = True
elif("make money online" in text): 
    spam = True
else:
    spam = False

if(spam):
    print("This is spam" )
else:
    print("This is not spam")
    
