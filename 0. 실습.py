## 사이트 비밀번호

# url = "http//:google.co.kr"
# site = url.replace("http//:","")
# site = site[:site.index(".")]
# password = site[0:3] + str(len(site)) + str(site.count("e"))
# print(password)


## 오늘의 운세

# import random
# solution = [
#     "좋은일이 생길거야",
#     "조심하렴",
#     "그저그런 하루",
#     ]
# today = random.randint(0, len(solution)-1)
# print(solution[today])


## 총점과 평균 구하기

# subject = ["korean", "english", "math"]
# point = [7, 8, 9]
# total = 0
# avr = 0
# points = point.copy()
# while points:
#     total += points.pop()
#     avr = total / len(point)
# print(total, avr)


## 늘어나는 숫자

# c= 0
# for a in range(10):
#     c += 1
#     for b in range(c):
#         print(b, end = " ")
#     print()


## 구구단 출력

# for a in range(1, 10):
#     for b in range(1, 10):
#         print("{}X{}={}".format(b, a, a*b), end = "\t")
#     print()


## 로또번호

# import random
# lotto = []
# while len(lotto) <= 5:
#     numbers = random.randint(1, 45)
#     if numbers not in lotto:
#         lotto.append(numbers)
#         number = len(lotto) - 1
#         print("당첨번호 : " + str(lotto[number]))
# lotto.sort()
# print("최종번호 : " + str(lotto))


## 연금복권 번호

# import random
# number = random.randint(1, 5)
# lotto = []
# while len(lotto) <= 5:
#     numbers = random.randint(0, 9)
#     lotto.append(numbers)
# print("{}조".format(number), lotto[::-1])


## 알파벳 카운트

# text = "pineapple"
# dic = {word:text.count(word) for word in text}
# print(dic)


## 긴 단어 추출하기

# word = "Today's my favorite day"
# text = word.split()
# dic = {len(num):num for num in text}
# co = max(dic.keys())
# print(dic[co])


## code 단순화

# ls = range(10)
# data1 = [num1**2 for num1 in ls]
# data2 = [num2 for num2 in ls if num2 % 2]
# data3 = ["홀" if num3 %2 else "짝" for num3 in ls]
# data4 = list(filter(lambda data: True if data % 2 else False, ls))

# print(data1)
# print(data2)
# print(data3)
# print(data4)


## 비밀번호생성(데코)


# def disp(func):
#     def wapper(*args, **kwargs):
#         pw = "1234"
#         pw_input = input("password? : ")
#         if pw == pw_input:
#             result = func(*args, **kwargs)
#         else:
#             result = "XXX"
#         print(result)
#         return result
#     return wapper

# @disp
# def plus(a, b):
#     result = a + b
#     return a + b

# plus(5, 5)
