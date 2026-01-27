import random
import re

def GetDivisors(x):
    """Gets the divisors of a number and returns them in a list."""
    list0 = []
    for i in range(int(x)):
        i += 1
        if x % i == 0:
            list0.append(i)
    return list0

def Get2Exp(x):
    """Gets the 2^x value. Uselessness at its peak."""
    return 2**x

def GetxthRoot(x, y):
    """Gets the xth root of y."""
    return y**(1/x)

def Magnitude(x, y=None, z=None):
    """Gets the magnitude of a vector x, y, z (z is optional.)"""
    if y != None and z != None:
        return ((x**2)+(y**2)+(z**2)) ** (1/2)
    elif y != None:
        return ((x**2)+(y**2)) ** (1/2)
    else:
        if len(x) == 3:
            s, t, u = x
            return ((s**2)+(t**2)+(u**2)) ** (1/2)
        elif len(x) == 2:
            s, t = x
            return ((s**2)+(t**2)) ** (1/2)
        else:
            raise ValueError("Amount of items in list is either too big (>3) or too low. (<2)")

def pythsTheorem(a, b):
    """Gets the two cathetuses a and b, and it calculates the hypotenuse."""
    c = (a**2 + b**2) ** (1/2)
    return c

def isPrime(x):
    """Determines if x is prime or not."""
    list0 = []
    for i in range(int(x)):
        i += 1
        if x % i == 0:
            list0.append(i)
    if len(list0) < 3:
        return True
    elif x == 0:
        return False
    else:
        return False

def GetElementFromPeriodicTable(x):
    """Gets the element with the x index in the periodic table, if it doesn't exist, it'll return Undefined."""
    elements = {
        1: "H",
        2: "He",
        3: "Li",
        4: "Be",
        5: "B",
        6: "C",
        7: "N",
        8: "O",
        9: "F",
        10: "Ne",
        11: "Na",
        12: "Mg",
        13: "Al",
        14: "Si",
        15: "P",
        16: "S",
        17: "Cl",
        18: "Ar",
        19: "K",
        20: "Ca",
        21: "Sc",
        22: "Ti",
        23: "V",
        24: "Cr",
        25: "Mn",
        26: "Fe",
        27: "Co",
        28: "Ni",
        29: "Cu",
        30: "Zn",
        31: "Ga",
        32: "Ge",
        33: "As",
        34: "Se",
        35: "Br",
        36: "Kr",
        37: "Rb",
        38: "Sr",
        39: "Y",
        40: "Zr",
        41: "Nb",
        42: "Mo",
        43: "Tc",
        44: "Ru",
        45: "Rh",
        46: "Pd",
        47: "Ag",
        48: "Cd",
        49: "In",
        50: "Sn",
        51: "Sb",
        52: "Te",
        53: "I",
        54: "Xe",
        55: "Cs",
        56: "Ba",
        57: "La",
        58: "Ce",
        59: "Pr",
        60: "Nd",
        61: "Pm",
        62: "Sm",
        63: "Eu",
        64: "Gd",
        65: "Tb",
        66: "Dy",
        67: "Ho",
        68: "Er",
        69: "Tm",
        70: "Yb",
        71: "Lu",
        72: "Hf",
        73: "Ta",
        74: "W",
        75: "Re",
        76: "Os",
        77: "Ir",
        78: "Pt",
        79: "Au",
        80: "Hg",
        81: "Tl",
        82: "Pb",
        83: "Bi",
        84: "Po",
        85: "At",
        86: "Rn",
        87: "Fr",
        88: "Ra",
        89: "Ac",
        90: "Th",
        91: "Pa",
        92: "U",
        93: "Np",
        94: "Pu",
        95: "Am",
        96: "Cm",
        97: "Bk",
        98: "Cf",
        99: "Es",
        100: "Fm",
        101: "Md",
        102: "No",
        103: "Lr",
        104: "Rf",
        105: "Db",
        106: "Sg",
        107: "Bh",
        108: "Hs",
        109: "Mt",
        110: "Ds",
        111: "Rg",
        112: "Cn",
        113: "Nh",
        114: "Fl",
        115: "Mc",
        116: "Lv",
        117: "Ts",
        118: "Og"
    }
    return elements.get(x, "Undefined")

