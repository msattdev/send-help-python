def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0h0m0s"
    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    
    seconds = 0
    while totalSeconds >= 1:
        seconds += 1
        totalSeconds -= 1
    
    hms = []
    if hours > 0:
        hms.append(str(hours) + "h")
    if minutes > 0:
        hms.append(str(minutes) + "m")
    if seconds > 0:
        hms.append(str(seconds) + "s")
    return ''.join(hms)

print(getHoursMinutesSeconds(45))        # Should print "45s"
print(getHoursMinutesSeconds(125))       # Should print "2m5s"
print(getHoursMinutesSeconds(3600))      # Should print "1h"
print(getHoursMinutesSeconds(3665))      # Should print "1h1m5s"
print(getHoursMinutesSeconds(7325))      # Should print "2h2m5s"
print(getHoursMinutesSeconds(0))         # Should print "0h0m