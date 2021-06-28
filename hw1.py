def computing(a, b):
    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a

    result = {}
    result['합'] = num1+num2
    result['차'] = num1-num2
    result['곱'] = num1*num2
    result['몫'] = num1//num2

    return result

nums = []

while True:
    int1 = int(input('0 이 아닌 정수 입력  : '))

    if int1 == 0:
        nums.clear()
    else:
        nums.append(int1)

    if len(nums) >= 2:
        break

print('num1= ', nums[0], ' num2= ', nums[1])

dict1 = computing(nums[0], nums[1])

for key in dict1:
    print(key, ' : ', dict1[key], end = '      ')
