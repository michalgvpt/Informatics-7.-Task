list1=[2,7,10,16,58]
list2=[15,16,18,20]
length1=len(list1)
length2=len(list2)
def merge(list1:list,list2:list)->list:
    x=0
    y=0
    list=[]
    while x<length1 and y<length2:
      if list1[x]<list2[y]:
           list.append(list1[x])
           x+=1
      else:
           list.append(list2[y])
           y+=1
    list+=list1[x:]+list2[y:]
    return list

print(merge(list1,list2))