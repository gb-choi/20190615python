'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무가 넘어갔습니다.")
'''

'''
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input("숫자를 입력하세요 : "))
'''

'''
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d 개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''

'''
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요! : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d 를 주고 커피를 줍니다." % (money -300))
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d 개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''

'''
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
'''

# 1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오.
'''
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: 
        result += i
    i += 1

print(result)
'''
# 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = 0

while A:
    mark = A.pop()
    if mark >=50:
        total += mark
print(total)
'''
# 별 표시하기
'''
i = 0
while True:
    i += 1
    if i > 4 : break
    print('*' * i)
'''
