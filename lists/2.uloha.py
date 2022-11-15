def chopping(list):
    counter=0
    for i in range(0,len(list),2):
        counter+=list[i]*list[i+1]
    return counter

print(chopping([3, 2.5, 0.5, 10, 1.2, 1.2]))