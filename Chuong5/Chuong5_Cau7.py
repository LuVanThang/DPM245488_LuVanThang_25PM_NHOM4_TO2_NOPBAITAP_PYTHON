def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip())!=0:
            s2=s2+word+" "
    return s2.strip()
s=" TRần duY thAnH "
s=s.title()
s=ToiUuChuoi(s)
print(s)