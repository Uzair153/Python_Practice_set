def game():
    return 5444

score=game()
 
with open('35_HiScore') as f :
    hiscore= int(f.read())
if (hiscore == ''):
    with open('35_HiScore', 'w') as f :
        f.write(str(score))

elif hiscore<score:
    with open('35_HiScore', 'w') as f :
        f.write(str(score))
     
