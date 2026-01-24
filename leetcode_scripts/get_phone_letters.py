



def get_letters(d):

    d = ord(d) - ord('0')
    offset =  3 * (d-2)
    
    if d in (8,9) : offset+=1

    count = 4 if d in (7,9) else 3

    start = ord('a')+offset

    for i in range(count):
        yield chr(start+i)

for i in get_letters('7'):
    print(i,end='')
print('') 

#print(get_letters('6'))
#print(get_letters('7'))
#print(get_letters('8'))
#print(get_letters('9'))



    
