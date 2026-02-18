def solveQuadratic(expr: str):
    """Solves quadratic equations in the form of ax^2 + bx + c = 0."""
    resultList = []
    a = ''
    b = ''
    c = ''
    count = 0
    for char in expr:
        if char == 'x':
            break
        if char == '+' or char == '-':
            count += 1
        if count == 0:
            a += char
    count = 0
    for char in expr:
        if char == '+' or char == '-':
            count += 1
        if count == 1:
            if char == 'x':
                break
            b += char
    count = 0
    for char in expr:
        if char == '+' or char == '-':
            count += 1
        if count == 2:
            c += char
    count = 0
    a, b, c = float(a), float(b), float(c)
    x = (-b + (((b**2) - (4*a*c))**0.5)) / (2*a)
    resultList.append(x)
    y = (-b - (b**2 - (4*a*c))**0.5) / (2*a)
    resultList.append(y)
    return resultList

def summation(upperLimit: int, variable: str, startingValue: int, expr: str):
    """Calculates the summation of an expression. The only operations supported are *, -, /, +."""
    summationResult = 0
    prevExpr = expr
    openParentheses = False
    exprinParentheses = ''
    for i in range(upperLimit-startingValue+1):
        for char in expr:
            if openParentheses and char != "(" and char != ")":
                exprinParentheses += char
            if char == variable and prevChar.isalnum():
                expr = expr.replace(variable, str("*"+(i+startingValue)))
                exprinParentheses = exprinParentheses.replace(variable, str("*"+(i+startingValue)))
            elif char == variable:
                expr = expr.replace(variable, str((i+startingValue)))
                exprinParentheses = exprinParentheses.replace(variable, str((i+startingValue)))
            elif char == "(":
                openParentheses = True
            elif char == ")" and openParentheses:
                openParentheses = False
                expr = expr.replace("("+exprinParentheses+")", str(eval(exprinParentheses)))
            else:
                prevChar = char
        summationResult += eval(expr)
        exprinParentheses = ''
        expr = prevExpr
    return summationResult

def product(upperLimit: int, variable: str, startingValue: int, expr: str):
    """Calculates the product of an expression. The only operations supported are *, -, /, +."""
    prodResult = 1
    prevExpr = expr
    openParentheses = False
    exprinParentheses = ''
    for i in range(upperLimit-startingValue+1):
        for char in expr:
            if openParentheses and char != "(" and char != ")":
                exprinParentheses += char
            if char == variable and prevChar.isalnum():
                expr = expr.replace(variable, str("*"+(i+startingValue)))
                exprinParentheses = exprinParentheses.replace(variable, str("*"+(i+startingValue)))
            elif char == variable:
                expr = expr.replace(variable, str((i+startingValue)))
                exprinParentheses = exprinParentheses.replace(variable, str((i+startingValue)))
            elif char == "(":
                openParentheses = True
            elif char == ")" and openParentheses:
                openParentheses = False
                expr = expr.replace("("+exprinParentheses+")", str(eval(exprinParentheses)))
            else:
                prevChar = char
        prodResult = prodResult * eval(expr)
        exprinParentheses = ''
        expr = prevExpr
    return prodResult

def factorial(x):
    for i in range(x-1):
        x *= i+1
    return x

def sin(x: float, accuracy=None):
    """Calculates the sine of x with specified accuracy using the Taylor series."""
    operator = False
    result = x
    iNumber = 3
    if accuracy != None:
        for i in range(accuracy):
            if not operator:
                result -= x**iNumber/(factorial(iNumber))
            elif operator:
                result += x**iNumber/(factorial(iNumber))
            iNumber += 2
            operator = not operator
        return result
    else:
        for i in range(2):
            if not operator:
                result -= x**iNumber/(factorial(iNumber))
            elif operator:
                result += x**iNumber/(factorial(iNumber))
            iNumber += 2
            operator = not operator
        return result
    
