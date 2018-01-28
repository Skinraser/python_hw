# Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в ней за
# исключением пробелов встречаются только один раз. Например, строки 'Питон', 'downstream', 'книга без слов'
# являются изограммами, а само слово 'изограмма' - нет.
lst = []


def is_isogram(string):
    for i in string:
        if i not in lst:
            lst.append(i)
        elif ' ' in string:
            continue
        elif i in lst:
            return False
    return True


print(is_isogram(input()))
