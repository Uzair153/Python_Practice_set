def game():
    return 9999

score=game()
 
with open('35_HiScore.txt') as f :
    hiscore= int(f.read())
if (hiscore == ''):
    with open('35_HiScore.txt', 'w') as f :
        f.write(str(score))

elif hiscore<score:
    with open('35_HiScore.txt', 'w') as f :
        f.write(str(score))
     
