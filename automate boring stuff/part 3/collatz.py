# Write your code here :-)
def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3*number + 1
        print(result)
        return result


terminatingFlag = False

while not terminatingFlag:
    print('Please enter the integer value you want')
    try:
        value = int(input())
    except ValueError:
        print('Program terminating..You should enter the number not a string')
        break
    result = collatz(value)
    while result != 1:
        result = collatz(result)
    terminatingFlag = True
