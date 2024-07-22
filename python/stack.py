def isValid(s):
    b = [["(", ")"], ["[", "]"], ["{", "}"]]
    stack = []
    for x,e in enumerate(s):
        if e == b[0][0]:
            stack.append(b[0][1])
        elif e == b[1][0]:
            stack.append(b[1][1])
        elif e == b[2][0]:
            stack.append(b[2][1])
        elif e == b[0][1] and not not stack:
            if stack.pop() != e:
                return False
        elif e == b[1][1] and not not stack:
            if stack.pop() != e:
                return False
        elif e == b[2][1] and not not stack:
            if stack.pop() != e:
                return False
        else:
            return False
    if not stack:
        return True
    else:
        return False