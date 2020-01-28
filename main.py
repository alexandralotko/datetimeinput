'''
from datetime import datetime
expectedforamt = '%Y-%m-%d %H:%M:%S'
dt = datetime.strptime('2019-05-03 22:04:00', expectedforamt)
print(dt)

from datetime import datetime
expectedforamt = '%Y-%m-%d %H:%M:%S'
dt = datetime.strptime('2019-Jan-03 22:04:00', expectedforamt)
print(dt)
'''

''' year must be between 1900 and 2020, month must be between 1 and 12, day must be between 1 and 31, hour must be between 1 and 24, minutes and seconds must be between 1 and 59 '''

while yeari == None:
    year = input("Enter the year: ")
    try:
        yeari = int(year)
    except:
        pass

    if yeari is not None:
        
        if yeari < 1900:
            print("The year must be greater than 1900.")
            yeari = None
        elif yeari > 2020:
            print("The year must be less than 2020.")
            yeari = None
        else:
            print("The year is valid")
    else:
        print("The year "+year+" is invalid.")



while monthi == None:
    month = input("Enter the month: ")
    try:
        monthi = int(month)
    except:
        pass
    if monthi is not None:
        if monthi < 1:
            print("The month must be greater 0.")
            monthi = None
        elif monthi > 12:
            print("The month must be less than 13.")
            monthi = None
        elif monthi < 10:
            month = "0" + month
        else:
            print("The month is valid")
    else:
        print("The month "+month+" is invalid.")



while dayi == None:
    day = input("Enter the day: ")
    try:
        dayi = int(day)
    except:
        pass
    if dayi is not None:
        if dayi < 1:
            print("The day must be greater 0.")
            dayi = None
        elif dayi > 31:
            print("The day must be less than 32.")
            dayi = None
        elif dayi < 10:
            day = "0" + day
        else:
            print("The day is valid")
    else:
        print("The day "+day+" is invalid.")




while houri == None:
    hour = input("Enter the hour: ")
    try:
        houri = int(hour)
    except:
        pass
    if houri is not None:
        if houri < 1:
            print("The hour must be greater 0.")
            houri = None
        elif houri > 24:
            print("The hour must be less than 25.")
            houri = None
        elif houri < 10:
            hour = "0" + hour
        else:
            print("The hour is valid")
    else:
        print("The hour "+hour+" is invalid.")



while minutei == None:
    minute = input("Enter the minute: ")
    try:
        minutei = int(minute)
    except:
        pass
    if minutei is not None:
        if minutei < 1:
            print("The minute must be greater 0.")
            minutei = None
        elif minutei > 59:
            print("The minute must be less than 60.")
            minutei = None
        elif minutei < 10:
            minute = "0" + minute
        else:
            print("The minute is valid")
    else:
        print("The minute "+minute+" is invalid.")



while secondi == None:
    second = input("Enter the second: ")
    try:
        secondi = int(second)
    except:
        pass
    if secondi is not None:
        if secondi < 1:
            print("The second must be greater 0.")
            secondi = None
        elif secondi > 59:
            print("The second must be less than 60.")
            secondi = None
        elif secondi < 10:
            second = "0" + second
        else:
            print("The second is valid")
    else:
        print("The second "+second+" is invalid.")

print (year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second)