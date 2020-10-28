def func(height):
    actual = sorted(height)
    ctr = 0
    for i in range(len(height)):
        if(actual[i]!=height[i]):
            ctr+=1
    return(ctr)