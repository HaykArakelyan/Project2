import random

uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

char_source = {
    0: uppers,
    1: lowers,
    2: chars,
    3: numbers
}

password = ""

length = int(input("What length should the password be(Min 16 characters): ") or "16")




for i in range(1, length + 1):
    source = char_source[random.randint(0, 3)]
    char = source[random.randint(0, len(source)) - 1]
    password += char

print(password)



