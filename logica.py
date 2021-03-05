a, b = False, True
out = (a and b and a) or (b) or (b or a) or (a and not a and not b)

print(out)