def Percent(x, y):
    """Gets the x% of y."""
    return (y/100) * x

def rad2deg(x: float):
    """Converts radians to degrees."""
    return x * (180/3.14)

def deg2rad(x: float):
    """Converts degrees to radians."""
    return x * (3.14/180)

def hexArea(x):
    """Calculates the area of a hexagon with side x."""
    return ((3*(3**0.5))*(x**2)) / 2

def hexcolorRandom(hasAlpha: bool):
    """Generates a pseudo-random hex color code."""
    hexcodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    if hasAlpha == False:
        for i in range(6):
            result += random.choice(hexcodes)
        return "#" + result
    elif hasAlpha == True:
        for i in range(8):
            result += random.choice(hexcodes)
        return "#" + result
    else:
        raise TypeError("Used int/float/str instead of bool.")

def xor(x, y):
    """Logic gate XOR."""
    if x and y:
        return False
    elif x or y:
        return True
    else:
        return False

def xnor(x, y):
    """Logic gate XNOR."""
    if x and y:
        return True
    elif not x and not y:
        return True
    else:
        return False

def complexAdd(x, y):
    """Adds x (in the form of x+yi) by y (in the form of x+yi)"""
    pattern = rf"-?\d+(?:\.\d+)?i"
    pattern2 = rf"-?\d+(?:\.\d+)?\b"
    pattern3 = rf"-?\d+(?:\.\d+)?"
    impartx = re.findall(pattern=pattern, string=x)
    impartx = impartx[0]
    repartx = re.findall(pattern=pattern2, string=x)
    reparty = re.findall(pattern=pattern2, string=y)
    reparty = reparty[0]
    repartx = repartx[0]
    imparty = re.findall(pattern=pattern, string=y)
    imparty = imparty[0]
    reRes = float(repartx) + float(reparty)
    imRes = float(re.findall(pattern=pattern3, string=impartx)[0]) + float(re.findall(pattern=pattern3, string=imparty)[0])
    if imRes < 0:
        return str(reRes) + str(imRes) + 'i'
    elif imRes > 0:
        return str(reRes) + '+' + str(imRes) + 'i'

def complexSub(x, y):
    """Subtracts x (in the form of x+yi) by y (in the form of x+yi)"""
    pattern = rf"\d+(?:\.\d+)?i"
    pattern2 = rf"\d+(?:\.\d+)?\b"
    pattern3 = rf"\d+(?:\.\d+)?"
    impartx = re.findall(pattern=pattern, string=x)
    impartx = impartx[0]
    repartx = re.findall(pattern=pattern2, string=x)
    reparty = re.findall(pattern=pattern2, string=y)
    reparty = reparty[0]
    repartx = repartx[0]
    imparty = re.findall(pattern=pattern, string=y)
    imparty = imparty[0]
    reRes = float(repartx) + float(reparty)
    imRes = float(re.findall(pattern=pattern3, string=impartx)[0]) - float(re.findall(pattern=pattern3, string=imparty)[0])
    if imRes < 0:
        return str(reRes) + str(imRes) + 'i'
    elif imRes > 0:
        return str(reRes) + '+' + str(imRes) + 'i'
    elif imRes == 0:
        return str(reRes) + '+' + str(imRes) + 'i'

def imaginaryMult(x, y):
    """Multiplies x (in the form of xi) by y (in the form of yi)"""
    pattern = rf"\d+(?:\.\d+)?i"
    pattern2 = rf"\d+(?:\.\d+)?"
    imCx =re.findall(pattern=pattern, string=x)[0]
    imCx = float(re.findall(pattern=pattern2, string=imCx)[0])
    imCy = re.findall(pattern=pattern, string=y)[0]
    imCy = float(re.findall(pattern=pattern2, string=imCy)[0])
    res = imCx * imCy * -1
    return res

