word="learning"
with open("practice.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Find")           


#OUTPUT
#Found

#------------------------------------------------

word="Bhavana"
with open("practice.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Find")


#OUTPUT
#Not Found
