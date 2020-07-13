def Maximum(value1, value2, value3):
    """
    This function takes 3 int arguments and returns the highest value
    """
    maxValue = value1
    if value2 > maxValue:
        maxValue = value2
    if value3 > maxValue:
        maxValue = value3
    return maxValue