def complexMult(x, y):
    """Multiplies x (in the form of x+yi) by y (in the form of x+yi)"""
    pattern = rf"\d+i"
    pattern2 = rf"\d+"
    b = re.findall(pattern=pattern, string=x)
    b = b[0].strip('i')
    a = re.findall(pattern=pattern2, string=x)
    c = re.findall(pattern=pattern2, string=y)
    c = c[0]
    a = a[0]
    d = re.findall(pattern=pattern, string=y)
    d = d[0].strip('i')
    a, c = float(a), float(c)
    b1, d1 = float(re.findall(pattern=pattern2, string=b)[0]), float(re.findall(pattern=pattern2, string=d)[0])
    term1 = (a*c)-(float(b) * float(d))
    term2 = str((float(a) * float(d)) + (float(c) * float(b))) + 'i'
    res = complexAdd(str(term1)+'+0i', '0+' + str(term2))
    return res

def imaginaryDiv(x, y):
    """Divides x (in the form of xi) by y (in the form of xi)"""
    pattern = rf"\d+(?:\.\d+)?i?"
    pattern2 = rf"\d+(?:\.\d+)?"
    imCx =re.findall(pattern=pattern, string=x)[0]
    imCy = re.findall(pattern=pattern, string=y)[0]
    imCx2 =re.findall(pattern=pattern2, string=x)[0]
    imCy2 = re.findall(pattern=pattern2, string=y)[0]
    imCx2 = float(imCx2)
    imCy2 = float(imCy2)
    xim = False
    yim = False
    res = 'Error'
    if 'i' in imCx:
        xim = True
    if 'i' in imCy:
        yim = True
    if xim == True and yim == False:
        res = str(imCx2 / imCy2) + 'i'
    elif xim == False and yim == True:
        step1 = str(imCx2 / imCy2)
        imCy2 *= -1
        imCx = imCx + 'i'
        res = str(imCx2 / imCy2) + 'i'
    elif xim == True and yim == True:
        res = str(imCx2 / imCy2)
    elif xim == False and yim == False:
        res = str(imCx2 / imCy2)
    return res

def matrixsum(x, y):
    """Performs matrix addition."""
    for i in range(len(x)):
        x[i] += y[i]
    return x

def matrixsub(x, y):
    """Performs matrix subtraction."""
    for i in range(len(x)):
        x[i] -= y[i]
    z = x
    return z

def mean(x:list):
    """Gets the arithmetic mean of a list"""
    return sum(x) / len(x)

def median(x:list):
    """Gets the median of a list"""
    if len(x) % 2 != 0:
        return x[int((len(x)+1)/2)-1]
    else:
        return (x[int(len(x)/2)-1] + x[int(len(x)/2)]) / 2

def geoMean(x:list):
    """Gets the geometric mean of a list."""
    s = x[0]
    x.remove(x[0])
    for n in x:
        s = s*n
    return (s**(1/(len(x)+1)))

def mode(x:list):
    """Gets the mode of a list."""
    occs = {}
    for e in x:
        occs.update({e: x.count(e)})
    return max(occs, key=occs.get)

def isPerfectSquare(n):
    """Checks if the number is a perfect square."""
    if n**(1/2) % 1 == 0:
        return True
    else:
        return False

def fib(reps: int):
    """Generates a list with the fibonacci sequence, the length of it is denoted with (reps)."""
    n0 = 1
    n = 1
    sequence = []
    for i in range(reps):
        sequence.append(n)
        n0 = n-n0
        n += n0
    return sequence

def modulo(n):
    """Gets the modulo of x, |x|."""
    if n < 0:
        return -n
    else:
        return n

def isSorted(x: list, orient: None):
    """Checks if a list is sorted. When the 2nd argument is True or None, it'll check for 1, 2, 3, if False, 3, 2, 1."""
    if orient == True or orient == None:
        sorted = True
        highestn = -99999999999999999999
        for n in x:
            if n >= highestn:
                highestn = n
            elif n < highestn:
                sorted = False
                return sorted
        if sorted != False:
            return sorted
    else:
        sorted = True
        highestn = 99999999999999999999
        for n in x:
            if n <= highestn:
                highestn = n
            elif n > highestn:
                sorted = False
                return sorted
        if sorted != False:
            return sorted
        

