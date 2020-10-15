from datetime import datetime
def timeConversion(s):
    stime = datetime.strptime(s,"%I:%M:%S%p")
    return stime.strftime("%H:%M:%S")

s = input()
result = timeConversion(s)
print(result)