print("일반계산기 프로그램입니다!")
first = input("계산할 첫 번째 값을 입력해주세요: ")
second = input("계산할 두 번째 값을 입력해주세요: ")

first = int(first)
second = int(second)

print("두 개의 값:", first, "와", second)

print("더하기 값 (a + b):", first + second)
print("빼기 값 (a - b):", first - second)
print("곱하기 값 (a * b):", first * second)
print("정수 나누기 값 (a // b):", first // second)
print("실수 나누기 값 (a / b):", first / second)