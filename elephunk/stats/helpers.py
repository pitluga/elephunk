def percent(numerator, denominator, decimals=2):
    if denominator == 0:
        return "infinity"
    return "%.4g%%" % (float(numerator)/float(denominator) * 100)
