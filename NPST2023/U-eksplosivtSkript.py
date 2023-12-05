# OTP list as provided in the original script
otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

###En fremgangsmåte

# with open("pinneved.txt", "r") as file:
#     pinneved = file.read()

# intervall = len(pinneved) // len(otp)

# eksplosjon = [0] * len(otp)

# for i, p in zip(reversed(otp), [pinneved[n:n+intervall] for n in range(0, len(pinneved), intervall)]):
#     eksplosjon[i] = p

# bang = ["".join([chr(ord(c) - 2) for c in fragment]) for fragment in eksplosjon]
# with open("slede.txt", "w") as file:
#     file.write("".join(bang))


def explode(input, antall):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter

with open("pinneved.txt", "r") as file:
    slede = file.read()

bang = explode(slede, 24)
eksplosjon = [str(bang[23-otp.index(i)]) for i in range(0, len(otp))]
pinneved = [''.join([chr(ord(c) - 2) for c in fragment]) for fragment in eksplosjon]

with open("slede.txt", "w") as file:
    file.write(''.join(pinneved))