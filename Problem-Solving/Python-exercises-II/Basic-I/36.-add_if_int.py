
# Add two objects if both objects are an integer type

def sumIfInt(x,y):
    if not (isinstance(x,int) and isinstance(y,int)):
        raise TypeError("Inputs must be integers")
    else:
        return x + y

print(sumIfInt(2,'h'))










