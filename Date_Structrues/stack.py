from pythonds3.basic import Stack

def par_checkr(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()

def base_convert(decimal, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while decimal > 0:
        rem = decimal % base
        rem_stack.push(rem)
        decimal = decimal // base
    new_string = ""
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]
    return new_string
print(base_convert(1000 , 16))

