        max,i,j=0,0,0
        s=s+' '
        while max<len(s)-i:
            for i in range(len(s)):
                j=i+max
                while j<len(s):
                    s1=s[i:j]
                    if s1[::-1]==s1:
                        max=j-i
                        chuan=s1
                    j=j+1
        return chuan