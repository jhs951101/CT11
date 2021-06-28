def gcd(num1, num2, *nums):
    if num1 > num2:
        min1 = num2
    else:
        min1 = num1

    for i in range(0, len(nums), 1):
        if min1 > nums[i]:
            min1 = nums[i]

    stack = []

    for n in range(1, min1+1, 1):
        beZero = True

        if num1%n != 0 or num2%n != 0:
            beZero = False

        if beZero:
            for i in range(0, len(nums), 1):
                if nums[i]%n != 0:
                    beZero = False
                    break

            if beZero:
                stack.insert(0, n)

    return stack[0]

list1 = []

for i in range(0, 4, 1):
    list1.append( int(input('정수' + str(i+1) + ' 입력  :  ')) )

print( str(list1[0]) + ',  ' + str(list1[1]) + '의 최대공약수  : ', gcd(list1[0], list1[1]) )
print( str(list1[0]) + ',  ' + str(list1[1]) + ',  ' + str(list1[2]) + '의 최대공약수  : ', gcd(list1[0], list1[1], list1[2]) )
print( str(list1[0]) + ',  ' + str(list1[1]) + ',  ' + str(list1[2]) + ',  ' + str(list1[3]) + '의 최대공약수  : ', gcd(list1[0], list1[1], list1[2], list1[3]) )
