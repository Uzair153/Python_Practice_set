with open('37_text.txt') as f :
    content=f.read()
    content=content.replace('Donkey','@#$#@#$')

with open('37_text.txt', 'w') as f :
    f.write(content)