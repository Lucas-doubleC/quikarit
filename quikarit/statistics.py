def mean(x: list):
    """Gets the arithmetic mean of a list"""
    return sum(x) / len(x)

def median(x: list):
    """Gets the median of a list"""
    if len(x) % 2 != 0:
        return x[int((len(x)+1)/2)-1]
    else:
        return (x[int(len(x)/2)-1] + x[int(len(x)/2)]) / 2

def geoMean(x: list):
    """Gets the geometric mean of a list."""
    s = x[0]
    x.remove(x[0])
    for n in x:
        s = s*n
    return (s**(1/(len(x)+1)))

def mode(x: list):
    """Gets the mode of a list."""
    occs = {}
    for e in x:
        occs.update({e: x.count(e)})
    return max(occs, key=occs.get)

def standardDeviation(x: list):
    """Calculates the standard deviation of a list x. (Population standard deviation)"""
    result = 0
    xMean = mean(x)
    for i in range(len(x)):
        result += (x[i]-xMean)**2
    return ((1/len(x))*result)**(1/2)