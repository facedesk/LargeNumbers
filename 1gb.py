import sys
import datetime
print(sys.maxsize)

s=1
for x in range(2147483647):
    s = s*2
    if(x% 1000000 == 0):
        f = open(str(x)+".txt","w")
        f.write(str(s))
        f.close()
        print(x,datetime.datetime.now())
f = open("answer.txt","w")
f.write(str(s))
f.close()  

    
