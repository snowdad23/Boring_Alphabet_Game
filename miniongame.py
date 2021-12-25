def minion_game(string):
    def duplicateremover(listname):
        cleanlist=[]
        for i in listname:
            if i not in cleanlist:
                cleanlist.append(i)
        return cleanlist
    substrings=[]
    vowels=['A','I','E','O','U']
    consonants=[]
    csubstrings=[]
    vsubstrings=[]
    
    for i in range (ord('A'),ord('Z')+1):
        if chr(i) not in vowels:
            consonants.append(chr(i))

    for j in range(len(string)):
        for i in range (len(string)-j):
            substrings.append(string[i:i+j+1])
    substringsx=duplicateremover(substrings)
    for i in substringsx:
        if i[0] in vowels:
            vsubstrings.append(i)

        elif i[0] in consonants:
            csubstrings.append(i)

    vscore=0
    cscore=0
    for i in vsubstrings:
        vscore=vscore+substrings.count(i)
    for i in csubstrings:
        cscore=cscore+substrings.count(i)
    
    if cscore>vscore:
        print('Stuart',cscore)
    elif vscore>cscore:
        print('Kevin',vscore)
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)