# 호출 스택(콜 스택)
# 프로그램에서 함수가 호출되면, 해당 함수의 호출 정보를 스택에 저장

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

factorial(5)