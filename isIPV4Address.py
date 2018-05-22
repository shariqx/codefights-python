def isIPv4Address(inputString):
    sp_lit = inputString.split('.')
    if len(sp_lit) != 4:
        return False
    for i in range(0, len(sp_lit)):
        if not sp_lit[i].isdigit():
            return False
        if not 0 <= int(sp_lit[i]) <= 255:
            return False
    return True


print(isIPv4Address('172.16.254.1'))