

def solution(S):
    if len(S) % 2 is not 0:
        return 0
    else:
        stack = []
        for i in S:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) is 0:
                    return 0
                else:
                    if not valid_pair(stack.pop(), i):
                        return 0
    if len(stack) is not 0:
        return 0
    return 1


def valid_pair(first, last):
    if first is '(' and last is ')':
        return True
    elif first is '{' and last is '}':
        return True
    elif first is '[' and last is ']':
        return True
    else:
        return False


if __name__ == '__main__':
    # print(solution(')('))
    # print(solution('())(()'))
    # print(solution('{[()()]}'))
    print(solution('{{{{'))
