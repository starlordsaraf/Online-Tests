ef variantCounts(n,s0,k,b,m,a):
    ctr = 0
    sides = [0 for i in range(n)]
    sides[0] = s0
    if(s0*s0<=a):
        ctr+=1

    for i in range(1,n):
        sides[i] = ((k*sides[i-1]+b)%m+1+sides[i-1])
        if(sides[i]*sides[i]<=a):
            ctr+=1

    i = 0
    j = n-1

    while(i<j):
        if(sides[i]*sides[j]<=a):
            ctr+=2*(j-i)
            i+=1
        else:
            j-=1

    # for i in sides:
    #     if(i*i<=a):
    #         ctr+=1

    return(ctr)
    



print(variantCounts(3,2,3,3,2,15))