import sys


def combination(cnt, prev):
    global N
    global num_operators
    global nums
    global expr
    global max_val

    if cnt == num_operators:
        # 새로운 식 만들기
        new_expr = []
        check = False
        for i in range(N):
            if check:
                check = False
                continue
            if i%2 == 1 and nums[i//2] == 1:
                new_expr[-1] = calc(new_expr[-1], expr[i+1], expr[i])
                check = True
            else:
                new_expr.append(expr[i])

        # 새로운 식 계산하기
        result = int(new_expr[0])
        for i in range(len(new_expr)):
            if i%2 == 1:
                result = calc(result, new_expr[i+1], new_expr[i])

        # 최대값 갱신하기
        max_val = max(max_val, result)

        return

    if prev == 0:
        nums[cnt] = 1
        combination(cnt+1, 1)
        nums[cnt] = 0
        combination(cnt+1, 0)
    else:
        nums[cnt] = 0
        combination(cnt+1, 0)


def calc(operand1, operand2, operator):
    result = int(operand1)
    operand2 = int(operand2)
    if operator == '+':
        result += operand2
    elif operator == '-':
        result -= operand2
    elif operator == '*':
        result *= operand2
    return result


N = int(input())
num_operators = (N-1)//2

nums = [0 for _ in range(num_operators)]
expr = list(input())

max_val = -sys.maxsize
combination(0, 0)

print(max_val)
