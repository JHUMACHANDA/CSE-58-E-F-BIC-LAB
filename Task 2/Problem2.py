
text = input()  
k = int(input())
c = {}

for i in range (len(text)- k + 1 ):
    patt = text[i:i+k]
    
    if patt in c:
        c[patt]+=1
    else:
        c[patt]=1
        
        max_c=0
        for value in c.values():
            if value > max_c:
                max_c=value
       
        
for key in c:
    if c[key] == max_c:
        print(key, end=" ")
       
