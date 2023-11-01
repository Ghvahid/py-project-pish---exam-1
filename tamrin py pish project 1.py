new_str = ""
input_str = list(input("Enter your string : ").lower())
num = int(input("Enter Number : "))

for i in range(len(input_str)):
    x = ord(input_str[i])
    x += num
    if ord("a") <= x <= ord("z"):
        new_str += chr(x)
    elif x > ord("z"):
        while x > ord("z"):
            x -= 26
        new_str += chr(x)
    else:
        while x < ord("a"):
            x += 26
        new_str += chr(x)


print(new_str)
