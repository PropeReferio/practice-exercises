#Write a function to return if the given year is a leap year. A leap year is 
#divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Determines if a year is a leap year"""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        elif a_year % 100 != 0:
            return True
    else:
        return False

def test_leap_year(test_min, test_max):
    """Tests is_leap_year by printing years that return 'True'"""
    for year in range(test_min, test_max):
        test = is_leap_year(year)
        if test == True:
            print(year)

test_leap_year(1, 2001)



