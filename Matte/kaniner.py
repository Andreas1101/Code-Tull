

def diff():
    count = 0
    n = 1
    #r = 1.8
    x = float(input("Your value for x0: "))
    r = float(input("Your value for r: "))

    while count < 10:
        x = r*x*(1-x)
        print("x{} = {}".format(n, x))
        
        n = n + 1
        count = count + 1

if __name__ == "__main__":
    diff()