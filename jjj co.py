with open("poem.txt") as f:
    vow=0
    consonant=0
    ch=f.read(1)
    while ch:
        if ch in ["a","A","E","e","i","I","O","o","U","u"]:
            vow=vow+1
        elif consonant==consonant+1:
            ch=f.read(1)
    print("vowels are like",vow)
    print("consonants are like",consonant)
    
