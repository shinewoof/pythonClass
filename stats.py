import sys
import collections

inputParams = sys.argv
del inputParams[0]
inputNum = [int(params) for params in inputParams]
inputNum.sort()

#print('your input (in ascending order):'+ str(inputNum))

#宣告為有排序的dict
result = collections.OrderedDict()


#數量
numLen = len(inputNum)
#總和
result['sum'] = sum(inputNum)
#平均
result['mean'] = result['sum'] / numLen
#中位數
if (numLen % 2 == 0):
    key = numLen // 2
    result['med'] = (inputNum[key] + inputNum[ key+1 ]) / 2
else:
     key = numLen // 2
     result['med'] = (inputNum[key])
#最小值
result['min'] = min(inputNum)
#最大值
result['max'] = max(inputNum)

#樣本標準差 & 眾數 處理
numMode = []
tmpNum = 0
for num in inputNum:
    tmpNum += (num - result['mean']) ** 2
    if (inputNum.count(num) >= 2 and numMode.count(num) == 0 ):
        numMode.append(num)

#樣本標準差
result['std'] = (tmpNum / numLen) ** 0.5 

#無眾數時處理
if(len(numMode) == 0):
    numMode = list(set(inputNum))

#眾數
numMode.sort()

for k,v in result.items():
    output = "{key:>4s}: {num:->15.2f}".format(key=k,num=v)
    print(output)

#為了眾數排序 單獨印
print("{key:>4s}: {num}".format(key='mode',num=numMode))

