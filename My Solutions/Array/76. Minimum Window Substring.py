def minWindow(s: str, t: str) -> str:
    """
    s - m
    t - n
    """
    def getCountMap(s, n):
        mt = dict()
        for i in range(n):
            c = s[i]
            if not c in mt.keys():
                mt[c] = 1
            else:
                mt[c] += 1
        return mt
    def isSContainsTLetters(mt, ms):
        for k in mt.keys():
            if not k in ms.keys():
                return False
            else:
                if ms[k] < mt[k]:
                    return False
        return True
    def getNextLeft2(start, end, s, m, t, n, ms, mt):
        stop_end = False
        stop_start = False
        while ((not stop_end or not stop_start) and start < end and end < m):
            if not stop_start:
                c = s[start]
                if c in mt.keys():
                    stop_start = ms[c] - 1 < mt[c]
                    if not stop_start:
                        start += 1
                        ms[c] -= 1
                else:
                    start += 1
                    ms[c] -= 1

            if not stop_end:
                c = s[end]
                if c in mt.keys():
                    stop_end = ms[c] - 1 < mt[c]
                    if not stop_end:
                        end -= 1
                        ms[c] -= 1
                else:
                    end -= 1
                    ms[c] -= 1
        return s[start:end+1], start, end
    def getNextLeft(start, end, s, m, t, n, ms, mt):
        stop_end = False
        stop_start = False
        while ((not stop_end or not stop_start) and start < end and end < m):
            
            if not stop_start:
                c = s[start]
                if c in mt.keys():
                    stop_start = ms[c] - 1 < mt[c]
                    if not stop_start:
                        start += 1
                        ms[c] -= 1
                else:
                    start += 1
                    ms[c] -= 1

            if not stop_end:
                c = s[end]
                if c in mt.keys():
                    stop_end = ms[c] - 1 < mt[c]
                    if not stop_end:
                        end -= 1
                        ms[c] -= 1
                else:
                    end -= 1
                    ms[c] -= 1
        return s[start:end+1], start, end

    m = len(s)
    n = len(t)
    ms = getCountMap(s, m)
    mt = getCountMap(t, n)
    if not isSContainsTLetters(mt, ms):
        return ""

    start = 0
    end = m - 1
    min_sub = s[start:end+1]
    while(start + n < m and end < m):
        sub, start, end = getNextLeft(start, end, s, m, t, n, ms, mt)
        
        min_sub = sub if isSContainsTLetters(mt, ms) and len(sub) <= len(min_sub) else min_sub
        c = s[start]
        if c in ms.keys():
            ms[c] -= 1
        start += 1
        if (start > m):
            break
        # c = s[start]
        # if c in ms.keys():
        #     ms[c] += 1

        while(not isSContainsTLetters(mt, ms) and end < m):
            end += 1
            if end >= m :
                end -=1
                break
            c = s[end]
            if c in mt.keys():
                ms[c] += 1
            

    return min_sub
