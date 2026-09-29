def solution(s):

    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
            
        else:
            if not stack:
                return False
            else:
                stack.pop()

        # print(stack)
    
    if stack:
        return False
    else:
        return True
    

if __name__ == "__main__":
    s1 = "()()"	
    print(solution(s1))

    s2 = "(())()"
    print(solution(s2))

    s3 = ")()("	
    print(solution(s3))

    s4 = "(()("	
    print(solution(s4))