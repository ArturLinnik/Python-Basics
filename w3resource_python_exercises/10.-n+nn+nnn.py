
# Accepts an integer (n) and computes the value of n+nn+nnn

def n_operation(n):
    nn = str(n) + str(n)
    nnn = str(n) + str(n) + str(n) 
    new_n = n + int(nn) + int(nnn) 

    return new_n

print(n_operation(5))

# Other option is:

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)






