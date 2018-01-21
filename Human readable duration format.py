# 4kyu

def format_duration(seconds):
    if seconds == 0:
        return "now"
    year = seconds // (365 * 24 * 3600)
    seconds = seconds % (365* 24 * 3600)
    day = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    seconds = seconds
    time = {'ayears':year, 'days':day, 'hours':hour, 'minutes':minutes, 'seconds':seconds}
    string, los = '', []
    for key, val in sorted(time.iteritems()):
        if val == 0:
            continue
        elif val == 1:
            if key[0] == 'a':
                s = str(val) + " " + key[1:-1]
            else:
                s = str(val) + " " + key[:-1]
        elif val > 1:
            if key[0] == 'a':
                s = str(val) + " " + key[1:]
                print s
            else:
                s = str(val) + " " + key
        los.append(s)
    for i in los:
        if len(los) - los.index(i) - 1 > 1:
            string += i + ", "
        elif len(los) - los.index(i) - 1 == 1:
            string += i + " and "
        elif len(los) - los.index(i) - 1 == 0:
            string += i
        
    return string


print format_duration(1) # , "1 second")
print format_duration(62) # , "1 minute and 2 seconds")
print format_duration(120) # , "2 minutes")
print format_duration(3600) # , "1 hour")
print format_duration(3662) # , "1 hour, 1 minute and 2 seconds")
print format_duration(132030240) # , "4 years, 68 days, 3 hours and 4 minutes")