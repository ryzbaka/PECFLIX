'''
use this program to generate code for various genre combinations:

crime drama
comedy-drama
legal drama
spy drama
western
reality
sci-fi
action
mystery
fantasy
supernatural
horror
thriller
zombie fiction
detective drama
musical
comedy
satire
political satire

'''
#begining of code
import sys
def check_g(x,listo,listy):
    if x in listo:
        return 1
    elif x not in listy:
        return 2
    else:
        return 0
def mapper(n):
    megalist=["crime drama","comedy-drama","legal drama","spy drama","western"
    ,"reality"
    ,"sci-fi"
    ,"action"
    ,"mystery"
    ,"fantasy"
    ,"supernatural"
    ,"horror"
    ,"thriller"
    ,"zombie fiction"
    ,"detective drama"
    ,"musical"
    ,"comedy"
    ,"satire"
    ,"political satire"]
    glist=[]
    for i in range(n):
        print("enter genre {}".format(i+1))
        genre=input(">")
        flag=check_g(genre,glist,megalist)
        if flag==0:
            glist.append(genre)
        else:
            print("\n\nDuplicate value or invalid genre...try again")
            break
    if flag!=0:
        mapper(n)
    if flag==0:
        print(glist)
        for j in range(len(megalist)):
            if megalist[j] in glist:
                print("1",end="")
            else:
                print("0",end="")
        print("")
        print("Is the code to be input in genre column")


def val_input():
    print("Number of genres in movie(maximum 3)")
    try:
     n=int(input(">"))
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("try again...")
        val_input()
    if n>3:
     print("it has to be less than or equal to 3")
     val_input()
    else:
     mapper(n)   

