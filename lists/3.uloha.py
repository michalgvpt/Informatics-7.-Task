def sum(list):
    counter=1
    for i in list:
        counter*=i
    return counter

c=[2, 3, 5, 7, 11]
print(sum(c))
print(sum(list(range(1,11))))
print(sum([2]*20))