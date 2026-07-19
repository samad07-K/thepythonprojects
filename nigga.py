po=open(r"NN/nyfile.txt/poem.txt","r")
k=po.read().lower()
if "twinkle" in k:
    print('twinkle khanna is present')
else:
    print("its not present")
po.close()