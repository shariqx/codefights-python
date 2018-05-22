def lineEncoding(s):
    curr_char = s[0]
    curr_count = 0
    out = ''
    for a in s:
        if a != curr_char:
            if curr_count > 1:
                out+=str(curr_count) + curr_char
            else:
                out+=curr_char
            curr_count = 1
            curr_char = a
        else:
            curr_count+=1
    out+=(str(curr_count) if curr_count > 1 else '')+ curr_char
    return out


print(lineEncoding("abbcabb"))
