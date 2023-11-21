import datetime
'''
print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print("======")
print(datetime.today().strftime("%Y%m%d%H%M%S"))
'''
print(datetime.datetime.today().strftime("%Y-%m-%d"))

print(str(datetime.datetime.today())[:10])
print(str(datetime.datetime.today())[:10]) # today() 함수를 사용해 오늘의 날짜, 시간을 IO

                                                                           # str() 함수를 사용해 출력하려는 내용을 string 형태로 IO

                                                                           # [:10]를 사용해 10글자만 출력하도록 하여 년, 월, 일만 출력하도록  함