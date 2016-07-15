def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

mylist = []
# ti ginetai ama dn ine akrivos 4ada?
# metatrepw to int se binary kai me vasi to mikos vriskw posa bytes thelei
# ftiaxnw ta tags
# xwrizw ton arithmo se oxtades me vasi to groupvarint
for i in range(2,100):
    mylist.append(fib(i))

print mylist
print

for i in range((len(mylist) + 1)/4):
    output = " "
    print "Round" + str(i)
    for j in range(4): 
        x = bin(mylist[4*i+j])[2:]
        tag = '{0:02b}'.format((len(x)-1)/8)
        output += tag 
       # print output
        #print
    output+="_"     
    for j in range(4):
        print "Encoding" + str(mylist[4*i+j])
        x='{0:032b}'.format(mylist[4*i+j])
        y = bin(mylist[4*i+j])[2:]
        # print
        #print "Y:" + y
        print "LEN:" + str(len(y))
        if len(y) <=8 :
            output+= x[24:32]
            output+="_"
        elif len(y)<= 16 :
            output+= x[24:32]
            output+="_"
            for k in range(8):
                output+=x[16+k]
            output+="_"    
        elif len(y)<= 24 :
            output+= x[24:32]
            output+="_"
            output+= x[16:24]
            output+="_"
            for k in range(8):
                output+=x[8+k]
            output+="_"    
        elif len(y) <= 32:    
            output+= x[24:32]
            output+="_"
            output+= x[16:24]
            output+="_"
            output+= x[8:16]
            output+="_"
            for k in range(8):
                output+=x[k]
            output+="_"    
        #output+= x[24:32]
        #output+="_"    
       # print output
        #print
    print output
    print 
  
    


