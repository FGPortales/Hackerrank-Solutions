S = input()
_string = ""
# print(len(S),"**")
if len(S)>0 and len(S)<=100:
    for v in S:
        if v == v.lower():
            _string = _string + v.upper()
        else:
            _string = _string + v.lower()

print(_string)

# Other Solution
# string_input = input()
# print(string_input.swapcase())