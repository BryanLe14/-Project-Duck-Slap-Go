from cursor import Cursor as c

print("qwerty\n"*10)
print("\x1b[H")
# print("\x1b[s")
print("uiop\n"*10)
# print("\x1b[u")
print("hjkl\n"*10)


print(c.moveTo(0, 1))
print("◘")