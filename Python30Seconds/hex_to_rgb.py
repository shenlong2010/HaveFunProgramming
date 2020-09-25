def hexToRgb(hex):
	return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

print(hexToRgb('FFA501'))

print(int('FF', 16))
print(int('A5', 16))
print(int('01', 16))