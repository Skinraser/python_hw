import string


def encode(str_to_encode):  # returns enсoded string
    encoding_str = string.ascii_lowercase + string.digits
    encoded_string = ''
    print("Введить строку которую надо зашифровать:")
    user_string = input()
    for i in user_string.lower():
        for j in encoding_str:
            if i == j:
                j = encoding_str.index(i)
                sym = encoding_str[int(j):int(j) + 6:5]
                encoded_string += sym[1]
    print(encoded_string)
    return encoded_string


encode(str)