def cos(x: float, accuracy=None):
    """Calculates the cosine of x with specified accuracy using the Taylor series."""
    operator = False
    result = 1
    iNumber = 2
    if accuracy != None:
        for i in range(accuracy):
            if not operator:
                result -= x**iNumber/(factorial(iNumber))
            elif operator:
                result += x**iNumber/(factorial(iNumber))
            iNumber += 2
            operator = not operator
        return result
    else:
        for i in range(2):
            if not operator:
                result -= x**iNumber/(factorial(iNumber))
            elif operator:
                result += x**iNumber/(factorial(iNumber))
            iNumber += 2
            operator = not operator
        return result
    
def tan(x: float, acc=None):
    """Calculates the tangent of x with specified accuracy."""
    if acc != None:
        return sin(x, accuracy=acc)/cos(x, accuracy=acc)
    else:
        return sin(x)/cos(x)
    
def arctan(x: float, acc=None):
    """Calculates the arctan of x with specified accuracy using the Maclaurin series."""
    operator = False
    result = x
    iNumber = 3
    if acc != None and x >= -1 and x <= 1:
        for i in range(acc):
            if not operator:
                result -= x**iNumber/(iNumber)
            elif operator:
                result += x**iNumber/(iNumber)
            iNumber += 2
            operator = not operator
        return result
    elif acc == None and x >= -1 and x <= 1:
        for i in range(20):
            if not operator:
                result -= x**iNumber/(iNumber)
            elif operator:
                result += x**iNumber/(iNumber)
            iNumber += 2
            operator = not operator
        return result
    elif acc != None and x > 1:
        operator = True
        iNumber = 1
        result = 3.141592653589793/2
        result2 = 0
        for i in range(acc):
            if not operator:
                result2 -= 1/(iNumber*x**iNumber)
            elif operator:
                result2 += 1/(iNumber*x**iNumber)
            iNumber += 2
            operator = not operator
        return result-result2
    elif acc == None and x > 1:
        operator = True
        iNumber = 1
        result = 3.141592653589793/2
        result2 = 0
        for i in range(20):
            if not operator:
                result2 -= 1/(iNumber*x**iNumber)
            elif operator:
                result2 += 1/(iNumber*x**iNumber)
            iNumber += 2
            operator = not operator
        return result-result2
    elif acc != None and x < -1:
        operator = True
        iNumber = 1
        result = -3.141592653589793/2
        result2 = 0
        for i in range(acc):
            if not operator:
                result2 -= 1/(iNumber*x**iNumber)
            elif operator:
                result2 += 1/(iNumber*x**iNumber)
            iNumber += 2
            operator = not operator
        return result-result2
    elif acc == None and x < -1:
        operator = True
        iNumber = 1
        result = -3.141592653589793/2
        result2 = 0
        for i in range(20):
            if not operator:
                result2 -= 1/(iNumber*x**iNumber)
            elif operator:
                result2 += 1/(iNumber*x**iNumber)
            iNumber += 2
            operator = not operator
        return result-result2

def rad2deg(x: float, acc=None):
    """Converts radians to degrees."""
    pi = "3.14159265358979323846264338327"
    if acc != None:
        return x * (180/float(pi[:acc+2]))
    else:
        return x * (180/3.14159)

def deg2rad(x: float, acc=None):
    """Converts degrees to radians."""
    pi = "3.14159265358979323846264338327"
    if acc != None:
        return x * (float(pi[:acc+2])/180)
    else:
        return x * (3.14159/180)

def slopeAngle(x: str):
    """Calculates the angle of the slope of a linear function (in radians), in the form of y=mx+b."""
    mx = ''
    m = ''
    inMx = True
    inM = True
    for char in x:
        if mx == '' and char.isdecimal() and inMx or mx == '' and char == 'x' and inMx:
            mx += char
            if char == 'x':
                inMx = False
                break
    for char in mx:
        if char.isdecimal():
            m += char
        elif char == 'x':
            if m == '':
                m = 1
            break
    return arctan(float(m), acc=30)

def findSlopebyAngle(x: float):
    """Finds the slope (mx) by the angle. Similar to tan(x)."""
    return round(tan(x)*1000)/1000