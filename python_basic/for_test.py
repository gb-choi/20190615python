'''
list = ['one', 'two', 'three']
for i in list:
    print(i)
'''

'''
a = [(1,2), (3,4), (5,6)]

for (first, last) in a:
    print(first + last)
'''

'''
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
'''

'''
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)
'''

'''
sum = 0

for i in range(1, 11):
    sum = sum + i

print(sum)
'''

'''
birth = input("주민번호를 입력해주세요:")

if len(birth) != 14:
    print('잘못 입력 하셨습니다')
else:
    year = birth[:2]
    month = birth[2:4] 
    date = birth[4:6]
    gender = birth[6:8]
    gender = int(gender)
    if gender % 2 ==0:
        gender = '여성'
        
    else:
        gender = '남성'

        
print("{}년{}월{}일 출생 {}입니다".format(year, month, date, gender))

'''

'''
i = 2
j = 1
while i <= 9:
    while j <= 9:
        print (i, 'x',  j, '=', i * j)
        j = j + 1
    i = i + 1
    j=1
    print()
'''
'''
coffee = {'아메리카노':2500, '카페라떼':3000, '카푸치노':3500}

for c in coffee:
    print(c, end=' ')
print()

order = input("선택 : ")
for k,v in coffee.items():
    if k==order:
        print(v)
    else:
        print("해당 상품이 없습니다.")
'''
'''
import random 

count = 0

print("\n■테스트를 시작하려면 '1'을 입력해주세요")
print("■테스트를 종료하려면 '0'을 입력해주세요")
choose = int(input("--> "))

for x in range(0,5):
    if choose == 1:
        while(True): 
                    
            a = random.randint(1,50) 
            b = random.randint(1,50) 
        
            print("\n\n(+)덧셈은 '1'\n(-)뺄셈은 '2'\n (E)프로그램 종료는 '0'\n선택한 값을 입력해주세요")
            choose = int(input("--> "))
            
            if choose == 1:
                print(a,"+",b)
                result = int(input("= "))
                if result == a+b:
                    print("\n♥정답입니다~!")
                else:
                    print("\n▶틀렸습니다..")
        
            elif choose == 2:
                print(a,"-",b)
                result = int(input("= "))
                if result == a-b:
                    print("\n♥정답입니다~!")
                else:
                    print("\n▶틀렸습니다..")

            elif choose == 0:
                print("\n◎프로그램이 종료되었습니다.")
                break

                
    elif choose == 0:
        print("\n◎프로그램이 종료되었습니다")
print("%d 개 맞음" %count)
'''

'''
import random
num1 = random.randint(1,50)
num2 = random.randint(1,50)

print("첫번째수: ",num1)
print("두번째수: ",num2)


print('연산을 정하세요')
print('1.덧샘  , 2.뺄샘 , 3.곱셈 , 4.나눗셈')

hod = int(input('선택:'))
sum = num1 + num2
sum1 = num1 - num2
sum2 = num1 * num2
sum3 = num1 / num2

if hod == 1:
    print('두수의 합은 {} 입니다'.format(sum))
elif hod == 2:
    print('두수의 차는 {} 입니다'.format(sum1))
elif hod == 3:
    print('두수의 곱은 {} 입니다'.format(sum2))
else:
    print('두수의 나눗셈은 {} 입니다'.format(sum3))

'''
'''
import random

lotto = random.randint(1,99)

user = int(input("복권 번호를 입력하세요(1~99사이):"))

lotto1 = lotto // 10
lotto2 = lotto % 10

user1 = user // 10
user2 = user % 10

if (lotto1 == user1)and(lotto2 == user2):
    print('당첨 번호는 {} 입니다'.format(lotto))
    print('상금은  100 만원 입니다')
elif (lotto1 == user1)or(lotto2 == user2):
    print('당첨 번호는 {} 입니다'.format(lotto))
    print('상금은  50 만원 입니다')
else:
    print('당첨 번호는 {} 입니다'.format(lotto))
    print('당신은 멍청이 입니다')
'''

'''
import time

input("엔터 누르고 시작후 20초 셉니다")
start = time.time()
input("20초 세고 엔터를 누르세요")
end = time.time()
et = end - start
print("실제시간 :" , et, "초")
print("차이 : ", abs(et -20), "초")
'''
'''
import random
import time

number = random.randint(1,100)
count = 0
input("시작!")
start = time.time()
while True:
    guess = int(input('숫자를 입력하세요 :'))
    count += 1
    if guess == number:        
        print('정답입니다. {}번 만에 맞추셨습니다'.format(count))        
        break
    elif guess > number:        
        print('더 작은 수 입니다')
    else:
        print('더 큰 수 입니다.')
end = time.time()
et = end - start
print("걸린시간은 {:.0f}초 입니다.".format(et))
'''

'''
import random

for i in range(0,5):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print("로또 : ",lotto)
'''



import random
number = str(random.randint(1,999)).zfill(3)
count = 0
 
while True:
    guess = input('3자리 숫자를 입력하세요 :')
    count += 1
    if guess == number:
        print('정답입니다. {}번 만에 맞추셨습니다'.format(count))
        break
 
    strike = 0
    ball = 0
    answer = list(number)   
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
            answer[i] = 's'
 
    for i in range(3):
        if guess[i] in answer:
            ball += 1
            answer[answer.index(guess[i])] = 'b'
    print(strike,ball, answer)