def decrypt():
    a_string = "JgkJqPåGtFgvLwnKilgp"   # Insert your string here.
    alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]
    big_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Æ","Ø","Å"]
    answer = []

    for letter in a_string:
        a=0
        b=0
        for letter2 in alphabet:
            a+=1
            if (letter == letter2):
                answer.append(alphabet[a-3].lower())
        for letter3 in big_alphabet:
            b+=1
            if (letter == letter3):
                answer.append(big_alphabet[b-3].upper())

    print(answer)
    quit()

if __name__ == "__main__":
    decrypt()

#Better solution
# import string
# 
# for letter in "RUV{JgkJqPåGtFgvLwnKilgp}":
#     if letter in string.ascii_letters:
#         print(chr(ord(letter)-2), end="")
#     else:
#         print(letter, end="")

#Better better solution
# "".join([chr(ord(a)-2) if a in __import__("string").ascii_letters else a for a in "RUV{JgkJqPåGtFgvLwnKilgp}"])