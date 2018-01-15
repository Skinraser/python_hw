def sum_symbol_codes(first, last):
    total = 0
    for i in range(ord(first), ord(last)+1):
        total += i
    print(total)


sum_symbol_codes('x', 'x')
