def solution(numbers):
    answer = []
    for number in numbers:
        binnum = convert2fullbin(number)
        answer.append(int(check(binnum)))
    return answer

def makeBin(num) -> str:
    tmp = ''
    while num>0:
        tmp = str(num%2) + tmp
        num = num//2
    return tmp

def convert2fullbin(num) -> str:
    binNum = makeBin(num)
    n, s = 0, 1
    while len(binNum)> s:
        n += 1
        s += 2**n
    return binNum.zfill(s)

#가능한 값인지 계산하기
def check(number) :
    length = len(number)
    if length == 1 or '0' not in number or '1' not in number:
        return True
    mid = int(length//2)
    if number[mid] == '0':
        return False
    
    return check(number[:mid]) and check(number[mid+1:])   