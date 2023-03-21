# name Parker Asbury
def encode(into):
    split = [i for i in into]
    for j in range(len(split)):
        split[j] = str(int(split[j]) + 3)
    final = ''.join(split)
    return final

""" uhh i didnt attend lab so I didnt get a partner. But i did the lab and learned github uploading and put the whole
thing into a public github that I submitted so...
"""
def decode(into):
    split = [i for i in into]
    for j in range(len(split)):
        split[j] = str(int(split[j]) - 3)
    final = ''.join(split)
    return final
option = 0
while __name__ == '__main__':
    while option != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option:"))
        if option == 1:
            currentEnPass = encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!\n")

        if option == 2:
            print("The encoded password is " + str(currentEnPass) + ", and the original password is " + str(decode(currentEnPass)) + ".\n")

        if option == 3:
            break
    break