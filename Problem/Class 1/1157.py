x=input()
#print(x)
x=x.lower()
x=list(x)
x.sort()
#print(x)

y=len(x)


k=x[0]
j=0
z=[]
for i in range(0,y):
    
    j+=1
    if i==y-1: 
        z.append([x[i],j])
        break
        
    if not x[i+1]==x[i]:
        
        z.append([x[i],j])
        j=0
    
#print(z)

maxnumber=0
for i in z:
    if maxnumber<i[1]:
        maxnumber=i[1]
        winner=i[0].upper()
    elif i[1]==maxnumber:
        winner='?'
    
    
print(winner)

    



    

