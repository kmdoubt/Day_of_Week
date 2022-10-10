
def weekday(month, day, year):
    leap_years = (year-1)//4
    y = ((year-1)*365)+leap_years
    if (month.lower() == 'february') or (month == 2):
        y = y + 31
    elif (month.lower() == 'march') or (month == 3):
        if (year%4 == 0):
            y = y + 60
        else:
            y = y + 59
    elif (month.lower() == 'april') or (month == 4):
        if (year%4 == 0):
            y = y + 91
        else:
            y = y + 90  
    elif (month.lower() == 'may') or (month == 5):
        if (year%4 == 0):
            y = y + 121
        else:
            y = y + 120
    elif (month.lower() == 'june') or (month == 6):
        if (year%4 == 0):
            y = y + 151
        else:
           y = y + 151
    elif (month.lower() == 'july') or (month == 7):
        if (year%4 == 0):
            y = y + 183
        else:
            y = y + 182
    elif (month.lower() == 'august') or (month == 8):
        if (year%4 == 0):
            y = y + 213
        else:
            y = y + 212
    elif (month.lower() == 'september') or (month == 9):
        if (year%4 == 0):
            y = y + 244
        else:
            y = y + 243
    elif (month.lower() == 'october') or (month == 10):
        if (year%4 == 0):
            y = y + 274
        else:
            y = y + 273
    elif (month.lower() == 'november') or (month == 11):
        if (year%4 == 0):
            y = y + 305
        else:
            y = y + 304
    elif (month.lower() == 'december') or (month == 12):
        if (year%4 == 0):
            y = y + 335
        else:
            y = y + 334

    y = y+day

    y = y%7
    
    if (y == 0):
        return "Saturday"
    elif (y == 1):
        return "Sunday"
    elif (y == 2):
        return "Monday"
    elif (y == 3):
        return "Tuesday"
    elif (y == 4):
        return "Wednesday"
    elif (y == 5):
        return "Thursday"
    elif (y == 6):
        return "Friday"