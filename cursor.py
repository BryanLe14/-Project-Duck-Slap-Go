ESC = "\x1b"
toESC = lambda code:ESC+"["+str(code)
class Cursor:
    moveTo = lambda x, y: toESC(f"{x};{y}H")
    save = toESC("s")
    restore = toESC("u")
