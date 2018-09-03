'''A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".'''


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