def flipList(x: list):
    """Flips the order of the numbers in the list"""
    for i in range(len(x)-1):
        temp = x[0+i]
        temp2 = x[len(x)-i-1]
        x[0+i] = temp2
        x[len(x)-i-1] = temp
    return x

def selectionSort(x: list):
    """Human-like manner of sorting numbers, it gets the smallest number and puts it first, then it gets the second smallest one, and so on."""
    sortedA = [] 
    smallest = 9999999999999999999999999
    y = x 
    for i in range(len(y)): 
        for n in x: 
            if n <= smallest: 
                smallest = n 
        sortedA.append(smallest)
        x.remove(smallest) 
        smallest = 9999999999999999999999999
    return sortedA

def bogoSort(x: list):
    """Shuffles numbers randomly until it is sorted. Best case is O(n)."""
    sortedA = []
    while not isSorted(x, True):
        rdn = random.randint(0, len(x)-1)
        if rdn < len(x)-1:
            x[rdn], x[rdn+1] = x[rdn+1], x[rdn]
        else:
            x[rdn], x[rdn-1] = x[rdn-1], x[rdn]
    return x

def stalinSort(x: list):
    """Removes every number out of order. Not considered a real sort."""
    sortedA = []
    prevNum = None
    for n in x:
        if prevNum == None:
            prevNum = n
            sortedA.append(n)
        else:
            if n >= prevNum:
                prevNum = n
                sortedA.append(n)
            elif n < prevNum:
                pass
    return sortedA

#def bubbleSort(x: list):
    """If it identifies a set of two numbers out of order, it swaps them. Does not support repeated numbers. aaaand it doesn't even work, wow."""
    prevNum = None
    while not isSorted(x, False):
        for n in x:
            if prevNum == None:
                prevNum = n
            else:
                if n >= prevNum:
                    prevNum = n
                elif n < prevNum:
                    temp = x[x.index(n)-1]
                    temp2 =  x[x.index(n)]
                    x[x.index(n)-1] = temp2
                    x[x.index(n)] = temp
    return flipList(x)

def bin2dec(x: str):
    """Converts binary to decimal. Input x must be a string."""
    charCounter = len(x)-1
    outputNum = 0
    for char in x:
        if char == "0":
            charCounter -= 1
        elif char == "1":
            outputNum += 2**charCounter
            charCounter -= 1
    return outputNum

def dec2bin(x: int):
    """Converts decimal to binary. Input x must be an integer."""
    outputNum = ""
    if (x == 0 or x == 1):
        return x
    while x > 1:
        rem = x % 2
        outputNum = outputNum + str(int(rem))
        x = x / 2
    return outputNum[::-1]

def hex2dec(x: str):
    """Converts hexadecimal to decimal. Input x must be a string."""
    cIndex = len(x)-1
    result = 0
    for char in x:
        try:
            char = int(char) * 16**cIndex
        except:
            if char == "A":
                char = 10 * 16**cIndex
            elif char == "B":
                char = 11 * 16**cIndex
            elif char == "C":
                char = 12 * 16**cIndex
            elif char == "D":
                char = 13 * 16**cIndex
            elif char == "E":
                char = 14 * 16**cIndex
            elif char == "F":
                char = 15 * 16**cIndex
        result += char
        cIndex -= 1
    return result

def hex2bin(x: str):
    """Converts hexadecimal to binary. Input x must be a string."""
    table = {
        "A": 1010,
        "B": 1011,
        "C": 1100,
        "D": 1101,
        "E": 1110,
        "F": 1111
    }
    result = ""
    for char in x:
        # could be more efficient.
        if table.get(char, None) == None:
            if len(str(dec2bin(int(char)))) == 1:
                result = result + "000" + str(dec2bin(int(char)))
            elif len(str(dec2bin(int(char)))) == 2:
                result = result + "00" + str(dec2bin(int(char)))
            elif len(str(dec2bin(int(char)))) == 3:
                result = result + "0" + str(dec2bin(int(char)))
            else:
                result = result + str(dec2bin(int(char)))
        else:
            result = result + str(table.get(char, 0))
    return result
