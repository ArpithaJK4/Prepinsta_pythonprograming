def Reverse(a,start,end):
    while start<end :
        a[start],a[end] = a[end],a[start]
        start+=1
        end-=1

a=[1,2,3,4,3,4,5,6,7,8,45,6,787,56]
Reverse(a,0,len(a)-1)
print(a)
