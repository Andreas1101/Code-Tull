def diff():
    count = 0
    n = 1
    x = float(input("Your value for x0: "))
    r = float(input("Your value for r: "))

    while count < 10:
        x = r*x*(1-x)
        print("x{} = {}".format(n, x))
        
        n = n + 1
        count = count + 1

def diff2():
    x = 0.7     # x_0 starting value

    for r in range(2, 10, 1):
        count = 0
        n = 1
        print("r = {}".format(r))
        while count < 10:
            x = r*x*(1-x)
            print("x{} = {}".format(n, x))
            
            n = n + 1
            count = count + 1

def diff_robin():
    
    r = 1.0

    for i in range(2, 11):
        r = r + 1.0
        count = 0
        n = 1

        x = 0.77    # x_0 starting value

        print("r = {}\t\tx_0 = {}".format(r, x))
        print("___________________________________")
        while count < 10:
            x = r*x*(1-x)
            print("x{}\t=\t{}".format(n, x))
            
            n = n + 1
            count = count + 1
        print("")


if __name__ == "__main__":
    diff_robin()
