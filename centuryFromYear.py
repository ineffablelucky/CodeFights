# Given a year, return the century it is in.
# The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    cent=1
    if year%100==0:
        cent=year//100
    else:
        cent=(year//100)+1
    return cent
