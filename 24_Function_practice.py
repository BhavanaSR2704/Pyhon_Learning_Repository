def greeting():  #WITHOUT PARAMETERS
    print("HELLO, IT'S ME BHAVANA:- WELCOME TO TO MY HOME") # function defined

greeting() # function calling                        #-----------------------O/P HELLO, IT'S ME BHAVANA:- WELCOME TO TO MY HOME

#--------------------------------------------------------------------------------

def marriage(boy,girl):# WITH PARAMETERS
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")                     #----------------------O/P Boy is RAM 
    print(f" {boy} married {girl} ")                                       #Girl is SITHA
                                                                           #RAM married SITHA 
marriage("RAM","SITHA") # POSITIONAL ARRGUMENT                       
#marriage(boy="RAM",girl="SITHA") #KEY WORD ARRGUMENT 

#---------------------------------------------------------------------------------

def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

tables(3)                  #------------------O/P (3-tables)

#--------------------------------------------------------------------------------

#return function 
def func(num):
    return int(num*2)
a=2
b=a+func(2)          #b=2+4
print(b)             #---------------------------O/P 6
