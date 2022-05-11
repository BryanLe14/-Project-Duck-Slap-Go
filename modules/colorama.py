ESC="\x1b"
toESC = lambda code:ESC+"["+str(code)+"m"
tstTxt = "Hello World!"
RESET = toESC(0)
class Clrama:
    BRIGHT = False
    RESET = toESC(0)
class Font:
    BOLD = toESC(1)
    DIM=FAINT = toESC(2)
    ITALIC = toESC(3)
    UNDERLINE = toESC(4)
    BLINK=BLINKING = toESC(5)
    INVERSE=INVERT = toESC(7)
    HIDE=HIDDEN=INVISIBLE = toESC(8)
    STRIKETHROUGH = toESC(9)
    DOUBLEUNDERLINE=UNDERLINE2 = toESC(21)
    BRIGHT = Clrama.BRIGHT = True
    
    UNBOLD = toESC(22)
    UNDIM=UNFAINT = toESC(22)
    UNITALIC = toESC(23)
    UNUNDERLINE = toESC(24)
    UNBLINK=UNBLINKING = toESC(25)
    UNINVERSE=UNINVERT = toESC(27)
    UNHIDE=UNHIDDEN=UNINVISIBLE = toESC(28)
    UNSTRIKETHROUGH = toESC(29)
    UNBRIGHT = Clrama.BRIGHT = not True
    RESET = toESC(0)

class Color:pass
class Fore(Color):
    if Clrama.BRIGHT:
        BLACK = toESC(90)
        RED = toESC(91)
        GREEN = toESC(92)
        YELLOW = toESC(93)
        BLUE = toESC(94)
        MAGENTA = toESC(95)
        CYAN = toESC(96)
        WHITE = toESC(97)
        DEFAULT = toESC(39)
        RESET = toESC(0)
    else:#elif not Clrama.BRIGHT:
        BLACK = toESC(30)
        RED = toESC(31)
        GREEN = toESC(32)
        YELLOW = toESC(33)
        BLUE = toESC(34)
        MAGENTA = toESC(35)
        CYAN = toESC(36)
        WHITE = toESC(37)
        DEFAULT = toESC(39)
        RESET = toESC(0)
    ID = lambda index: toESC("38;5;"+str(index))
    RGB = lambda r,g,b: toESC(f"38;2;{r};{g};{b}")
class Back(Color):
    if Clrama.BRIGHT:
        BLACK = toESC(100)
        RED = toESC(101)
        GREEN = toESC(102)
        YELLOW = toESC(103)
        BLUE = toESC(104)
        MAGENTA = toESC(105)
        CYAN = toESC(106)
        WHITE = toESC(107)
        DEFAULT = toESC(49)
        RESET = toESC(0)
    else:#elif not Clrama.BRIGHT:
        BLACK = toESC(40)
        RED = toESC(41)
        GREEN = toESC(42)
        YELLOW = toESC(43)
        BLUE = toESC(44)
        MAGENTA = toESC(45)
        CYAN = toESC(46)
        WHITE = toESC(47)
        DEFAULT = toESC(49)
        RESET = toESC(0)
    ID = lambda index: toESC("48;5;"+str(index))
    RGB = lambda r,g,b: toESC(f"48;2;{r};{g};{b}")