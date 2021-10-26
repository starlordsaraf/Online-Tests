def sortBoxes(boxList):
    old = []
    new = []
    for box in boxList:
        if(box.split(" ")[1].isdigit()):
            new.append(box)
        else:
            old.append(box)
    
    old = sorted(old , key = lambda x: (x.split(" ",1)[1], x.split(" ",1)[0]))
    final = old + new
    return(final)



print("ANSWER",sortBoxes(["ykc 82 01","eo first qpx","09z cat hamster","06f 12 25 6","az0 first qpx", "236 cat dpg rabbit snake"]))



